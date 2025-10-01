import streamlit as st

st.title("🎈It's my app")
st.write("안녕하세요!! 오늘은 10월1일 입니다.")

st.info("success")
st.success("만나서 반가워.나는 아카자!")
st.image("https://ojsfile.ohmynews.com/STD_IMG_FILE/2025/0812/IE003508187_STD.jpg")

with st.expander("ℹ️ 우리나라 지도"):
    import pandas as pd
    df = pd.DataFrame({"lat":[37.5],"lon":[127.8]})
    st.map(df,zoom=14)

sidebar_1 = st.sidebar
sidebar_1.title("사이드바 메뉴")
sidebar_1.link_button("연습장","/workspaces/streamlit_1001/streamlit_app.py")
sidebar_1.link_button("게임","/workspaces/streamlit_1001/pages/연습장.py")


col1, col2 = st.columns(2)  # 2개의 열 생성
with col1:
    name = st.text_input("이름을 입력하세요.")
    if name != "":
        st.write(f"{name}")
with col2:
    age = st.number_input("나이를 입력하세요.",step=1)
    if age > 0:
        st.write(f"{2025-age}년에 태어남")

color = st.selectbox("좋아하는 색상",["빨강","파랑","녹색"])
st.write(f"선택한 색상:{color}")
if color == "빨강":
    st.error("빨강을 좋아함")
elif color == "파랑":
    st.info("파랑이 좋음")
elif color == "녹색":
    st.success("녹색이 짱")

date = st.date_input("날짜를 입력하세요.")
# st.write(date)







# image = st.camera_input("사진을 찍어보세요.")
# if image:
#     st.image(image)

# import openai

# # 사용자에게 직접 API 키를 입력받음
# user_api_key = st.text_input("🔐 OpenAI API 키를 입력하세요", type="password")

# # 입력값이 있을 때만 GPT 호출
# if user_api_key:
#     openai.api_key = user_api_key

#     # GPT 테스트 호출
#     if st.button("GPT에게 물어보기"):
#         with st.spinner("GPT가 생각 중입니다..."):
#             try:
#                 response = openai.ChatCompletion.create(
#                     model="gpt-3.5-turbo",
#                     messages=[{"role": "user", "content": "Streamlit이 뭐야?"}]
#                 )
#                 st.write("GPT 응답:", response["choices"][0]["message"]["content"])
#             except Exception as e:
#                 st.error(f"오류 발생: {e}")