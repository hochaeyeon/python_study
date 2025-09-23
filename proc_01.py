# 데이터베이스 연결
#.env, .gitignore은 상단에 있어야함. 
    # 1. 환경변수 로드 
    # 2. os를 이용해서 환경변수의 값 읽어서 connection 객체를 생성
    # 3. connection 객체의 cursor 객체를 생성 
    # 4. 커서객체의 callproc('프로시저 이름', [, , , ,])

import pymysql
from dotenv import load_dotenv
import os
# .env 로드
load_dotenv()

# 1. DB 연결
conn = pymysql.connect(host = os.getenv('DB_HOST'),
        user = os.getenv('DB_USER'),
        password = os.getenv('DB_PASSWORD'),
        database= 'sqldb'
    )

with conn as conn:
    with conn.cursor() as cursor:
        cursor.callproc('AddCoderwithTransaction', ['PRO', 'P10', '소', 0, 'Y']) # 프로시저 호출
        for row in cursor.fetchall():
            print(row)

conn.commit() 



# 프로시저 호출 