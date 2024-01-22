import streamlit as st
from PIL import Image

st.title('미디어 표시 예제')

'''

'''
st.subheader('이미지 표시 예제')

st.markdown('#### 서버에 있는 이미지 파일 표시 ####')
# 이미지 파일 경로
img_path = './source/data/avenue.jpg'
# 이미지 파일 열기
img_local = Image.open(img_path)
# 이미지 표시
st.image(img_local, width=400, caption='로컬 이미지 표시')


st.markdown('#### 인터넷에 있는 이미지 파일 표시 ####')
# url 지정
img_url = 'data:image/jpeg;base64,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'
# 이미지 표시
st.image(img_url, width=400, caption='인터넷 이미지 표시')



'''
st.video(video_data, [format, start_time])
- video_data : 서버 또는 웹 상 비디오 파일 경로(주소)
- format : 재생할 비디오 데이터 MIME 타입 지정(기본값: video/mp4)
- start_time : 재생 시점 지정(기본값: 0)
'''
st.subheader('비디오 표시 예제')

st.markdown('#### 서버에 있는 비디오 파일 표시 ####')
# 비디오 파일 경로
video_path = './source/data/sample_video.mp4'
# 비디오 파일 열기
video_local = open(video_path, 'rb')
video_bytes = video_local.read()
# 비디오 표시
st.video(video_bytes, format='video/mp4')

'''

'''
st.markdown('#### 유튜브에 있는 비디오 파일 표시 ####')

# 비디오 파일 열기
youtube_path = 'https://youtu.be/WwMckqa6N4E?si=_C97O84LYTWZT3VU'
# 비디오 표시
st.video(youtube_path, format='video/mp4')



'''
[실습]
1. audio 표시
 - 서버에 있는 오디오(mp3)
 - 인터넷에 있는 오디오(wav, mpeg)
 
2. 파일 업로드
 - 파일 읽기
'''
st.markdown('#### 서버에 있는 오디오 파일 표시 ####')
# 오디오 파일 경로
audio_path = './source/data/서연의_하루_TTS_배경음악_short.mp3'
# 오디오 파일 열기
audio_local = open(audio_path, 'rb')
audio_bytes = audio_local.read()
# 오디오 표시
st.audio(audio_bytes, format='audio/mpeg')


st.markdown('#### 인터넷에 있는 오디오 파일 표시 ####')
# 오디오 파일 열기
web_audio_path = 'https://pixabay.com/ko/sound-effects/intense-transition-vol-2-pack-186247/'
# 비디오 표시
st.audio(web_audio_path, format='audio/mpeg')


'''
'''


from io import StringIO
uploaded_file = st.file_uploader("파일을 선택하세요", type=['csv', 'png', 'jpg', 'mp3', 'txt'])
if uploaded_file is not None:
    # 파일을 바이트로 읽기:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)
    
    # 문자열 기반 IO로 변환하기:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)
    
    # 파일을 문자열로 읽기:
    string_data = stringio.read()
    st.write(string_data)

# streamlit run ./source/media.py