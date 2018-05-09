# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GardenflowerspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class GardenFlower(scrapy.Item):
    flower_name = scrapy.Field()
    page = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()

class GardenLeaf(scrapy.Item):
    leaf_name = scrapy.Field()
    page = scrapy.Field()
    file_urls = scrapy.Field()
    files = scrapy.Field()
