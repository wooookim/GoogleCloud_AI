# pip install streamlit
import streamlit as st

# 텍스트 출력
st.title('st.title(문자열) : 제목')

st.header('st.header(문자열) : 헤더')

st.subheader('st.subheader(문자열) : 서브헤더')

st.text('st.text(문자열) : 일반 텍스트')

st.text('st.code(code) : 파이썬 코드')
st.code('num = 1')

function = '''
def hello():
    print('hello streamlit')
'''
st.code(function)

st.markdown('스트림릿에서 **마크다운** 사용이 `가능` :sunglasses:')



# streamlit run ./source/textApp.py