# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class UniqloItem(Item):
    # define the fields for your item here like:
    name = Field()
    code = Field()
    currency = Field()
    price = Field()
    oldprice = Field()
    tags = Field()
    colors = Field()
    sizes = Field()
    imageUrl = Field()
    imageName = Field()
    material = Field()
    care = Field()
    description = Field()
