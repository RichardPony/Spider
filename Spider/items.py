# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

#实验一
# import scrapy
# class PcblogItem(scrapy.Item):
#     # define the fields for your item here like:
#     # name = scrapy.Field()
#     url = scrapy.Field()
#     title = scrapy.Field()
#     time = scrapy.Field()
#     tags = scrapy.Field()
#     content = scrapy.Field()
#     pass

#实验二
import scrapy
class PcblogItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    time = scrapy.Field()
    tags = scrapy.Field()
    content = scrapy.Field()
    fav_nums = scrapy.Field()
    read_nums = scrapy.Field()
    comment_nums = scrapy.Field()
    trans_nums = scrapy.Field()
    like_nums = scrapy.Field()
    pass