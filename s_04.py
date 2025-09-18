# 1~100 데이터 100개 랜덤하게 생성
import streamlit as st
import random

data = [random.randint(1, 100) for i in range(10)] # randint 하면 중복허용하지 않고 100개 포함한 리스트 출려함. 

st.bar_chart(data)
st.line_chart(data)
st.area_chart(data)
col1, col2 = st.columns(2)
with col2:
    st.write("선 그래프")
    st.line_chart(data)
with col1:
    st.write("막대 그래프")
    st.bar_chart(data)
col2.line_chart(data)