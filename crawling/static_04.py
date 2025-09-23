# shop_base2_tbl

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
import tqdm


# terminal에서 pip install tqdm
import tqdm # 진행되는 정도 표시 

for page_num in tqdm.tqdm(range(1,47)):
    datas = coffedb.get_data(page_num)
    with get_connection() as conn:
        with conn.cursor() as cur:
            for data in datas:
                try:
                    sql = 'insert into shop_base2_tbl values(%s,%s,%s,%s,%s)'
                    cur.execute(sql, (data[0],data[1],data[2],data[3],data[4]))
                except pymysql.err.IntegrityError:
                    sql = '''update shop_base2_tbl
                                set shop_state=%s, shop_addr=%s,shop_phone_num=%s
                            where area=%s and shop_name=%s
                    '''
                    cur.execute(sql, (data[2],data[3],data[4],data[0],data[1]))
                    conn.commit()
                else:
                    conn.commit()



# with get_connection() as conn:
#     with conn.cursor() as cur:
#         for data in datas:
#             try : 
#                 sql = 'insert into shop_base2_tbl values(%s, %s, %s, %s, %s)'
#                 cur.execute(sql, ('서울', '서초점', '영업중', '서울 서초구', '9102-2010'))
#             except pymysql.err.IntegrityError:
#                 sql = '''update shop_base2_tbl 
#                         set shop_addr=%s, shhop_date=%s, sop_phone+number=%s 
#                         where shop_area=%s and shop_name=%s'''
#                 cur.execute(sql, ('영업중', '서울 서초구', '9102-2010', '서울', '서초점'))
#                 conn.commit()
#             else :
#                 conn.commit()