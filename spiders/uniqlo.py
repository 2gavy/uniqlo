import scrapy
from scrapy import Request


class UniqloSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'https://www.uniqlo.com/sg/store/',
    ]

    def parse(self, response):
        links = response.css(
            '#navHeader .cateNaviLink a::attr(href)').extract()
        for link in links:
            yield Request(url=link, callback=self.parse_itemLink)

    def parse_itemLink(self, response):
        itemLinks = response.css(".item > a::attr(href)").extract()
        for itemLink in itemLinks:
            yield Request(url=itemLink, callback=self.parse_item)

    def parse_item(self, response):
        try:
            name = ''.join(response.css(
                "#prodInfo > h1 > span ::text").extract())
            print(name.strip())
        except Exception as ex:
            print("No name: " + response.url)
