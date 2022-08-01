import logging
from typing import Tuple

import lxml.html
import readability

#debugログを表示されないようにする
#邪魔なので
logging.getLogger('readability.readability').setLevel(logging.WARNING)

def get_content(html: str) -> Tuple[str, str]:
    #HTMLの文字列から(title, text)のtupleを取得する
    document = readability.Document(html)
    content_html = document.summary()

    #HTMLタグを除去して本文のテキストのみを取得する
    content_text = lxml.html.fromstring(content_html).text_content().strip()
    short_title = document.short_title()
    
    return short_title, content_text