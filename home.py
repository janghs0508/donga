import streamlit as st
st.title('수행평가')
st.subheader('수행평가 과목')
st.text('1234567890')
if st.button("수행평가 하는 방법"):
    st.text("1234567890")
val = st.text_input("이름을 입력하세요")
if st.checkbox('5개 보기') :
        st.text('1')
        st.text('2')
        st.text('3')
        st.text('4')
        st.text('5')
else :
     st.text('숨겼습니다.')
number = ['1', '2', '3', '4', '5']
my_choice = st.selectbox('숫자 선택', number)

if my_choice == number[0] :
        st.write('1을 선택하셨습니다.')
elif my_choice == number[1] :
        st.write('2를 선택하셨습니다.')
elif my_choice == number[2] :
        st.write('3을 선택하셨습니다')
elif my_choice == number[3] :
        st.write('4를 선택하셨습니다')
elif my_choice == number[4] :
        st.write('5를 선택하셨습니다')