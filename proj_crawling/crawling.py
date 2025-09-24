from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # enter키 등을 입력하기위해서
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

from bs4 import BeautifulSoup
import time

import re
url = 'https://www.kia.com/kr/customer-service/center/faq' # 페이지 주소 
#웹 드라이버를 자동으로 설치하고 최신버전을 유지
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# 사이트 접속
driver.get(url)
driver.maximize_window() # 전체 화면으로 실행  옵션
print('사이트 접속했습니다.')
# 사이트가 로드될때까지 기다린다.
time.sleep(3)

for i in range(10):
    try:
        driver.find_element(By.ID,f'accordion-item-{i}-button').click()
        time.sleep(1)
    except Exception as e:
        print(f'error : {e}')


time.sleep(1)
soup = BeautifulSoup(driver.page_source,'html.parser')  #--> 셀리니움 문법을 이용해서 원하는 태그의 속한 텍스트를 추출


titles, bodys = [] , []

#각 panel(div) 단위로 반복
for panel in soup.select("div[data-cmp-hook-accordion='panel']"):
    # panel 안의 <p>만 모으기
    ps = panel.select("p")
    # 텍스트 정리
    texts = []
    for p in ps:
        raw_text = p.get_text(" ", strip=True)      # 태그 제거, 공백 구분
        text = raw_text.replace('\xa0', ' ')        # &nbsp; 제거
        text = re.sub(r'\s+', ' ', text).strip()    # 연속 공백/개행 → 공백 하나
        if text:                                    # 빈 문장은 제외
            texts.append(text)

    if texts:
        # 여러 <p> 문단이 있으면 \n으로 합쳐서 하나의 답변으로 저장
        bodys.append("\n".join(texts))
# print("답변")
# print(bodys[0])
# print('-'*100)  
print("-"*100)
  
titles_soup = soup.select('.cmp-accordion__title')
for title in titles_soup:
    # print(title.text)
    titles.append(title.text)

print("질문")
print(titles[0])
print("-"*100)
print("답변")
print(bodys[0])

result = list(zip(titles,bodys))
#print(result[0])


    # mysql 업로드 코드
# import pymysql
# from dotenv import load_dotenv
# import os
#     # .env 로드
#     load_dotenv()

#     def get_connection():
#         return pymysql.connect(
#             host=os.getenv("DB_HOST"),
#             user=os.getenv("DB_USER"),
#             password=os.getenv("DB_PASSWORD"),
#             database="faq",           # 실제 DB명 (faq 스키마)
#         )

#     with get_connection() as conn:
#         sql = "INSERT INTO faq.tbl (Q, A) VALUES (%s, %s)"
#         with conn.cursor() as cur:
#             cur.executemany(sql, result)   # 여러 행 한 번에 넣기
#         conn.commit()
#     print("✅ MySQL에 저장 완료")