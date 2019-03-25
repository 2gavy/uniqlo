# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from crawler.spiders import util
from crawler.settings import *
import json
import logging


class MongoPipeline(object):
    def __init__(self):
        # set logger
        self.logger = util.set_logger('pipeline', LOG_FILE_PIPELINE)

        # Initialise mongo server
        self.db = util.set_mongo_server()

    def process_item(self, item, spider):
        try:
            if "name" in item:
                self.db[MONGODB_COLNAME].insert(dict(item))

        except Exception as ex:
            self.logger.warn('Pipeline Error (others): %s %s' %
                             (str(ex),  str(item)))
