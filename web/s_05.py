import streamlit as st
import random
import time

# 페이지 기본 설정
st.set_page_config(
    page_title="Streamlit 레이아웃 예제",
    layout="wide"  # 전체 페이지를 wide 모드로 설정
)

# 사이드바 메뉴 생성
with st.sidebar:
    st.title("게임")
    selected_menu = st.radio(
        "원하시는 게임를 선택하세요:",
        ["홈", "가위바위보 게임", "숫자 맞추기 게임", "도움말"]
    )

# 메인 컨텐츠 영역
def show_home():
    st.header("홈")
    st.write("환영합니다! 이곳은 홈 페이지입니다.")


IMG = {
    "가위" : r"C:\Python_src\가위.png",
    "바위" : r"C:\Python_src\바위.png",
    "보" : r"C:\Python_src\보.png"
}
# def show_game1():
#     st.header("가위바위보 게임")
#     st.write("가위바위보 게임에 오신 것을 환영합니다!")
#     choices = ["가위", "바위", "보"]
#     user_choice = st.selectbox("가위, 바위, 보 중 하나를 선택하세요:", choices)
#     if st.button("결과 확인"):
#         computer_choice = random.choice(choices)
#         st.write(f"컴퓨터의 선택: {computer_choice}")

#         if user_choice == computer_choice:
#             st.success("비겼습니다!")
#         elif (user_choice == "가위" and computer_choice == "보") or \
#              (user_choice == "바위" and computer_choice == "가위") or \
#             (user_choice == "보" and computer_choice == "바위"):
#             st.success("이겼습니다!")
#         else:
#             st.error("졌습니다!")

# def show_game1():
#     st.header("가위바위보 게임")
#     st.write("가위바위보 게임에 오신 것을 환영합니다!")
#     choices = ["가위", "바위", "보"]
#     user_choice = st.selectbox("가위, 바위, 보 중 하나를 선택하세요:", choices)
#     if st.button("결과 확인"):
#         computer_choice = random.choice(choices)
#         st.write(f"컴퓨터의 선택: {computer_choice}")

#         if user_choice == computer_choice:
#             st.success("비겼습니다!")
#         elif (user_choice == "가위" and computer_choice == "보") or \
#              (user_choice == "바위" and computer_choice == "가위") or \
#             (user_choice == "보" and computer_choice == "바위"):
#             st.success("이겼습니다!")
#         else:
#             st.error("졌습니다!")
def show_game1():
    st.header("가위바위보 게임")
    st.write("가위바위보 게임에 오신 것을 환영합니다!")

    choices = ["가위", "바위", "보"]
    user_choice = st.selectbox("가위, 바위, 보 중 하나를 선택하세요:", choices)

    # 결과 버튼
    if st.button("결과 확인"):
        # 좌/우 컬럼 배치
        col_user, col_vs, col_comp = st.columns([1, 0.2, 1])

        with col_user:
            st.subheader("나")
            st.image(IMG[user_choice], caption=user_choice, use_container_width=True, width = 10)

        with col_vs:
            st.markdown("<h1 style='text-align:center;'>VS</h1>", unsafe_allow_html=True)

        with col_comp:
            st.subheader("컴퓨터")
            comp_ph = st.empty()  # 이미지를 바꿔 끼울 자리

        # 2초 동안 1초마다 랜덤 이미지로 애니메이션
        for _ in range(20):               # 총 2초
            tmp = random.choice(choices)  # 중간 연출용 랜덤
            comp_ph.image(IMG[tmp], caption="고르는 중...", use_container_width=True, width=10)
            time.sleep(0.1)

        # 최종 선택 & 결과 판정
        computer_choice = random.choice(choices)
        comp_ph.image(IMG[computer_choice], caption=computer_choice, use_container_width=True, width=10)

        st.write(f"컴퓨터의 선택: **{computer_choice}**")

        wins = {"가위": "보", "바위": "가위", "보": "바위"}
        if user_choice == computer_choice:
            st.success("비겼습니다!")
        elif wins[user_choice] == computer_choice:
            st.success("이겼습니다! 🎉")
        else:
            st.error("졌습니다! 😭")

def show_game2():
    st.header("숫자 맞추기 게임")
    st.write("숫자 맞추기 게임에 오신 것을 환영합니다!")

    if 'c_num' not in st.session_state:
        st.session_state.c_num = random.randint(1, 100)
    h_num = st.number_input("숫자 입력", 1, 100)

    if st.button("확인"):
        if h_num < st.session_state.c_num:
            st.write("더 큰 수를 입력하세요")
        elif h_num > st.session_state.c_num:
            st.write("더 작은 수를 입력하세요")
        else:
            st.balloons()
            st.success("정답입니다!!")
            if st.button("게임 재시작"):
                st.session_state.c_num = random.randint(1, 100)
                st.write("게임이 재시작되었습니다. 새로운 숫자를 맞춰보세요!")
    
def show_help():
    st.header("도움말")
    st.write("도움이 필요하시다면 아래 연락처로 문의해주세요:")
    st.write("이메일: help@example.com")

# 선택된 메뉴에 따라 해당하는 컨텐츠 표시
if selected_menu == "홈":
    show_home()
elif selected_menu == "가위바위보 게임":
    show_game1()
elif selected_menu == "숫자 맞추기 게임":
    show_game2()
elif selected_menu == "도움말":
    show_help()