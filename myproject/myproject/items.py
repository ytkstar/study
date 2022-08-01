# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyprojectItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class Headline(scrapy.Item):
    """
    ニュースのヘッドラインを表すItem
    """
    title = scrapy.Field()
    body = scrapy.Field()

class Page(scrapy.Item):
    
    #WEBページ
    url = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()

    def __repr__(self):
        #ログへの出力時に長くなりすぎないよう、contentを省略する
        
        p = Page(self)
        if len(
                p['content']
            ) > 100:
            p['content'] = f"{p['content'][:100]}..." #100文字より長い場合は省略

        return super(page, p).__repr__()