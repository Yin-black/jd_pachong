# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdPachongItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id = scrapy.Field()        #产品ID
    company = scrapy.Field()   #品牌
    id_sort = scrapy.Field()   #产品分类
    product = scrapy.Field()   #型号
    price = scrapy.Field()   #价格
    user_product = scrapy.Field()   #好评度
    expression = scrapy.Field()   #设备参数

