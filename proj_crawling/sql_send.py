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
        database='faq'
    )


def insert_result(result):
    with get_connection() as conn:
        sql = "INSERT INTO faq (question, answer) VALUES (%s, %s)"
        with conn.cursor() as cur:
            cur.executemany(sql, result)
        conn.commit()