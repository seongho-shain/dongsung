import streamlit as st
st.write("this is page2")
if "name" in st.session_state :
    st.write(st.session_state["name"])
    #호출할 때는 조건문 써서 있는지 확인
    #메인페이지는 과목설명과 로그인 페이지를 만드세요
    #1페이지에는 퀴즈 5문제를 냅니다 객관식으로
    #2페이지는 만들기만 해놓으세요