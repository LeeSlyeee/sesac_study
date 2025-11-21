import korean as ko # 임포트 korean
import pandas as pd # 임포트 pandas
import matplotlib as mpl # 임포트 matplotlib
import matplotlib.pyplot as plt # 임포트 matplotlib.pyplot
import numpy as np # 임포트 numpy

ko.korean_setup() # 한글 설정 함수 호출



gender_no_time = [55.2, 45]
gender_no_with = [7.9, 8.3]
gender_no_place = [5.5, 6]
gender_hate_health = [29.8, 38.8]


# 4분면 파이 그래프를 위한 데이터 및 설정
labels = ['남성', '여성'] # 각 파이 조각에 대한 라벨

# 전체 그래프(figure)의 크기를 설정합니다.
plt.figure(figsize=(10, 10))

# 1. 좌상단 그래프 (운동할 시간이 없어서)
plt.subplot(2, 2, 1)
df_no_time = pd.Series(gender_no_time, index=labels)
df_no_time.plot.pie(autopct='%.1f%%', startangle=90, counterclock=False)
plt.title('운동할 충분한 시간이 없어서')
plt.ylabel('') # 불필요한 y축 라벨 제거

# 2. 우상단 그래프 (함께 운동할 사람이 없어서)
plt.subplot(2, 2, 2)
df_no_with = pd.Series(gender_no_with, index=labels)
df_no_with.plot.pie(autopct='%.1f%%', startangle=90, counterclock=False)
plt.title('함께 운동할 사람이 없어서')
plt.ylabel('')

# 3. 좌하단 그래프 (운동을 싫어해서)
plt.subplot(2, 2, 3)
df_hate_health = pd.Series(gender_hate_health, index=labels)
df_hate_health.plot.pie(autopct='%.1f%%', startangle=90, counterclock=False)
plt.title('운동을 싫어해서')
plt.ylabel('')

# 4. 우하단 그래프 (운동할 장소가 없어서)
plt.subplot(2, 2, 4)
df_no_place = pd.Series(gender_no_place, index=labels)
df_no_place.plot.pie(autopct='%.1f%%', startangle=90, counterclock=False)
plt.title('운동할 장소가 없어서')
plt.ylabel('')

# 그래프들이 겹치지 않도록 레이아웃을 자동 조정합니다.
plt.tight_layout()

# 그래프를 화면에 표시합니다.
plt.show()
