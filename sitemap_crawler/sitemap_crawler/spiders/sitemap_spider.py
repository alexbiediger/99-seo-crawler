# -*- coding: utf-8 -*-
from scrapy.spiders import SitemapSpider

class Sitemap404Crawler(SitemapSpider):
    name = "sitemap_404"
    sitemap_urls = [
        'https://dw.99.co/landed-address-sitemap.xml',
        'https://dw.99.co/landed-address-srp-rent-sitemap.xml',
        'https://dw.99.co/landed-address-srp-sale-sitemap.xml',
    ]

    handle_httpstatus_list = [404]

    def parse(self, response):
        yield {'status': response.status, 'url': response.url, }
