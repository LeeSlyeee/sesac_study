import matplotlib.pyplot as plt
import matplotlib as mpl
import korean
import pandas as pd
import numpy as np
import seaborn as sns 







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



























































































































































































































































































































































