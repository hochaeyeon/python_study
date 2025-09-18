# 가상환경에서 진행하는게 좋음pip install pymysql
import pymysql
# 1. db 연결
conn = pymysql.connect(host='127.0.0.1',
                user  = 'root',
                passwd = 'root1234',
                database='shopdb'
                )
print('접속 성공')
conn.close() # 접속 해제 

# 2. 각 테이블멸
    # 4. c -insert
    # 5. R - select
    # U - update
    # D - delete

# 3. 메소드
    # 회원가입
    # 상품 정보 출력
    # 삼품 구입
    # 상품정보 입력
    # 대시보드 : 고객별 상품별 구매횟수, 평균 구매액 
# 4. 기능 구현과 테스트가 되면, .. streamlit으로 UI 구성  - 템플릿화면을 보고 유사한 형태로 구현 


