import requests
# 데이터 요청할 주소 
url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1'
# 서버에 보낼 데이터(1페이지 보여달라는 의미) 

from_data = {
    'pageNo' : 1, # 여러개를 주고 싶으면 밑에 추가 
    'sido' : '',
    'gugun' : '',
    'store' : ''

}

response =requests.post(url, data=from_data)
print(response.text[:500])
