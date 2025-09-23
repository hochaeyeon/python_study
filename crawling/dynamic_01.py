#rl = 'https://www.coffeebeankorea.com/store/store.asp'

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get('https://www.google.com/')

# 검색창 요소 찾기 : (id가 ipt_keyword_recruit인 input 태그 찾음. )
serch_input = driver.find_element(By.CLASS_NAME, 'gLFyf')
serch_input.send_keys('파이썬')
time.sleep(3)
# enter 키 누르기
serch_input.send_keys(Keys.ENTER)
time.sleep(3) # 대략 3초동안 페이지 로드 될때까지 기다림. 
driver.quit()



