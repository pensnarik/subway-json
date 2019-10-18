from lxml.html import fromstring

from subway.subway_parser import SubwayParser

class MoscowSubway(SubwayParser):

    def russian_date_to_date(self, d):
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
                  'августа', 'сентября', 'октября', 'ноября', 'декабря']
        parts = d.split(' ')
        return '%s-%.2d-%.2d' % (parts[2], months.index(parts[1]) + 1, int(parts[0]))

    def get_coords(self, td):
        a = td.xpath('.//a[contains(@class, "mw-kartographer-maplink")]')
        if len(a) > 0:
            return {'lat': float(a[0].get('data-lat')), 'lon': float(a[0].get('data-lon'))}
        else:
            return {}

    def get_list(self):
        page = self.get_page('https://ru.wikipedia.org/wiki/Список_станций_Московского_метрополитена')
        html = fromstring(page)

        for table_row in html.xpath('//table[@style="text-align:center"]/tbody/tr'):
            columns = table_row.xpath('.//td')
            if len(columns) != 8:
                continue

            line = columns[0].xpath('.//span[@title]')[0].get('title')
            name = columns[1].xpath('.//a')[0].text_content().strip()
            open_date = self.russian_date_to_date(columns[2].text_content().strip())
            depth = columns[4].text_content().strip()
            coords = self.get_coords(columns[6])

            yield({'name': name, 'line': line, 'open_date': open_date, 'depth': depth, 'coords': coords})
