import korean as ko # 임포트 korean
import pandas as pd # 임포트 pandas
import matplotlib as mpl # 임포트 matplotlib
import matplotlib.pyplot as plt # 임포트 matplotlib.pyplot
import numpy as np # 임포트 numpy

ko.korean_setup() # 한글 설정 함수 호출


# 현재 파일의 위치를 불러와 \를 기준으로 분리하여 "file_list"변수에 저장
file_list = __file__.split("\\") 

# file_list를 이용하여 현재파일의 이름 대신 "notExercise.csv"로 변경하여 변수에 저장
load_file = __file__.replace(file_list[-1], "notExercise.csv") 


# 판다스에서 csv파일을 읽어옴
df_noHealthData = pd.read_csv(load_file) 


# 전체 DataFrame에서 특정 column만 가져온 데이터를 리턴하는 함수
def extract_columnName(column_name):
    # DataFrame의 여러 행 중에서 '대분류' 열의 값이 '성별'인 행들만 모두 추출하여 새로운 데이터프레임을 만듦
    df_tmp = df_noHealthData[df_noHealthData['대분류'] == column_name] #    
    return df_tmp

df_large_cate = extract_columnName('지역별')

print()

def extract_data(class_name):
    chart_dict = {}
    for row_index in df_noHealthData.index:
        if (df_noHealthData.loc[row_index, "대분류"] != class_name):
            continue
        for col_index in range(3, len(df_noHealthData.columns)-1):
            title = df_noHealthData.columns[col_index]
            name = df_noHealthData.loc[row_index, "분류"]
            value = df_noHealthData.loc[row_index, df_noHealthData.columns[col_index]]
            if (title not in chart_dict):
                chart_dict[title] = {}
            chart_dict[title][name] = value
    return chart_dict

extract_data('')