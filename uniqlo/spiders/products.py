# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_splash import SplashRequest
from uniqlo.items import UniqloItem
import pymongo


class ProductsSpider(scrapy.Spider):
    name = 'products'
    allowed_domains = ['www.uniqlo.com']
    start_urls = ['https://www.uniqlo.com/sg/store//']

    def parse(self, response):
        links = response.css(
            '#navHeader .cateNaviLink a::attr(href)').extract()
        for link in links:
            print(link)
            yield SplashRequest(link, self.parse_categoryLink, meta={'url': link}, args={'wait': 1})

    def parse_categoryLink(self, response):
        itemLinks = response.css(".item > a::attr(href)").extract()
        originalLink = response.meta['url']
        for itemLink in itemLinks:
            yield Request(url=itemLink, meta={'originalLink': originalLink, 'itemLink': itemLink}, callback=self.parse_item)

    def parse_item(self, response):
        item = UniqloItem()

        name = ''.join(response.css(
            "#prodInfo > h1 > span ::text").extract()).strip()
        code = ''.join(response.css(
            "div.basicinfo_wrap > span > ul > li.number::text").extract()).replace("ITEM CODE: ", "").strip()
        currency = ''.join(response.css(
            "div.basicinfo_wrap > span > ul > li:nth-child(2) > div.price-box > meta::attr(content)").extract()).strip()
        price = ''.join(response.css(
            "div.basicinfo_wrap > span > ul > li:nth-child(2) > div > p.special-price > span.price::text").extract())
        oldPrice = ''.join(response.css(
            "div.basicinfo_wrap > span > ul > li:nth-child(2) > div > p.old-price > span.price::text").extract())
        tags = response.css(
            '#prodInfo > div > ul.special > li::text').getall()
        colors = response.css(
            '#listChipColor > li > a::attr(title)').getall()
        sizes = response.css(
            '#prodSelectAttribute > #prodSelectSize > #selectSizeDetail > #listChipSize > li > a > em::text').getall()
        imageUrl = response.css(
            '#prodImgDefault > img::attr(src)').extract()
        imageName = response.css(
            '#prodImgDefault > img::attr(alt)').extract()
        description = ''.join(response.css(
            '#prodDetail > div::text').extract()).strip()
        material = response.css(
            '#prodDetail > div.content > dl.spec > dd:nth-child(2)::text').extract()
        care = response.css(
            '#prodDetail > div.content > dl.spec > dd:nth-child(6)::text').extract()

        item["name"] = name
        item["code"] = code
        item["currency"] = currency
        item["price"] = price
        item["oldprice"] = oldPrice
        item["tags"] = tags
        item["colors"] = colors
        item["sizes"] = sizes
        item["imageUrl"] = imageUrl
        item["imageName"] = imageName
        item["material"] = material
        item["care"] = care
        item["description"] = description
        item["originalLink"] = response.meta['originalLink']
        item["itemLink"] = response.meta['itemLink']
        print(item)
        yield item
