import scrapy
import json
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'fast_spider'

    def start_requests(self):
        urls = [
            'https://www.bigboxdelivery.com.br/cat/Alimentos-Basicos',
            'https://www.bigboxdelivery.com.br/cat/Frios-e-Laticinios',
            # 'https://www.bigboxdelivery.com.br/cat/Mercearia',
            # 'https://www.bigboxdelivery.com.br/cat/Bebidas-Nao-Alcoolicas',
            # 'https://www.bigboxdelivery.com.br/cat/Biscoitos-e-Aperitivos',
            # 'https://www.bigboxdelivery.com.br/cat/Limpeza'

        ]
        for url in urls:
            # print('url in start requests = ', url)
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        items = response.css('single-item')
        print('response = ', response.url)
        for i in items:
            yield {
                'name': i.css('span.title::text').get(),
                'brand': i.css('span.brand::text').get(),
                'price': i.css('div.prices span.price::text').get(),
                'image': i.css('a img.item-image').attrib['src']
            }

        # spans = response.css('span.title::text').getall()
        # print('spans = ', spans)

        # next_page = response.css('li a::attr(href)').get()
        # print('#######################')
        # print('next page = ', next_page)
        # next_page = response.css('div.ib-pagination li a').attrib['href']

        pages = response.css('div.ib-pagination li')

        next_page = None
        for i in pages:
            if i.css('span.next').get():
                next_page = i.css('a').attrib['href']

        # print('next page = ', next_page)

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(url=next_page, callback=self.parse)
        # else:
        #     next_page = 'https://www.bigboxdelivery.com.br/cat/Alimentos-Basicos'
        #     yield SplashRequest(url=next_page, callback=self.parse)
