# bigdata_work_1
# 웹 크롤링
# 파이썬을 이용한 교촌치킨 매장 정보 크롤링

# BeautifulSoup 라이브러리를 사용하여 HTML 페이지를 크롤링하는 것은 정적 웹 페이지에서만 가능
from bs4 import BeautifulSoup as bs
import urllib.request
# 크롤링한 데이터를 pandas를 사용하여 CSV파일로 저장
import pandas as pd
import datetime
# 웹 브라우저를 원격 조정하는 Selenium 라이브러리를 사용하여 동적 웹 페이지 크롤링 가능
# -- 자바스크립트를 사용하는 동적 웹 페이지는 웹 브라우저에서 자바스크립트가 실행되어야만 크롤링할 데이터가 나타남
from selenium import webdriver

num = 0
def kyochon_store(result):
    # 페이지를 반복해서 url 설정
    for sido in range(1, 30):
        for gungu in range(1, 70):
            # 없는(빈) 페이지일 경우 pass
            try:
                Kyochon_url = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (sido, gungu)
                # url 요청하여 응답 받은 웹 페이지 저장
                html = urllib.request.urlopen(Kyochon_url)
                # BeautifulSoup 객체 생성
                soupKyochon = bs(html, 'html.parser')
                # 필요한 항목만 추출하여 result 리스트에 추가 저장
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
    # pandas를 사용하여 테이블 형태의 데이터프레임을 생성
    kyochon_tbl = pd.DataFrame(result, columns=('store_name', 'store_sido', 'store_gungu', 'store_address'))
    # 테이블을 CSV 파일로 저
    kyochon_tbl.to_csv('C:/Users/kimha/BigData/Kyochon.csv', encoding='cp949', mode='w', index=True)
    print('- 완료 -')
    del result[:]
    
if __name__ == '__main__':
    main()
