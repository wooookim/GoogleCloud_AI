import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from sklearn.datasets import load_iris

'''
대시보드 페이지
'''
iris_dataset = load_iris()
# print(iris_dataset)

# 데이터 프레임으로 변환
df = pd.DataFrame(data = iris_dataset.data, columns = iris_dataset.feature_names)
# print(df.head())

# 품종 정보 추가
df['species'] = iris_dataset.target
# print(df.head())

species_str = {0:'setosa', 1:'versicolor', 2:'virginica'}

def map_species(x):
    return species_str[x]

df['species'] = df['species'].apply(map_species)
#print(df.head())


'''
스트림릿에서 데이터 프레임 표현
- table
- dataframe
'''
# st.table(df.head())
# st.dataframe(df.head())



'''
select box
- sidebar 에 select box를 두고 종을 선택한 후 해당하는 행만 추출
'''
# st.sidebar.title('Iris Species')
# 클라이언트가 선택한 값이 지정
# selectedSpecies = st.sidebar.selectbox('확인할 품종 선택', ['setosa', 'versicolor', 'virginica'])

# 지정된 값을 기반으로 원본 프레임을 필터링해서 출력
#resultDF = df[df['species'] == selectedSpecies]

# st.table(resultDF.head())


'''
[실습]
여러값을 선택할 수 있는 selectbox = multiselect
'''
# st.sidebar.title('Iris Species')
# multi_selectedSpecies = st.sidebar.multiselect('복수 선택', ['setosa', 'versicolor', 'virginica'])

# # 지정된 값을 기반으로 원본 프레임을 필터링해서 출력
# resultDF = df[df['species'].isin(multi_selectedSpecies)]

# st.table(resultDF)


'''
Radio / Slider
'''
st.sidebar.title('Iris Species')
multi_selectedSpecies = st.sidebar.multiselect('복수 선택', ['setosa', 'versicolor', 'virginica'])

# 선택된 품종에서 기준 컬럼을 선택
selectRadio = st.sidebar.radio('기준 컬럼 선택', ['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)'], horizontal=True)

# 선택한 컬럼의 값의 범위 지정
selectRange = st.sidebar.slider('기준 컬럼으로 범위 지정',
                                0.0,   # 시작 값
                                10.0,  # 끝 값
                                (2.5, 7.5)  # 양쪽 범위
                                # value = 2.5   
                                )

# 선택이 끝나면 실행될 버튼
submitBtn = st.sidebar.button('결과 확인')

# slider 선택범위 = selectRange (리스트형태로 최소/최대값 2개 저장)
# selectRange[0] = 최소값, selectRange[1] = 최대값

# 버튼 클릭 후 결과 확인
if submitBtn:
    # multiselect 필터링
    resultDF = df[df['species'].isin(multi_selectedSpecies)]
    # radio / slide 필터링
    resultDF[((resultDF[selectRadio]) >= selectRange[0]) & ((resultDF[selectRadio]) <= selectRange[1])]
    st.table(resultDF)
    

# streamlit run ./source/layout.py