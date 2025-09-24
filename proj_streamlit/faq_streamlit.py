import streamlit as st
import pandas as pd
import pymysql
import os
from sqlalchemy import create_engine, text

# def loaddata():
#     conn = pymysql.connect(
#         host = os.getenv('DB_HOST'),
#         user = os.getenv('DB_USER'),
#         password = os.getenv('DB_PASSWORD'),
#         database='faq'
#     )

#     query = "SELECT 연료, 연도, 차종류, 대수 FROM 자동차테이블;"
#     df = pd.read_sql(query, conn)
#     conn.close()
#     return df

# st.set_page_config(page_title="연료별 차량 데이터", layout="wide")


# st.title("🚗 연료별 차량 데이터")


# 검색어 출력 
st.set_page_config(page_title="연료별 차량 현황", layout="wide")

# 메인 제목
st.title("🚗 연료별 차량 현황 & FAQ")

menu = st.sidebar.selectbox("메뉴", ["연료별 차량 현황", "FAQ"])

if menu == "FAQ":
    st.set_page_config(page_title="FAQ", layout="wide")
    st.title("📌 FAQ")
    st.write("")  # 한 줄 띄우기


    def load_tbl_top10():
        conn = pymysql.connect(
            host="localhost",
            user="root",
            password="root1234",
            database="faq",
            charset="utf8mb4"
        )
        query = """
            SELECT id,
                COALESCE(category, 'TOP10') AS category,
                Q AS question,
                A AS answer
            FROM tbl
            ORDER BY id ASC
            LIMIT 10
        """
        df = pd.read_sql(query, conn)
        conn.close()
        return df

    # ---- 세션 상태 초기화
    if "search_term" not in st.session_state:
        st.session_state.search_term = ""
    if "search_clicked" not in st.session_state:
        st.session_state.search_clicked = False

    def trigger_search():
        st.session_state.search_clicked = True

    # ---- 한 줄: 입력창 + 버튼 (폼 사용 X → 버튼 정렬 깔끔)
    # 세션 상태 초기화
    if "search_clicked" not in st.session_state:
        st.session_state.search_clicked = False

    def trigger_search():
        st.session_state.search_clicked = True


    st.text_input(
            label = "검색어를 입력하고 Enter를 눌러주세요.",  # ✅ label 추가
            key="search_term",
            placeholder="검색어를 입력하세요",
            label_visibility="visible",
            on_change=trigger_search
        )


    # ---- 데이터 로드 & 필터
    df = load_tbl_top10()
    if st.session_state.search_clicked and st.session_state.search_term.strip():
        term = st.session_state.search_term.strip()
        mask = df["question"].str.contains(term, case=False, na=False)
        df = df[mask]

    # ---- 결과 건수 문구 (버튼/엔터로 검색한 후에도 유지)
    if st.session_state.search_clicked:
        st.write(f"🔍 **‘{st.session_state.search_term}’** 에 대한 검색 결과: **{len(df)}건**")

    # ---- 결과 표시
    if df.empty:
        st.warning("검색 결과가 없습니다.")
    else:
        for i, r in df.iterrows():
            with st.expander(f"{i+1}. {r['question']}"):
                st.write(r['answer'])


