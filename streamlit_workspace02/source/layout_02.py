import streamlit as st
from PIL import Image

'''
스트림릿 메인 화면은 기본적으로 세로방향
가로방향으로 변환할 때 화면 분할 형식 사용
st.columns(spec)
- spec: 숫자나 숫자를 요소로 갖는 리스트
'''
st.title('화면 분할 예제')
st.markdown('### 2개로 단 분할 ###')

[col1, col2] = st.columns(2)  # st.container로 리턴

# 첫째 단
with col1:
    st.subheader('첫 번째 비디오')
    # 비디오 표시
    st.video('https://youtu.be/WwMckqa6N4E?si=_C97O84LYTWZT3VU')

# 둘째 단
with col1:
    st.subheader('첫 번째 비디오')
    # 비디오 표시
    st.video('https://youtu.be/WwMckqa6N4E?si=_C97O84LYTWZT3VU')


st.markdown('### 3개로 단 분할 ###')
columns = st.columns([1.1, 1.0, 0.9])   # 너비가 다른 3개

folder = './source/data/'
imgFiles = ['bird.png', 'dog.png']
imgCaption = ['새', '개']

for i in range(len(columns)):
    with columns[i]:
        # st.subheader(imgCaption[i])
        st.image(Image.open(folder + imgFiles[i]), caption=imgCaption[i])



st.markdown('### tab 분할 ###')
tab1, tab2 = st.tabs(['Tab A', 'Tab B'])

with tab1:
    st.image(Image.open(folder + 'dog.png'), caption='강아지')
with tab2:
    st.image(Image.open(folder + 'bird.png'), caption='새')


# css 적용
st.markdown('''
            <style>
            img{
                width: 300px;
            }
            </style>
            ''', unsafe_allow_html=True)




# streamlit run ./source/layout_02.py