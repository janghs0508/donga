import streamlit as st
st.title('인증')
value = st.text_input("이름과 비밀번호")
if st.button('저장'):
 st.session_state["a"] = value #선언