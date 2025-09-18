import streamlit as st
st.title('반가워요') # 제목
st.write('첫번째 앱') # 밑에 쓰는 거 
st.header("헤더")
st.subheader("서브헤더")
st.button("button")
st.checkbox("체크 박스")
st.radio("레디오 박스", ('a', 'b', 'c'))
st.selectbox("셀렉트 박스", ("일번", "이번"))
st.slider("슬라이더", 0,100,50) #최대 최소 기본값
name = st.text_input("이름을 입력하세요")
st.write(f'안녕하세요 {name}님!!')
