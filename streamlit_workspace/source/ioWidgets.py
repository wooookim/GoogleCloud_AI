# widget - download Btn
import streamlit as st
import pandas as pd
from io import BytesIO

st.title('스트림릿 다운로드 버튼 사용 예제')
st.subheader('텍스트 파일다운로드 예제')

folder = './source/data/'

'''
st.download_button(label, data, [file_name, mine])
- label : 다운로드 버튼에 표시할 문자열
- data : 다운로드할 데이터(텍스트, 바이너리)
- file_name : 다운로드할 파일 이름 지정(기본값 - 자동지정)
- mine : 다운로드할 파일의 MINE 타입(기본값 - 텍스트 파일은 text/plain, 바이너리는 application/octet-stream)

'''
with open(folder + '서연의_이야기.txt', encoding= 'utf-8') as text_file:
    text_data = text_file.read()
    st.download_button(
        label='텍스트 파일 다운로드',
        data=text_data,
        file_name='서연의_이야기_복사본.txt'
    )

    
'''

'''
st.subheader('이미지 파일 다운로드 예제')
with open(folder + 'sample_image.png', 'rb') as img_file:  # rb : read binary
    st.download_button(
        label='이미지 파일 다운로드',
        data=img_file,
        file_name='sample_image_copied.png',
        mime = 'image/png'
    )


'''

'''
st.subheader('오디오 파일 다운로드 예제')
with open(folder + '서연의_하루_TTS_배경음악_short.mp3', 'rb') as audio_file: 
    st.download_button(
        label='오디오 파일 다운로드',
        data= audio_file,
        file_name='서연의_하루_TTS_배경음악_short_copied.mp3',
        mime = 'audio/mpeg'
    )
    


    
    
# streamlit run ./source/ioWidgets.py