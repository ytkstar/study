from scrapy.spiders import SitemapSpider


class IkeaSpider(SitemapSpider):
    name = 'ikea'
    allowed_domain = ['www.ikea.com']

    custom_settings = {
        'USER_AGENT': 'ikeabot',
    }

    #XMLサイトマップのURLのリスト
    #robots.txtのURLを指定すると、SitemapからXMLサイトマップのURLを取得する.
    sitemap_urls = [
        'https://www.ikea.com/robots.txt',
    ]

    #サイトマップインデックスから辿るサイトマップURLの正規表現のリスト
    #このリストの正規表現にマッチするURLのサイトマップのみを辿る
    #指定しない場合、すべてのサイトマップを辿る
    sitemap_follow = [
        r'prod-ja_JP',
    ]

    #サイトマップに含まれるURLを処理するコールバック関数を指定する
    #指定しない場合、すべてのURLをコールバック関数parseで処理する
    sitemap_rules = [
        (r'/products/', 'parse_product'), #productsのページをparse_productで処理する
    ]

    def parse_product(self, response):
        #製品ページから製品の情報を抜き出す
        yield {
            'url': response.url,
            'name': response.css('#name::text').get().strip(), #名前、本来はタグを確認する
            'type': response.css('#type::text').get().strip(), #種類
            'price': response.css('#pricel::text').re_first('[\S\xa0]+').replace('\xa0', ' '),
        }
        