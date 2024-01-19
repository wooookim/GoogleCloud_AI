'''
widget - btn
'''

import streamlit as st

st.title('스트림릿의 버튼 입력 예제')

st.subheader('Button Widgets 예제')

clicked = st.button('버튼 1')
st.write('버튼 1 상태: ', clicked)
if clicked :
    st.write('버튼 1을 클릭했습니다.')
else:
    st.write('버튼 1을 클릭하지 않았습니다.')

clicked = st.button('버튼 2')
st.write('버튼 2 클릭 상태: ', clicked)
if clicked :
    st.write('버튼 2을 클릭했습니다.')
else:
    st.write('버튼 2을 클릭하지 않았습니다.')
    


'''
st.checkbox(label, [value])
- label : 체크박스 옆 표시할 문자열
- value : 초기상태(True/False)
'''
st.subheader('체크박스 예제')

checked1 = st.checkbox('체크박스 1')
st.write('체크박스 1 상태: ', checked1) 
if checked1:
    st.write('체크박스 1을 체크')
else:
    st.write('체크박스 1을 체크하지 않음')
    
checked2 = st.checkbox('체크박스 2', value=True)
st.write('체크박스 2 상태: ', checked2) 
if checked2:
    st.write('체크박스 2을 체크')
else:
    st.write('체크박스 2을 체크하지 않음')

    
'''
st.radio(label, options, [index, horizontal])
- label : 라디오 버튼에 표시될 문자열
- options : 라디오 버튼의 선택 항목 라벨을 담고 있는 튜플 또는 리스트
- index : 초기선택 항목의 인덱스 번호(0부터 시작)
- horizontal : 선택 항목 라벨 배치 방향(True : 가로 / False : 세로) 기본값 false
'''
st.subheader("라디오 버튼 예제")

radio_options = ['10', '20', '30', '40']
selected_radio = st.radio('5 * 5 + 5 결과', radio_options)
st.write('선택한 답: ', selected_radio)

radio_options2 = ['축구', '야구', '농구', '발야구']
selected_radio2 = st.radio('가장 좋아하는 운동', radio_options2, index=3, horizontal=True)
st.write('선택한 운동: ', selected_radio2)


'''
st.selectbox(label, opntion, [index])
- radio 옵션과 동일
'''
st.subheader('선택박스 사용 예제')

selectbox_options1 = ['보티첼리', '피카소', '고흐', '램브란트']
selected_option1 = st.selectbox('좋아하는 화가', selectbox_options1)
st.write('당신의 선택: ', selected_option1)

# [실습] '----' 출력 제외
selectbox_options2 = ['-'*30,'보티첼리', '피카소', '고흐', '램브란트']
selected_option2 = st.selectbox('좋아하는 화가', selectbox_options2)
# if selectbox_options2[0] not in selected_option2:
#     st.write('당신의 선택: ', selected_option2)
    
if selected_option2 == selectbox_options2[0]:
    pass
else:
    st.write('당신의 선택: ', selected_option2)
    
    
'''
st.text_input(label, [value, max_char, type])
- label : 텍스트 입력에 표시할 문자열
- value : 입력창 초기에 보여줄 문자열(placeholder)
- max_chars : 최대 입력 가능 문자열 수
- type : 입력 텍스트 형식 지정(기본값 : 입력 문자, passord: ●)
'''
st.subheader('텍스트 입력 예제')

userid = st.text_input('아이디 입력', value='kim', max_chars=15)
userpw = st.text_input('비밀번호 입력', value='1234', max_chars=15, type='password')
if userid == 'kim':
    if userpw == '1234':
        st.write('<h2>로그인 되었습니다.</h2>', unsafe_allow_html=True)
    else:
        st.write('<h2>잘못된 비밀번호 입력됨.</h2>', unsafe_allow_html=True)
else:
    st.write('<h2>존재하지 않는 아이디.</h2>', unsafe_allow_html=True)
    

# streamlit run ./source/inputWidgets.py