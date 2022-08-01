import scrapy

from myproject.items import Page
from myproject.utils import get_content

class BroadSpider(scrapy.Spider):
    name = 'broad'
    
    #ハテブの新着エントリーページ
    start_urls = ['http://b.hatena.ne.jp/entrylist/all']

    def parse(self, response):
        #新着エントリーページをparse()するメソッド

        #個別のWEBページへのリンクを辿る
        urls = response.css('.entrylist-contents-main > h3 > a::attr("href")').getall()
        for url in urls:
            #parse_page(メソッドをコールバック関数として指定)
            yield scrapy.Request(url, callback = self.parse_page)
        
        #pageの値が1桁である間のみ、次の20件のリンクを辿る
        url_more = response.css('.entrylist-main > section > p > a::attr("href")').re_first(r'.*\?page=\d{1}$')
        if url_more:
            yield response.follow(url_more)
    
    def parse_page(self, response):
        #個別のWEBページをparseする
        #utils.pyに定義したget_content()関数で、titleとtextを抽出する
        title, content = get_content(response.text)

        #Pageオブジェクトを作成してyieldする
        yield Page(url = response.url, title = title, content = content)
