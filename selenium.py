#webdriverのインポート
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome import service as fs

#sleepメソッドのインポート
from time import sleep

#webdriver managerのインポート
from webdriver_manager.chrome import ChromeDriverManager
 
# ブラウザーを起動(ブラウザは非表示にするヘッドレス)
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
chrome_service = fs.Service(executable_path = "CHROMEDRIVER") 

driver = webdriver.Chrome(service = chrome_service, options = options)

# BIGLOBE商品ページにアクセス
driver.get('https://yuyu-tei.jp/game_poc/carddetail/item_detail.php?VER=pack&CID=10227&MODE=sell')

sleep(1)

# 入荷待ちのときの処理と在庫ありのときの処理
if len(driver.find_elements(by = By.XPATH, value = "//*[@id='main']/div[3]/div[1]/div[2]/form/p[5]/span/input")) > 0:
    print('入荷待ち')
else:
    print('在庫あり')

# ブラウザーを終了
driver.quit()
