import re
from urllib import request
from bs4 import BeautifulSoup
import lxml

def scrape(_url):
    # url = "https://www.yayoiken.com"
    _html = request.urlopen(_url)
    soup_base = BeautifulSoup(_html, "lxml")
    # print(soup_base)
    _keyword = 'Python'
    _buta = soup_base.find(string=re.compile(_keyword))
    # print(_buta)

    if _buta != None:
        print("このサイトは...   " + _keyword + "関連のサイトだよ～")
    else:
        print("このサイトは...   " + "いっちょんわからん")

if __name__ == '__main__':
    # scrape('https://qiita.com/Namibillow/items/954c7f9f53682d6dd9c9')
    scrape('https://qiita.com/suzuq/items/f236672bbad7e3b354b2')



