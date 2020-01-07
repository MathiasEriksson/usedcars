# -*- coding: utf-8 -*-
import scrapy


class VaihtoautoSpider(scrapy.Spider):
    name = 'vaihtoauto'
    allowed_domains = ['https://www.nettiauto.com/en/vaihtoautot']
    start_urls = ['http://https://www.nettiauto.com/en/vaihtoautot/']

    def parse(self, response):
        pass
