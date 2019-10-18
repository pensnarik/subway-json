import os
from lxml.html import fromstring

from parselab.parsing import BasicParser
from parselab.network import NetworkManager
from parselab.cache import FileCache

class SubwayParser(BasicParser):

    def __init__(self):
        self.cache = FileCache(namespace='subway-json', path=os.environ.get('CACHE_PATH'))
        self.net = NetworkManager()

    def get_list(self):
        raise NotImplementedError()
