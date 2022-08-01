import scrapy

from myproject.items import Headline 

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['news.yahoo.co.jp']
    start_urls = ['http://news.yahoo.co.jp/']

    def parse(self, response):
        #urlのリストを取得する
        urls = response.css('#uamods-topics > div > div > div > ul > li > a ::attr("href")').getall()

        for url in urls:
            yield response.follow(url, self.parse_topics)
        
    
    def parse_topics(self, response):
        #取得したurlを辿る
        item = Headline() #Headlineオブジェクトを作成
        item['title'] = response.css('#uamods-pickup > div > div > div > h1 ::text').get()
        item['body'] = response.css('#uamods-pickup > div > p ::text').get()
        yield item