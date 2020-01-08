# -*- coding: utf-8 -*-
import scrapy


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
        
        yield {
            'manufacturer': response.xpath('//*[@id="heightForSlogan"]/h1/a/span/text()').get().strip(),
            'model': response.xpath('//*[@id="heightForSlogan"]/h1/a/span/span/text()').get().strip(),
            'price': response.xpath('//*[@id="rightLogoWrap"]/span/span/span/text()').get().strip(),
        }
