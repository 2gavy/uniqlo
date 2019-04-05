# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from uniqlo.spiders import util
from uniqlo.settings import *
import json


class UniqloPipeline(object):
    def __init__(self):
        # Initialise mongo server
        self.db = util.set_mongo_server()

    def process_item(self, item, spider):
        try:
            if "name" in item:
                self.db[MONGODB_COLNAME].insert(dict(item))

        except Exception as ex:
            self.logger.warn('Pipeline Error (others): %s %s' %
                             (str(ex),  str(item)))
