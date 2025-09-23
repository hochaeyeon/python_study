import requests
# 데이터 요청할 주소 
url = 'https://www.hollys.co.kr/store/korea/korStore2.do'
# 서버에 보낼 데이터(1페이지 보여달라는 의미) 

from_data = {
    'pageNo' : 1, # 여러개를 주고 싶으면 밑에 추가 
    'sido' : '',
    'gugun' : '',
    'store' : ''

}

response =requests.post(url, data=from_data)
# print(response.text)

# 터미널에서 pip install beautifulsoup4
from bs4 import BeautifulSoup
# response 에 있는 문자열 된 데이터를 Beautifulsoup 객체로 변환 / Beautifulsoup <- 대문자, 클래스 
soup = BeautifulSoup(response.text, 'html.parser')

# 원하는 정보 추출 
# 아래 경로, F12 -> 원하는 위치에서 우클릭 -> copy -> copyselect
#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr 
str_table_rows = '#contents > div.content > fieldset > fieldset > div.tableType01 > table > tbody > tr'
#soup.select('todody > tr') tbody가 한개 밖에 없어서 가능. 만약 여러개면 가장 먼저 만나는 tbody 

#print(soup.select('tbody > tr'))

store_rows = soup.select(str_table_rows) 
first_store = store_rows[0]
# print(first_store.select('td')[0].text.strip())  # td 하나씩 다 가져옴 / .text 는 태그 제외하고 텍스트만 출력  # 지역
# print(first_store.select('td')[1].text.strip())  # 매장명
# print(first_store.select('td')[2].text.strip())  # 현황
# print(first_store.select('td')[3].text.strip())  # 주소 
# print(first_store.select('td')[5].text.strip()) # 전화번호 
shop_list = []
for row in store_rows:
    shop_list.append({row.select('td')[0].text.strip(),
                      row.select('td')[1].text.strip(),
                      row.select('td')[2].text.strip(),
                      row.select('td')[3].text.strip(),
                      row.select('td')[5].text.strip()})
    


#     print(idx)
#     print(row.select('td')[0].text.strip())
#     print(row.select('td')[1].text.strip())
#     print(row.select('td')[2].text.strip())
#     print(row.select('td')[3].text.strip())
#     print(row.select('td')[5].text.strip())
#     print("*"* 100)


