import streamlit as st
'''
세션상태를 이용하면 재실행해도 세션 변수 공유 가능
이전 세션에서 변경한 상태를 저장하고 그대로 유지 가능
'''
st.title('세션 상태 예제')

# 세션 상태 초기화
if 'count' not in st.session_state:
    st.session_state['count'] = 0
    
if 'register' not in st.session_state:
    st.session_state['register'] = []
    
# 텍스트 입력 위젯
clientInput = st.text_input('이름 입력', value='이름을 입력', key = 'name')

# 버튼 입력 위젯
submitBtn = st.button('등록')

if submitBtn:
    st.session_state['count'] += 1
    st.write('버튼 입력 횟수: ', st.session_state['count'])
    
    name = st.session_state['name']
    st.session_state['register'].append(name)
    st.write('등록된 인원 리스트', st.session_state['register'])

# streamlit run ./source/sessionState.py