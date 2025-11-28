import matplotlib.pyplot as plt
import matplotlib as mpl
import korean
import pandas as pd
import numpy as np


file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "cctv_result.csv")


"""
1. csv 파일을 불러와서 
2. 구별 열을 인덱스로 설정
3. CCTV 수(소계)로 정렬
4. 인구대비 CCTV 비율 계산
5. CCTV 비율로 정렬하여 구별 확인
6. CCTV 수와 인구대비 CCTV 비율 순위 비교

"""

# csv파일을 불러와서 데이터 프레임 생성
df1 = pd.read_csv(load_file)

# 구별 열을 인덱스로 설정. 
# inplace=True를 사용하여 원본 데이터에 영향을 줌.
df1.set_index('구별', inplace=True)

# CCTV 수(소계)로 오름차순 정렬.
# inplace=True를 사용하여 원본 데이터에 영향을 줌.
df1.sort_values(by='소계', ascending=False, inplace=True)

# df컬럼명 "CCTV비율"에 "소계 / 인구수 * 100"로 value를 넣어 대입함.
df1['CCTV비율'] = df1['소계'] / df1['인구수'] * 100

# CCTV비율로 오름차순 정렬.
# inplace=True를 사용하여 원본 데이터에 영향을 줌.
df1.sort_values(by='CCTV비율', ascending=False, inplace=True)

# # CCTV비율로 오름차순 정렬한 데이터 프레임의 인덱스를 "cctv_ratio_top"변수에 대입함
cctv_ratio_top = df1.sort_values(by='CCTV비율', ascending=False).index

# print("CCTV가 가장 많은 구의 순서대로:", pd.DataFrame(cctv_ratio_top))










