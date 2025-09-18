#순환문 사용할 필요 없음.

import streamlit as st
# 숫자 입력 1~100 사이
import random

c_num = random.randint(1, 100)
h_num = st.number_input("숫자 입력", 1, 100)
#st.write("입력한 숫자:", h_num)

if st.button("확인"):
    if h_num < c_num:
        st.write("더 큰 수를 입력하세요")
    elif h_num > c_num:
        st.write("더 작은 수를 입력하세요")
    else:
        st.write("정답입니다!!")
        if st.button("게임 재시작"):
            c_num = random.randint(1, 100)
            st.write("게임이 재시작되었습니다. 새로운 숫자를 맞춰보세요!")