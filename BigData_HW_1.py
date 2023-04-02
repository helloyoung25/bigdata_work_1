from bs4 import BeautifulSoup as bs
import urllib.request
import pandas as pd
import datetime
from selenium import webdriver

num = 0
def kyochon_store(result):
    for sido in range(1, 30):
        for gungu in range(1, 70):
            try:
                Kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido, gungu)
                html = urllib.request.urlopen(Kyochon_url)
                soupKyochon = bs(html, 'html.parser')
                ul_tag = soupKyochon.find("div", {"class": "shopSchList"})
                for store_data in ul_tag.find_all('a'):
                    store_name = store_data.find('strong').get_text()
                    store_address = store_data.find('em').get_text().strip().split('\r')[0]
                    store_sido_gungu = store_address.split()
                    store_sido = store_sido_gungu[0]
                    store_gungu = store_sido_gungu[1]
                    result.append([store_name] + [store_sido] + [store_gungu] + [store_address])
            except:
                pass

def main():
    result = []
    print('Kyochon store crawling >>>>>>>>>>>>>>>>>>>>>>>>>>')
    kyochon_store(result)
    kyochon_tbl = pd.DataFrame(result, columns=('store_name', 'store_sido', 'store_gungu', 'store_address'))
    kyochon_tbl.to_csv('C:/Users/kimha/BigData/Kyochon.csv', encoding='cp949', mode='w', index=True)
    print('- 완료 -')
    del result[:]
    
if __name__ == '__main__':
    main()


# In[ ]:




