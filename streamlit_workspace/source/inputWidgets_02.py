import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd

st.title('스트림릿의 input widgets 예제')

'''
st.color_picker(label, value, [key, on_change, args, disabled])
- label : 클라이언트에게 입력이 어떤 용도로 사용되는 지 설명
- value : 초기값으로 사용될 색상 지정(RGB, HEX 지원)
- key : 위젯의 상태를 식별하고 추적하기 위한 고유 키
'''
st.subheader('colorpicker widgets 예제')

st.markdown('#### color-picker example 1 ####')
color = st.color_picker('색상 선택', '#2D9FEF', key = 1)
st.write('현재 색은 ' + color + '입니다.')
st.markdown(f"<p style ='color : {color}'> 선택된 색이 적용된 텍스트 </p>", unsafe_allow_html=True)


st.markdown('#### color-picker example 2 ####')
color2 = st.color_picker('색상 선택', '#2D9FEF', key = 2, label_visibility='hidden')
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]
fig, ax = plt.subplots()
ax.plot(x, y, color = color2)
st.pyplot(fig)


st.markdown('#### color-picker example 2 ####')
color3 = st.color_picker('색상 선택', '#2D9FEF', key = 3)
bg = f'background-color: {color3}'
st.write(f"<div style='{bg}'> 현재 문장의 배경색 변경 </div>", unsafe_allow_html=True)



'''
st.data_editor(data, [width, height, use_container_width, column_order, num_rows])
'''
st.subheader('data editor widgets 예제')
df = pd.DataFrame([
                    {'streamlit 명령어':'st.write()', '조회수':10, 'is_widget':True},
                    {'streamlit 명령어':'st.balloons()', '조회수':5, 'is_widget':False},
                    {'streamlit 명령어':'st.time_input()', '조회수':3, 'is_widget':True}
                    ])
# st.balloons()
# st.snow()
st.markdown('#### 높이가 변하는 표 ####')
df1 = st.data_editor(df, height=200, num_rows='fixed', key=4)
df2 = st.data_editor(df, height=None, num_rows='fixed', key=5)

st.markdown('#### 넓이가 변하는 표 ####')
df3 = st.data_editor(df, width=1000, num_rows='fixed', key=6)
df4 = st.data_editor(df, width=None, num_rows='fixed', key=7)

st.markdown('#### 컬럼 순서가 변하는 표 ####')
df5 = st.data_editor(df, column_order=('is_widget', 'streamlit 명령어', '조회수'), num_rows='fixed', key=8)
df6 = st.data_editor(df, column_order=None, num_rows='fixed', key=9)

st.markdown('#### 인덱스가 변하는 표 ####')
df7 = st.data_editor(df, column_order=('is_widget', 'streamlit 명령어', '조회수'), num_rows='fixed', key=10, hide_index=True)
df8 = st.data_editor(df, column_order=None, num_rows='fixed', key=11, hide_index=False)

# streamlit run ./source/inputWidgets_02.py