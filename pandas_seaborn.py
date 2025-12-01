import matplotlib.pyplot as plt
import matplotlib as mpl
import korean
import pandas as pd
import numpy as np
import seaborn as sns 
import folium






# x = np.linspace(1,14,100)
# # NumPy의 linspace 함수를 사용하여 x축 데이터 배열을 생성합니다.
# # 시작: 1, 끝: 14, 개수: 100개
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 배열을 만듭니다.
# print(x) # 생성된 x 배열의 내용을 콘솔에 출력합니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터 (sin(x))
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터 (2 * sin(x))
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터 (3 * sin(x))
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터 (4 * sin(x))

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 가로 10인치, 세로 6인치로 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 선 그래프를 그립니다.
# # 인수는 (x1, y1, x2, y2, x3, y3, x4, y4) 순서로 나열됩니다.
# # 모든 곡선은 동일한 x 배열을 공유하며, 진폭(y 값의 범위)만 다릅니다.

# plt.show() # 생성된 네 개의 사인 곡선 그래프를 화면에 표시합니다.








# x = np.linspace(1,14,100)
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 x축 데이터 배열을 생성합니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터

# sns.set_style('whitegrid')
# # Seaborn의 set_style 함수를 사용하여 Matplotlib의 기본 스타일을 변경합니다.
# # 'whitegrid' 스타일은 그래프 배경이 흰색이고, x축 및 y축에 밝은 격자(grid)가 표시되도록 설정합니다.

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 사인 곡선 그래프를 그립니다.
# # 인수는 (x1, y1, x2, y2, ...) 순서로 나열됩니다.

# plt.show() # 생성된 그래프를 화면에 표시합니다. (Seaborn 스타일이 적용됨)







# x = np.linspace(1,14,100)
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 x축 데이터 배열을 생성합니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터

# sns.set_style('darkgrid')
# # Seaborn의 set_style 함수를 사용하여 Matplotlib의 기본 스타일을 변경합니다.
# # 'darkgrid' 스타일은 그래프 배경이 회색이고, x축 및 y축에 밝은 격자(grid)가 표시되도록 설정합니다.

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 사인 곡선 그래프를 그립니다.
# # 인수는 (x1, y1, x2, y2, ...) 순서로 나열됩니다.

# plt.show() # 생성된 그래프를 화면에 표시합니다. (Seaborn 스타일이 적용됨)







# x = np.linspace(1,14,100)
# # NumPy의 linspace 함수를 사용하여 x축 데이터 배열을 생성합니다.
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 배열을 만듭니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터

# sns.set_style('whitegrid')
# # Seaborn의 set_style 함수를 사용하여 Matplotlib의 기본 스타일을 변경합니다.
# # 'whitegrid' 스타일은 그래프 배경을 흰색으로, 그리고 격자(grid)를 표시하도록 설정합니다.

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 사인 곡선 그래프를 하나의 Axes에 그립니다.
# # (x1, y1, x2, y2, ...) 순서로 인수가 나열되어 진폭만 다른 네 개의 곡선이 중첩됩니다.

# sns.despine(right=False, left=False)
# # Seaborn의 despine 함수를 사용하여 Axes 주변의 테두리(Spines)를 제어합니다.
# # right=False: 오른쪽 테두리를 "제거하지 않고" 유지합니다.
# # left=False: 왼쪽 테두리를 "제거하지 않고" 유지합니다.
# # (이 설정은 기본값으로 제거되는 오른쪽/위쪽 테두리를 유지하거나, 스타일 변경 후 축을 명시적으로 제어할 때 사용됩니다.)

# plt.show() # 생성된 그래프를 화면에 표시합니다.







# x = np.linspace(1,14,100)
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 x축 데이터 배열을 생성합니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터

# sns.set_context('talk')
# # Seaborn의 set_context 함수를 사용하여 Matplotlib의 기본 스타일을 변경합니다.
# # 'talk' 콘텍스트는 "프레젠테이션이나 발표 자료"에 적합하도록
# # "모든 텍스트 요소(제목, 축 레이블, 눈금 레이블 등)와 선 굵기"를 크게 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 사인 곡선 그래프를 그립니다.
# # 인수는 (x1, y1, x2, y2, ...) 순서로 나열되어 진폭만 다른 네 개의 곡선이 중첩됩니다.

# plt.show() # 생성된 그래프를 화면에 표시합니다. ('talk' 콘텍스트가 적용됨)








# x = np.linspace(1,14,100)
# # NumPy의 linspace 함수를 사용하여 x축 데이터 배열을 생성합니다.
# # 1부터 14까지의 범위를 100개의 균일한 간격으로 나눈 배열을 만듭니다.

# y1 = np.sin(x)    # 진폭 1을 가진 사인 곡선 데이터
# y2 = 2 * np.sin(x) # 진폭 2를 가진 사인 곡선 데이터
# y3 = 3 * np.sin(x) # 진폭 3을 가진 사인 곡선 데이터
# y4 = 4 * np.sin(x) # 진폭 4를 가진 사인 곡선 데이터

# sns.set_context('talk',font_scale=.5)
# # Seaborn의 set_context 함수를 사용하여 시각적 콘텍스트를 설정합니다.
# # 'talk': 프레젠테이션에 적합하도록 "모든 텍스트 요소와 선 굵기"를 기본보다 크게 설정합니다.
# # font_scale=.5: 'talk' 콘텍스트의 기본 글꼴 크기를 50% 수준으로 "축소"합니다.
# #               (즉, 기본 'notebook' 콘텍스트보다 작아질 수 있습니다.)

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# plt.plot(x, y1, x, y2, x, y3, x, y4)
# # plt.plot() 함수를 한 번 호출하여 네 개의 사인 곡선 그래프를 하나의 Axes에 그립니다.
# # 인수는 (x1, y1, x2, y2, ...) 순서로 나열되어 진폭만 다른 네 개의 곡선이 중첩됩니다.

# plt.show() # 생성된 그래프를 화면에 표시합니다.







# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# print(tips.head(5)) # DataFrame의 첫 5개 행을 콘솔에 출력하여 데이터 구조를 확인합니다.

# # --- 히스토그램 (Histogram) ---
# sns.histplot(x=tips['total_bill'])
# # total_bill 열의 분포를 "히스토그램"으로 그립니다.
# # 히스토그램은 데이터를 여러 구간(bins)으로 나누고 각 구간의 빈도수를 막대로 표시합니다.
# # 이 호출은 첫 번째 Figure를 생성합니다.

# plt.show() # 첫 번째 Figure (히스토그램)를 화면에 표시하고 "닫습니다".
#            # 이후의 그래프는 새로운 Figure에 그려집니다.

# # --- 커널 밀도 추정 (KDE) ---
# sns.kdeplot(x=tips['total_bill'])
# # total_bill 열의 분포를 "커널 밀도 추정 곡선"으로 그립니다.
# # KDE는 데이터 분포를 나타내는 부드러운 곡선을 추정합니다.
# # 이 호출은 두 번째 Figure를 생성합니다.

# plt.show() # 두 번째 Figure (KDE 곡선)를 화면에 표시하고 "닫습니다".





# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.

# sns.set_style('whitegrid')
# # Seaborn의 set_style 함수를 사용하여 그래프 배경을 흰색으로, 그리고 격자(grid)를 표시하도록 설정합니다.
# # (박스 플롯은 수직축에 데이터 값이 표시되므로 수평 격자선이 유용합니다.)

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# sns.boxplot(x = tips['total_bill'])
# # total_bill 열의 분포를 박스 플롯으로 그립니다.
# # x 인수에 데이터를 전달하면 수평(가로) 박스 플롯이 생성됩니다.

# sns.despine()
# # Axes 주변의 테두리(Spines)를 제어합니다.
# # 인수를 지정하지 않으면 기본적으로 위쪽(top)과 오른쪽(right) 테두리를 제거합니다.
# # (박스 플롯은 이미 깔끔한 형태이므로 시각적으로 불필요한 테두리를 없애줍니다.)

# plt.show() # 생성된 박스 플롯 그래프를 화면에 표시합니다.









# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('whitegrid')
# # Seaborn의 set_style 함수를 사용하여 그래프 배경을 흰색으로, 그리고 격자(grid)를 표시하도록 설정합니다.

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# sns.boxplot(x=tips['day'], y=tips['total_bill'])
# # 두 변수를 사용하여 박스 플롯을 그립니다.
# # x=tips['day']: X축에 범주형 변수('day': Thur, Fri, Sat, Sun)를 설정합니다.
# # y=tips['total_bill']: Y축에 수치형 변수('total_bill')를 설정합니다.
# # 이는 요일별로 total_bill의 "분포"를 나타내는 4개의 박스 플롯을 생성합니다.

# sns.despine(offset=10)
# # Axes 주변의 테두리(Spines)를 제어합니다.
# # 인수를 지정하지 않으면 기본적으로 위쪽(top)과 오른쪽(right) 테두리를 제거합니다.
# # offset=10: 축 눈금(ticks)이 축 테두리에서 10 포인트 "떨어져서" 표시되도록 설정합니다.

# plt.show() # 생성된 박스 플롯 그래프를 화면에 표시합니다.







# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('whitegrid')
# # Seaborn의 set_style 함수를 사용하여 그래프 배경을 흰색으로, 그리고 격자(grid)를 표시하도록 설정합니다.

# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# sns.boxplot(x='day', y='total_bill', data=tips, palette='Set2')
# # 두 변수를 사용하여 박스 플롯을 그립니다.
# # x='day': X축에 범주형 변수(요일)를 설정합니다.
# # y='total_bill': Y축에 수치형 변수(총 금액)를 설정합니다.
# # data=tips: 사용할 데이터프레임을 지정합니다. (x와 y 인수에 열 이름만 사용 가능하게 함)
# # palette='Set2': 박스 플롯의 색상을 Matplotlib/Seaborn의 'Set2' 색상 팔레트에서 가져와 설정합니다.
# #                 이는 각 요일별 박스의 색상을 다르게 지정하여 구분을 용이하게 합니다.

# sns.despine(offset=10)
# # Axes 주변의 테두리(Spines)를 제어합니다.
# # 인수를 지정하지 않으면 기본적으로 위쪽(top)과 오른쪽(right) 테두리를 제거합니다.
# # offset=10: 축 눈금(ticks)이 축 테두리에서 10 포인트 "떨어져서" 표시되도록 설정합니다.

# plt.show() # 생성된 박스 플롯 그래프를 화면에 표시합니다.






# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.
                                
# plt.figure(figsize=(10,6)) # 새로운 그림(Figure) 객체를 생성하고, 크기를 설정합니다.

# sns.boxplot(x='day', y='tip', hue='smoker', data=tips, palette='Set3')
# # 세 변수를 사용하여 그룹화된 박스 플롯을 그립니다.
# # x='day': X축에 "주요 범주형 변수"(요일)를 설정합니다.
# # y='tip': Y축에 "수치형 변수"(팁 금액)를 설정합니다. 각 요일별 팁의 분포를 보여줍니다.
# # hue='smoker': 'smoker' 변수를 "추가적인 그룹화 변수"로 설정합니다.
# #             각 요일(day) 카테고리 내에서 흡연(Yes) 그룹과 비흡연(No) 그룹의 박스 플롯을 나란히 표시합니다.
# # data=tips: 사용할 데이터프레임을 지정합니다.
# # palette='Set3': 박스 플롯의 색상을 Matplotlib/Seaborn의 'Set3' 색상 팔레트에서 가져와 설정합니다.

# plt.show() # 생성된 그룹화된 박스 플롯 그래프를 화면에 표시합니다.







# tips = sns.load_dataset('tips') # Seaborn 내장 'tips' 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "boxplot" 함수를 사용하여 상자 수염 그림(Box Plot)을 생성합니다.
# # Box Plot은 데이터의 분포와 이상치(outliers)를 확인하는 데 유용합니다. 

# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='total_bill',        # y축 변수로 "total_bill"(총 계산 금액, 수치형)을 지정합니다.
#             hue='sex',             # "sex"(성별, 범주형) 변수를 기준으로 박스 플롯을 분리(색상으로 구분)하여 그립니다.
#             data=tips,             # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             palette='Set3'         # 박스 플롯에 사용될 색상 팔레트를 "Set3"로 지정합니다.
#            )
# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.









# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.
                               
# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "boxplot" 함수를 사용하여 상자 수염 그림(Box Plot)을 생성합니다.
# # Box Plot은 데이터의 분포와 이상치(outliers)를 확인하는 데 유용합니다. 

# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='tip',             # y축 변수로 "tip"(팁 금액, 수치형)을 지정합니다.
#             data=tips,           # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             palette='Set3'       # 박스 플롯에 사용될 색상 팔레트를 "Set3"로 지정합니다.
#            )
# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.













# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.
                               
# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "boxplot" 함수를 사용하여 상자 수염 그림(Box Plot)을 생성합니다.
# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='tip',             # y축 변수로 "tip"(팁 금액, 수치형)을 지정합니다.
#             hue='sex',           # "sex"(성별, 범주형) 변수를 기준으로 박스 플롯을 분리(색상으로 구분)하여 그립니다.
#                                  # 이로써 요일별 팁 분포를 남성과 여성 그룹으로 나누어 비교할 수 있습니다.
#             data=tips,           # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             palette='Set3'       # 박스 플롯에 사용될 색상 팔레트를 "Set3"로 지정합니다.
#            )
# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.







# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.
                               
# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "boxplot" 함수를 사용하여 상자 수염 그림(Box Plot)을 생성합니다.
# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='tip',             # y축 변수로 "tip"(팁 금액, 수치형)을 지정합니다.
#             hue='sex',           # "sex"(성별, 범주형) 변수를 기준으로 박스 플롯을 분리(색상으로 구분)하여 그립니다.
#                                  # 이로써 요일별 팁 분포를 남성과 여성 그룹으로 나누어 비교할 수 있습니다.
#             data=tips,           # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             palette='husl'       # 박스 플롯에 사용될 색상 팔레트를 "husl"로 지정합니다. ("Set3" 대신 "husl" 사용)
#            )
# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.












# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "boxplot" 함수를 사용하여 상자 수염 그림(Box Plot)을 생성합니다.
# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='total_bill',      # y축 변수로 "total_bill"(총 계산 금액, 수치형)을 지정합니다.
#             hue='sex',           # "sex"(성별, 범주형) 변수를 기준으로 박스 플롯을 분리(색상으로 구분)하여 그립니다.
#                                  # 이로써 요일별 총 계산 금액 분포를 남성과 여성 그룹으로 나누어 비교할 수 있습니다.
#             data=tips,           # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             palette='Set3'       # 박스 플롯에 사용될 색상 팔레트를 "Set3"로 지정합니다.
#            )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.











# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # "swarmplot" 함수를 사용하여 스웜 플롯(Swarm Plot)을 생성합니다.
# sns.swarmplot(x='day',           # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#               y='total_bill',    # y축 변수로 "total_bill"(총 계산 금액, 수치형)을 지정합니다.
#               data=tips,         # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#               palette='husl'     # 스웜 플롯에 사용될 색상 팔레트를 "husl"로 지정합니다.
#              )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.













# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정하여 시각화 결과가 더 잘 보이도록 합니다.

# # 첫 번째 그래프: 상자 수염 그림(Box Plot)을 생성합니다.
# sns.boxplot(x='day',             # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#             y='total_bill',      # y축 변수로 "total_bill"(총 계산 금액, 수치형)을 지정합니다.
#             data=tips,           # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#             # 박스 플롯에 색상을 지정하지 않아 기본값(연한 색)으로 그려져 아래의 스웜 플롯과 잘 어우러지도록 합니다.
#            )

# # 두 번째 그래프: 스웜 플롯(Swarm Plot)을 첫 번째 그래프 위에 겹쳐서 생성합니다.
# # Box Plot의 분포 위에 개별 데이터 포인트를 표시하여 정확한 분포 형태와 데이터 밀집도를 보여줍니다.
# sns.swarmplot(x='day',           # x축 변수로 "day"(요일, 범주형)를 지정합니다.
#               y='total_bill',    # y축 변수로 "total_bill"(총 계산 금액, 수치형)을 지정합니다.
#               data=tips,         # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#               palette='husl'     # 스웜 플롯에 사용될 색상 팔레트를 "husl"로 지정합니다. (점들의 색상)
#              )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.








# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 회귀선(Regression Line)이 포함된 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            height=5        # 그래프의 높이(Height)를 5인치로 설정합니다. (너비는 자동으로 조정됨)
#           ) #

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.












# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            fit_reg=False,  # "fit_reg=False"는 핵심 설정으로, 선형 회귀선(Linear Regression Line)을 그리지 않도록 지정합니다.
#                            # 따라서 이 함수는 회귀선 없이 순수한 산점도만 생성합니다.
#            height=5        # 그래프의 높이(Height)를 5인치로 설정합니다.
#           ) 

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.













# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 선형 회귀선이 포함된 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            hue='smoker',   # "smoker"(흡연 여부) 변수를 기준으로 데이터를 두 그룹(Yes/No)으로 나누고,
#                            # 각 그룹별로 다른 색상과 별도의 회귀선을 그려 관계를 비교합니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            height=5        # 그래프의 높이(Height)를 5인치로 설정합니다.
#           )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.











# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 선형 회귀선이 포함된 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            hue='sex',      # "sex"(성별) 변수를 기준으로 데이터를 두 그룹(Male/Female)으로 나누고,
#                            # 각 그룹별로 다른 색상과 별도의 회귀선을 그려 관계를 비교합니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            height=5        # 그래프의 높이(Height)를 5인치로 설정합니다.
#           )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.











# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 선형 회귀선이 포함된 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            col='sex',      # 핵심 옵션: "sex"(성별) 변수의 범주(Male/Female)를 기준으로 그래프를 
#                            # 가로 방향으로 나열된 두 개의 "컬럼(패널)"로 분리하여 그립니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            height=5        # 각 패널(그래프)의 높이(Height)를 5인치로 설정합니다.
#           )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.









# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# sns.set_style('darkgrid') # 그래프의 배경 스타일을 "darkgrid"로 설정합니다. 
#                           # 이 스타일은 어두운 배경에 흰색 격자(grid)를 표시하여 데이터 포인트를 돋보이게 합니다.

# # "lmplot" 함수를 사용하여 선형 회귀선이 포함된 산점도(Scatter Plot)를 생성합니다.
# sns.lmplot(x='total_bill', # x축 변수로 "total_bill"(총 계산 금액)을 지정합니다.
#            y='tip',        # y축 변수로 "tip"(팁 금액)을 지정합니다.
#            col='smoker',   # 핵심 옵션: "smoker"(흡연 여부) 변수의 범주(Yes/No)를 기준으로 그래프를 
#                            # 가로 방향으로 나열된 두 개의 "컬럼(패널)"로 분리하여 그립니다.
#            data=tips,      # 시각화에 사용할 데이터프레임으로 "tips"를 지정합니다.
#            height=5        # 각 패널(그래프)의 높이(Height)를 5인치로 설정합니다.
#           )

# plt.show() # 생성된 시각화 결과(그래프)를 화면에 출력합니다.










# # "uniform_data" 변수에 (10, 12) 크기의 2차원 배열을 생성합니다.
# # np.random.rand(10, 12)는 0과 1 사이의 균일 분포에서 10행 12열의 난수를 생성합니다.
# uniform_data = np.random.rand(10,12) 

# print(uniform_data) # 생성된 난수 배열의 내용을 콘솔에 출력합니다.

# # "heatmap" 함수를 사용하여 히트맵을 생성합니다.
# # 히트맵은 데이터의 행렬 값을 색상의 강도로 표현하여 패턴을 시각적으로 파악하기 쉽게 만듭니다. 

# sns.heatmap(uniform_data, # 시각화할 2차원 데이터("uniform_data")를 지정합니다.
#             vmin=0,         # 색상 막대(Color Bar)의 최소값(Minimum value)을 0으로 설정합니다.
#             vmax=1          # 색상 막대의 최대값(Maximum value)을 1로 설정합니다.
#             # 난수 데이터의 범위(0~1)와 동일하게 설정하여 색상 대비를 명확하게 합니다.
#            )

# plt.show() # 생성된 히트맵을 화면에 출력합니다.









# tips = sns.load_dataset('tips') # Seaborn 내장 "tips" 데이터셋을 불러와 DataFrame 변수 tips에 저장합니다.
#                                 # 이 데이터셋은 식당 팁 관련 정보를 포함하고 있습니다.

# # tips DataFrame에서 수치형 컬럼들(total_bill, tip, size)만 선택하여 상관 관계 행렬을 계산합니다.
# # "numeric_only=True" 옵션은 오직 수치형 데이터만을 사용하여 상관 관계를 계산하도록 지정합니다.
# correlation_matrix = tips.corr(numeric_only=True)

# # 계산된 상관 관계 행렬을 콘솔에 출력합니다. (이 부분은 시각화 전에 데이터 확인용으로 추가될 수 있습니다.)
# print(correlation_matrix)

# # "heatmap" 함수를 사용하여 상관 관계 행렬을 히트맵으로 시각화합니다.
# sns.heatmap(correlation_matrix, # 시각화할 데이터로 상관 관계 행렬을 지정합니다.
#             annot=True,         # 핵심 옵션: "annot=True"는 각 셀에 계산된 "상관 계수" 값을 숫자로 표시하도록 합니다.
#             cmap='viridis'      # 색상 팔레트를 "viridis"로 지정합니다. 이는 값이 커질수록 밝고 대비가 뚜렷한 색상을 사용합니다.
#            )
# plt.show()












# flights = sns.load_dataset('flights') # Seaborn 내장 "flights" 데이터셋을 불러와 DataFrame 변수 flights에 저장합니다.
#                                       # 이 데이터셋은 1949년부터 1960년까지의 월별 항공기 승객 수를 포함하고 있습니다.

# print(flights.head()) # 데이터프레임의 첫 5개 행을 출력하여 데이터 구조를 확인합니다.
# print(flights.tail()) # 데이터프레임의 마지막 5개 행을 출력하여 데이터 구조를 확인합니다.

# # pd.pivot_table 함수를 사용하여 데이터를 피벗팅(재구조화)합니다.
# flight_p = pd.pivot_table(
#     flights,
#     index='month',      # 행(Row, Y축)으로 'month'(월)을 지정합니다.
#     columns = 'year',   # 열(Column, X축)으로 'year'(연도)를 지정합니다.
#     values='passengers',# 집계할 값(Cell 값)으로 'passengers'(승객 수)를 지정합니다.
#     fill_value=0        # 값이 없는 셀(결측치)을 0으로 채웁니다. (이 데이터셋에서는 결측치가 없을 가능성이 높음)
# )

# print(flight_p) # 피벗 테이블 결과를 출력합니다. (1월부터 12월까지 행, 1949년부터 1960년까지 열)

# plt.figure(figsize=(10,6)) # 그림(figure)의 크기를 가로 10인치, 세로 6인치로 설정합니다.

# # "heatmap" 함수를 사용하여 피벗 테이블(flight_p)을 시각화합니다.
# # 행(월)과 열(연도)에 따른 승객 수를 색상 강도로 표현하여 시간 경과에 따른 승객 수 변화 패턴을 보여줍니다.
# sns.heatmap(flight_p) # 

# plt.title('연도/월별 승객수') # 그래프의 제목을 설정합니다.
# plt.show() # 생성된 히트맵을 화면에 출력합니다.







# flights = sns.load_dataset('flights') # Seaborn 내장 "flights" 데이터셋을 불러와 DataFrame 변수 flights에 저장합니다.
#                                       # 이 데이터셋은 1949년부터 1960년까지의 월별 항공기 승객 수를 포함하고 있습니다.

# # pd.pivot_table 함수를 사용하여 데이터를 재구조화(피벗팅)하여 2차원 테이블을 만듭니다.
# flight_p = pd.pivot_table(
#     flights,
#     index='month',      # 행(Row, Y축)으로 'month'(월)을 지정합니다.
#     columns = 'year',   # 열(Column, X축)으로 'year'(연도)를 지정합니다.
#     values='passengers',# 셀(Cell)에 들어갈 값으로 'passengers'(승객 수)를 지정합니다.
#     fill_value=0        # 값이 없는 셀(결측치)을 0으로 채웁니다.
# )

# # print(flight_p) # 피벗 테이블 결과를 출력합니다. (1월부터 12월까지 행, 1949년부터 1960년까지 열)
# flight_p = flight_p.astype(int) # 데이터 프레임의 실수를 정수로 변환 
# print(flight_p) # 데이터 프레임의 실수를 정수로 변환한 결과를 출력합니다.
# plt.figure(figsize=(20,18)) # 그림(figure)의 크기를 가로 20인치, 세로 18인치로 매우 크게 설정하여 상세 내용을 잘 보이도록 합니다.

# # "heatmap" 함수를 사용하여 피벗 테이블(flight_p)을 시각화합니다.
# sns.heatmap(flight_p,       # 시각화할 데이터로 피벗 테이블을 지정합니다.
#             annot=True,     # 핵심 옵션: "annot=True"는 각 셀에 실제 '승객 수' 값을 숫자로 표시하도록 합니다.
#             fmt='f'         # 표시되는 숫자(승객 수)의 포맷을 일반 실수형('f')으로 지정합니다. 정수형일 경우 10진수 ('d')로 표현 
#                             # int로 표현해도 될것이라 판단했는데 씨본 내부에서 처리가 int와 decimal을 다르게 구분하는것으로 판단 됨.
#            )


# plt.title('연도/월별 승객수') # 그래프의 제목을 설정합니다.
# plt.show() # 생성된 히트맵을 화면에 출력합니다.


