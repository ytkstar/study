import requests
import os, os.path
from bs4 import BeautifulSoup as soup
from urllib.parse import urljoin, urlparse

store = 'images'
if not os.path.exists(store):
    os.makedirs(store)

url = 'https://www.pokemoncenter-online.com/?main_page=product_list&new=on&sort=new&page=1'
my_header = {
    "User-Agent" : 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
pages_to_crawl = 15

def download(url):
    session = requests.Session()
    res = session.get(url, headers = my_header, stream = True)
    filename = urlparse(url).path.split('/')[-1]
    print(f'Downloading: {filename}...')
    
    with open(os.path.join(store, filename), 'wb') as the_image:
        chunks = res.iter_content(chunk_size = 4096*4)
        for byte_chunk in chunks:
            the_image.write(byte_chunk)

for p in range(1, pages_to_crawl + 1):
    print(f'Scraping page: {p}...')
    session = requests.Session()
    res = session.get(url, headers = my_header, params = {'page': p})
    html_soup = soup(res.text, 'html.parser')
    for img in html_soup.select('#product_list > ul > li > a > img'):
        img_src = img.get('src')
        if not img_src:
            continue
        img_url = urljoin(url, img_src)
        download(img_url)