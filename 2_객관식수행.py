import streamlit as st
st.title('객관식수행')
if st.button('불러오기'):
  if 'a' in st.session_state :
      value = st.session_state["a"]
      number = ['1', '2', '3', '4', '5']
      my_choice = st.selectbox('객관식', number)

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
  else:
      f"값을 먼저 입력해주세요"
number = ['1', '2', '3', '4', '5']
my_choice = st.selectbox('객관식', number)

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