from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor

from myproject.items import Headline

class NewsCrawlSpider(CrawlSpider):
    name = 'news_crawl'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['https://news.yahoo.co.jp/']

    #リンクを辿るためのルールのリスト
    rules = (
            Rule(LinkExtractor(allow = r'/pickup/\d+$'), callback = 'parse_topics'),
    )

    def parse_topics(self, response):
        #トピックスのページからタイトルと本文を抜き出す

        item = Headline()
        item['title'] = response.css('#uamods-pickup > div > div > div > h1 ::text').get()
        item['body'] = response.css('#uamods-pickup > div > p ::text').get()
        yield item