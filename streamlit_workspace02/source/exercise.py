import streamlit as st
from PIL import Image

st.title('스트림릿의 사이드바 사용 예 ####')

columns = st.columns(4)   # 너비가 다른 3개
folder = './source/data/'
imgFiles = ['vermeer.png', 'Gogh.png', 'Munch.png', 'ShinYoonbok.png']
imgCaption = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']

st.sidebar.title('사이드바')
st.sidebar.subheader('아이디(ID) 입력')
st.sidebar.text_input('아이디 입력', value='id', max_chars=15)
st.sidebar.subheader('패스워드(Password) 입력')
st.sidebar.text_input('비밀번호 입력', max_chars=15, type='password')


st.sidebar.subheader('셀렉트박스 사용 예')
selectbox_options = ['진주 귀걸이를 한 소녀', '별이 빛나는 밤', '절규', '월하정인']
selectedSpecies = st.sidebar.selectbox('좋아하는 작품은?', selectbox_options)
st.sidebar.write('당신의 선택: ', selectedSpecies)


for i in range(len(columns)):
    with columns[i]:
        st.subheader(imgCaption[i])
        st.image(Image.open(folder + imgFiles[i]), caption=imgCaption[i])

for i in range(len(selectbox_options)):
    if selectedSpecies == selectbox_options[i]:
        st.image(Image.open(folder + imgFiles[i]), caption=imgCaption[i])

