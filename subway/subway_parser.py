import os
from lxml.html import fromstring

from parselab.parsing import BasicParser
from parselab.network import NetworkManager
from parselab.cache import FileCache

class SubwayParser(BasicParser):

    def __init__(self):
        self.cache = FileCache(namespace='subway-json', path=os.environ.get('CACHE_PATH'))
        self.net = NetworkManager()

    def russian_date_to_date(self, d):
        months = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля',
                  'августа', 'сентября', 'октября', 'ноября', 'декабря']
        parts = d.split(' ')
        return '%s-%.2d-%.2d' % (parts[2], months.index(parts[1]) + 1, int(parts[0]))

    def get_list(self):
        raise NotImplementedError()
