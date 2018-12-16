# # -*- coding: utf-8 -*-

# #实验一
# import scrapy
# import re
# import json
# import urllib
# from scrapy.http import Request
# from urllib import parse
# from Spider.items import PcblogItem
#
#
# class PccnblogSpider(scrapy.Spider):
#     name = 'pcblog'
#     allowed_domains = ['blog.sina.com.cn']
#     start_urls = ['http://blog.sina.com.cn/s/articlelist_1197161814_0_1.html']
#
#     def parse(self, response):
#         post_urls = response.css(".atc_title a::attr(href)").extract()
#         post_urls = response.xpath('//*[@class="articleList"]/div/p/span[2]/a/@href').extract()
#         for post_url in post_urls:
#             yield Request(url=parse.urljoin(response.url, post_url),    callback=self.parse_detail)
#         next_url = response.xpath('//*[@class="SG_pgnext"]/a/@href').extract()
#         if next_url != []:
#             yield Request(url=parse.urljoin(response.url,next_url[0]),callback=self.parse)
#             print("next page:" + next_url[0])
#
#     def parse_detail(self, response):
#         _id = response.url[30:-5]
#         _id = 't' + _id
#         url = response.url
#         title = response.css("#{a}::text".format(a=_id)).extract()[0]
#         time = response.xpath('//span[@class="time SG_txtc"]/text()').extract()[0]
#         tags_list = response.xpath('//td[@class="blog_tag"]/h3/a/text()').extract()
#         tags = ",".join(tags_list)
#         content = "".join(response.xpath('//div[@id="sina_keyword_ad_area2"]//*/text()').extract())
#
#         item = PcblogItem()
#         item['url'] = url
#         item['title'] = title
#         item['time'] = time
#         item['tags'] = tags
#         item['content'] = content
#         return item
#     pass


#实验二

import scrapy
import re
import json
import urllib
from scrapy.http import Request
from urllib import parse
from Spider.items import PcblogItem


class PccnblogSpider(scrapy.Spider):
    name = 'pcblog'
    allowed_domains = ['blog.sina.com.cn']
    start_urls = ['http://blog.sina.com.cn/s/articlelist_1197161814_0_1.html']

    def parse(self, response):
        post_urls = response.css(".atc_title a::attr(href)").extract()
        post_urls = response.xpath('//*[@class="articleList"]/div/p/span[2]/a/@href').extract()
        for post_url in post_urls:
            yield Request(url=parse.urljoin(response.url, post_url), callback=self.parse_detail)
        next_url = response.xpath('//*[@class="SG_pgnext"]/a/@href').extract()
        if next_url != []:
            yield Request(url=parse.urljoin(response.url,next_url[0]),callback=self.parse)
            print("next page:" + next_url[0])
    def parse_detail(self, response):
        _id = response.url[30:-5]
        _id = 't' + _id
        url = response.url
        title = response.css("#{a}::text".format(a=_id)).extract()[0]
        time = response.xpath('//span[@class="time SG_txtc"]/text()').extract()[0]
        tags_list = response.xpath('//td[@class="blog_tag"]/h3/a/text()').extract()
        tags = ",".join(tags_list)
        content = "".join(response.xpath('//div[@id="sina_keyword_ad_area2"]//*/text()').extract())
        maintype = 'num'
        URL = url[url.find('_') + 1: -5]
        uid = URL[:8]
        aids = URL[-6:]
        LINK = 'http://comet.blog.sina.com.cn/api?maintype={}&uid={}&aids={}'.format(maintype,uid,aids)
        request = urllib.request.Request(LINK)
        Json = urllib.request.urlopen(request)
        Json = Json.read().decode('utf-8')
        Begin = Json.find('{')
        End = url.rfind('}')
        jsonContent = Json[Begin: End - 1]
        jscon_dict = json.loads(jsonContent)
        fav_nums = jscon_dict[aids]['f']
        read_nums = jscon_dict[aids]['r']
        comment_nums = jscon_dict[aids]['c']
        trans_nums = jscon_dict[aids]['z']
        like_nums = jscon_dict[aids]['d']
        item = PcblogItem()
        item['url'] = url
        item['title'] = title
        item['time'] = time
        item['tags'] = tags
        item['content'] = content
        item['fav_nums'] = fav_nums
        item['read_nums'] = read_nums
        item['comment_nums'] = comment_nums
        item['trans_nums'] = trans_nums
        item['like_nums'] = like_nums
        return item
    pass