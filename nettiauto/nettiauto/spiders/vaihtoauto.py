# -*- coding: utf-8 -*-
import scrapy
import unicodedata

class VaihtoautoSpider(scrapy.Spider):
    name = 'vaihtoauto'
    start_urls = ['https://www.nettiauto.com/vaihtoautot?page=1']

    def parse(self, response):

        # Follow all links to cars in listingsData
        # which are not on "upsell" promotion
        cars_paths = '//div[@id="listingData"]/div[not(contains(@class, "upsellAd"))]/div/a[@class="childVifUrl tricky_link"]/@href'
        for href in response.xpath(cars_paths):
            yield response.follow(href, self.parse_car)
        # add follow pagination links

    def parse_car(self, response):

        data_table = response.xpath('//table[@class="data_table"]')

        yield {
            'manufacturer': response.xpath('//*[@id="heightForSlogan"]/h1/a/span/text()').get().strip(),
            'model': response.xpath('//*[@id="heightForSlogan"]/h1/a/span/span/text()').get().strip(),
            'price': response.xpath('//*[@id="rightLogoWrap"]/span/span/span/text()').get().strip(),
            'year_model': self.year_model_parser(data_table),
        }

    def year_model_parser(self, data_table):
        year_string_raw = data_table.xpath('.//tr[1]/td[2]/text()').get()
        year_string = unicodedata.normalize("NFKD", year_string_raw).strip()
        year = year_string.split()[0]
        return year
