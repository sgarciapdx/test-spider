# -*- coding: utf-8 -*-
import scrapy


class XkcdSpider(scrapy.Spider):
    name = "xkcd"
    allowed_domains = ["10.10.10.10"]
    start_urls = (
        'http://10.10.10.10/',
    )

    def parse(self, response):
        # Safe if Xpath is empty, extract handles it.
        prev_link = response.xpath('//*[@id="middleContainer"]/ul[1]/li[2]/a/@href').extract()
        if prev_link:
            url = response.urljoin(prev_link[0])
            yield scrapy.Request(url, callback=self.parse)
