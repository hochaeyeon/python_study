# 데이터 베이스에 접속 
# insert 쿼리 문을 사용해서 수집한 데이터 db에 저장. 

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
def get_connection():
    return pymysql.connect(
        host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database='shopinfo'
    )

import coffedb

for page_num in range(1,47):
    # with절 리소스 자동 해제
    with get_connection() as conn:
        with conn.cursor() as cur:
            sql = '''
            insert into shop_base_tbl 
                values(null, %s, %s, %s, %s, %s)'''
            #cur.execute(sql, (, , , ,) ) # 하나씩 값을 넣는데, 이걸 리스트로 받고 싶으면
            cur.executemany(sql, coffedb.get_data(page_num)) # 리스트로 받음. 
    
        conn.commit()
