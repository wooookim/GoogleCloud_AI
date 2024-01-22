'''
2. 파일 업로드
 - 파일 읽기
'''
import streamlit as st
from io import StringIO

st.title('스티림릿 파일 업로드 예제')
st.subheader('텍스트 파일 업로드')

'''
st.file_uploader(label, [type, accept_multiple_files])
- type: 기본값 = 모든 파일
- accept_multiple_files : 여러 파일을 동시에 업로드, 기본값 = False
'''
uploaded_file = st.file_uploader("파일을 선택하세요", type=['csv', 'png', 'jpg', 'mp3', 'txt'])
if uploaded_file is not None:
    # 문자열 기반 IO로 변환하기:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    str = stringio.read()
    st.write(str[:50])
    
    # 파일을 바이트로 읽기:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    
    # 파일을 문자열로 읽기:
    string_data = stringio.read()
    st.write(string_data)

# streamlit run ./source/media.py

