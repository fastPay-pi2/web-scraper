import scrapy
import json
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'fast_spider'

    def start_requests(self):
        urls = [
            'https://www.bigboxdelivery.com.br/cat/Alimentos-Basicos',
            'https://www.bigboxdelivery.com.br/cat/Frios-e-Laticinios',
            'https://www.bigboxdelivery.com.br/cat/Mercearia',
            'https://www.bigboxdelivery.com.br/cat/Carnes-e-Pescados-1'
        ]
        for url in urls:
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        items = response.css('single-item')

        for i in items:
            yield {
                'name': i.css('span.title::text').get(),
                'brand': i.css('span.brand::text').get(),
                'price': i.css('div.prices span.price::text').get()
            }

        # spans = response.css('span.title::text').getall()
        # print('spans = ', spans)

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield scrapy.Request(next_page, callback=self.parse)
