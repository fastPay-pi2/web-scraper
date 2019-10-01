import scrapy
import json
from scrapy_splash import SplashRequest

class QuotesSpider(scrapy.Spider):
    name = 'fast_spider'

    def start_requests(self):
        urls = [
            # 'https://www.bigboxdelivery.com.br/cat/Alimentos-Basicos',
            # 'https://www.bigboxdelivery.com.br/cat/Mercearia',
            # 'https://www.bigboxdelivery.com.br/cat/Bebidas-Nao-Alcoolicas',
            # 'https://www.bigboxdelivery.com.br/cat/Bebidas',
            # 'https://www.bigboxdelivery.com.br/cat/Condimentos-e-Molhos',
            # 'https://www.bigboxdelivery.com.br/cat/Biscoitos-e-Aperitivos',
            # 'https://www.bigboxdelivery.com.br/cat/Doces',
            # 'https://www.bigboxdelivery.com.br/cat/Higiene-e-Perfumaria',
            'https://www.bigboxdelivery.com.br/cat/Limpeza'
        ]
        for url in urls:
            # print('url in start requests = ', url)
            yield SplashRequest(url=url, callback=self.parse)

    def parse(self, response):
        pages = response.css('div.ib-pagination li')

        next_page = None
        for i in pages:
            if i.css('span.next').get():
                next_page = i.css('a').attrib['href']

        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield SplashRequest(url=next_page, callback=self.parse)

        items = response.css('div.ib-single-item a')
        for i in items:
            next_page = response.urljoin(i.attrib['href'])
            yield SplashRequest(url=next_page, callback=self.product_callback)


    def product_callback(self, response):
        category_path = response.css('div.ib-breadcrumb li')
        category = category_path[1].css('a::text').get()
        subcategory = category_path[2].css('a::text').get()

        product_info = response.css('div.product-info')

        for info in product_info:
            yield {
                'brand': info.css('h2.brand::text').get(),
                'name': info.css('h1.name::text').get(),
                'price': info.css('p.price span.price::text').get(),
                'category': category,
                'subcategory': subcategory
            }