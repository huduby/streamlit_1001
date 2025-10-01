import streamlit as st
import random

# if "page" not in st.session_state:
#     st.session_state.page = "home"

# # 페이지 전환 함수
# def switch_page(page_name):
#     st.session_state.page = page_name

# # 사이드바 또는 버튼으로 전환
# st.sidebar.button("연습장", on_click=switch_page, args=("streamlit_app"))
# st.sidebar.button("게임", on_click=switch_page, args=("연습장",))

# # 본문 내용 조건부 렌더링
# if st.session_state.page == "home":
#     st.title("🏠 홈 페이지입니다")
#     st.button("Page1으로 이동", on_click=switch_page, args=("streamlit_app",))
# elif st.session_state.page == "page1":
#     st.title("📄 연습장입니다")
#     st.button("홈으로 돌아가기", on_click=switch_page, args=("연습장",))

# # 초기화
# if "target" not in st.session_state:
#     st.session_state.target = random.randint(1, 100)
#     st.session_state.attempts = 0

st.title("🎲 숫자 맞추기 게임")
st.write("1부터 100 사이의 숫자 중 컴퓨터가 고른 숫자를 맞춰보세요!")

# 사용자 입력
guess = st.number_input("숫자를 입력하세요", min_value=1, max_value=100, step=1)

# 버튼 클릭 시 확인
if st.button("확인"):
    st.session_state.attempts += 1
    if guess < st.session_state.target:
        st.warning("너무 작습니다!")
    elif guess > st.session_state.target:
        st.warning("너무 큽니다!")
    else:
        st.success(f"정답입니다! 🎉 {st.session_state.attempts}번 만에 맞췄어요!")
        if st.button("다시 시작하기"):
            st.session_state.target = random.randint(1, 100)
            st.session_state.attempts = 0

st.write(f"시도 횟수: {st.session_state.attempts}")
