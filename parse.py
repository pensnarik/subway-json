#!/usr/bin/env python3

# Subway data parser

# Copyright Andrey Zhidenkov, 2018 (c)

import os
import sys
import json

from parselab.cache import FileCache
from subway.moscow import MoscowSubway
from subway.spb import SpbSubway

cities = {'Moscow': MoscowSubway, 'Spb': SpbSubway}

class App():

    data = list()

    def run(self):

        for city, parser in cities.items():
            instance = parser()
            self.data = []

            for item in instance.get_list():
                self.data.append(item)

            output = sorted(self.data, key=lambda k: k['name'])

            with open('%s.json' % city.lower(), 'wt') as f:
                json.dump(output, f, ensure_ascii=False, sort_keys=True, indent=4)

if __name__ == '__main__':
    app = App()
    sys.exit(app.run())
