import korean # 임포트 korean
import pandas as pd # 임포트 pandas
import matplotlib as mpl # 임포트 matplotlib
import matplotlib.pyplot as plt # 임포트 matplotlib.pyplot
import numpy as np # 임포트 numpy

korean.korean_setup() # 한글 설정 함수 호출

# data = [1, 2, 7, 4, 5] # 첫 번째 데이터
# plt.plot(data) # 첫 번째 그래프 그리기    

# plt.figure() # 새로운 그래프 창 열기

# data2 = [5, 4, -1, 2, 1] # 두 번째 데이터
# plt.plot(data2) # 두 번째 그래프 그리기

# plt.show() # 두 그래프 모두 표시하기

# x = np.arange(-4.5, 5, 0.5) # x 값 생성
# y = 2*x**2 # y 값 생성

# print([x,y]) # x, y 값 출력

# plt.plot(x, y) # 그래프 그리기
# plt.show()


# x = np.arange(-4.5, 5, 0.5) # x 값 생성
# y1 = 2*x**2 # 첫 번째 y 값 생성
# y2 = 5*x + 30 # 두 번째 y 값 생성
# y3 = 4*x**2 + 10 # 세 번째 y 값 생성

# plt.plot(x, y1) # 첫 번째 그래프 그리기   
# plt.plot(x, y2) # 두 번째 그래프 그리기   
# plt.plot(x, y3) # 세 번째 그래프 그리기
# plt.show()  


# plt.plot(x, y1, x, y2, x, y3)
# plt.show()

# plt.plot(x, y1) # 첫 번째 그래프 그리기
# plt.figure() # 새로운 그래프 창 열기
# plt.plot(x, y2) # 두 번째 그래프 그리기
# plt.show() # 새로운 그래프 창 열기


# x = np.arange(-5, 5, 0.1) # x 값 생성
# y1 = x**2 - 2 # 첫 번째 y 값 생성
# y2 = 20*np.cos(x)**2 # 두 번째 y 값 생성 / NumPy에서 cos()는 np.cos()으로 입력

# plt.figure(1) # 1번 그래프 창을 생성함
# plt.plot(x, y1) # 지정된 그래프 창에 그래프를 그림

# plt.figure(2) # 2번 그래프 창을 생성함
# plt.plot(x, y2) # 지정된 그래프 창에 그래프를 그림

# plt.figure(1) # 이미 생성된 1번 그래프 창을 지정함
# plt.plot(x, y2) # 지정된 그래프 창에 그래프를 그림

# plt.figure(2) # 이미 생성된 2번 그래프 창을 지정함
# plt.clf() # 2번 그래프 창에 그려진 모든 그래프를 지움
# plt.plot(x, y1) # 지정된 그래프 창에 그래프를 그림

# plt.show() # 모든 그래프 창을 화면에 표시함


# x = np.arange(0, 10, 0.1) # x 값 생성
# y1 = 0.3*(x-5)**2 + 1 # 첫 번째 y 값 생성
# y2 = -1.5*x + 3 # 두 번째 y 값 생성
# y3 = np.sin(x)**2 # NumPy에서 sin()은 np.sin()으로 입력
# y4 = 10*np.exp(-x) + 1 # NumPy에서 exp()는 np.exp()로 입력


# 2 × 2 행렬로 이뤄진 하위 그래프에서 p에 따라 위치를 지정
# plt.subplot(2,2,1) # p는 1 좌상단
# plt.plot(x,y1)

# plt.subplot(2,2,2) # p는 2 우상단
# plt.plot(x,y2)

# plt.subplot(2,2,3) # p는 3 좌하단
# plt.plot(x,y3)

# plt.subplot(2,2,4) # p는 4 우하단 
# plt.plot(x,y4)
# plt.show()



# x = np.linspace(-4, 4, 100) # [-4, 4] 범위에서 100개의 값 생성
# y1 = x**3
# y2 = 10*x**2 - 2
# plt.plot(x, y1, x, y2) # 그래프 그리기
# plt.show() # 그래프 표시하기


# plt.plot(x, y1, x, y2) # 그래프 그리기
# plt.xlim(-1, 1) # x축 범위 지정
# plt.ylim(-3, 3) # y축 범위 지정
# plt.show() # 그래프 표시하기



# x = np.arange(0, 5, 1) # x 값 생성
# y1 = x # 첫 번째 y 값 생성
# y2 = x + 1 # 두 번째 y 값 생성
# y3 = x + 2 # 세 번째 y 값 생성
# y4 = x + 3 # 네 번째 y 값 생성

# plt.plot(x, y1, x, y2, x, y3, x, y4) # 그래프 그리기
# plt.show() # 그래프 표시하기


# plt.plot(x, y1, 'm', x, y2,'y', x, y3, 'k', x, y4, 'c') # 그래프에 색상 지정하여 그리기
# plt.show() # 그래프 표시하기


# plt.plot(x, y1, '-', x, y2, '--', x, y3, ':', x, y4, '-.') # 그래프에 선 스타일 지정하여 그리기
# plt.show() # 그래프 표시하기

# plt.plot(x, y1, 'o', x, y2, '^',x, y3, 's', x, y4, 'd') # 그래프에 마커 스타일 지정하여 그리기
# plt.show() # 그래프 표시하기


# plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc') # 그래프에 색상, 선 스타일, 마커 스타일 지정하여 그리기
# plt.show() # 그래프 표시하기




# x = np.arange(-4.5, 5, 0.5)
# y = 2*x**3

# plt.plot(x,y) # 그래프 그리기
# plt.xlabel('X-axis') # x축 라벨 지정
# plt.ylabel('Y-axis') # y축 라벨 지정
# plt.title('Graph title') # 그래프 제목 지정
# plt.grid(True) # 격자무늬 표시
# plt.show() # 그래프 표시하기



# x = np.arange(0, 5, 1)
# y1 = x
# y2 = x + 1
# y3 = x + 2
# y4 = x + 3

# plt.plot(x, y1, '>--r', x, y2, 's-g', x, y3, 'd:b', x, y4, '-.Xc') # 그래프에 색상, 선 스타일, 마커 스타일 지정하여 그리기
# plt.legend(['데이터1', '데이터2', '데이터3', '데이터4'], loc = 'best') # 범례 위치 지정 (젤로 좋은 위치)
# plt.xlabel('X 축') # x축 라벨 지정
# plt.ylabel('Y 축') # y축 라벨 지정
# plt.title('그래프 제목') # 그래프 제목 지정
# plt.grid(True) # 격자무늬 표시
# plt.text(0, 6, "문자열 출력 1") # 그래프에 문자열 출력
# plt.text(0, 5, "문자열 출력 2") 
# plt.text(3, 1, "문자열 출력 3")
# plt.text(3, 0, "문자열 출력 4")
# plt.show() # 그래프 표시하기



# height = [165, 177, 160, 180, 185, 155, 172] # 키 데이터
# weight = [62, 67, 55, 74, 90, 43, 64] # 몸무게 데이터
# plt.scatter(height, weight) # 산점도 그래프 그리기
# plt.xlabel('Height(m)') # x축 라벨 지정
# plt.ylabel('Weight(Kg)') # y축 라벨 지정
# plt.title('Height & Weight') # 그래프 제목 지정
# plt.grid(True) # 격자무늬 표시
# plt.scatter(height, weight, s=500, c='r') # 마커 크기는 500, 컬러는 붉은색(red)
# size = 100 * np.arange(1,8) # 데이터별로 마커의 크기 지정
# colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 데이터별로 마커의 컬러 지정
# plt.scatter(height, weight, s=size, c=colors)
# plt.show()



# city = ['서울', '인천', '대전', '대구', '울산', '부산', '광주']
# # 위도(latitude)와 경도(longitude)
# lat = [37.56, 37.45, 36.35, 35.87, 35.53, 35.18, 35.16]
# lon = [126.97, 126.70, 127.38, 128.60, 129.31, 129.07, 126.85]
# # 인구 밀도(명/km^2): 2017년 통계청 자료
# pop_den = [16154, 2751, 2839, 2790, 1099, 4454, 2995]
# size = np.array(pop_den) * 0.2 # 마커의 크기 지정
# colors = ['r', 'g', 'b', 'c', 'm', 'k', 'y'] # 마커의 컬러 지정
# plt.scatter(lon, lat, s=size, c=colors, alpha=0.5) # alpha는 투명도
# plt.xlabel('경도(longitude)') # x축 라벨 지정
# plt.ylabel('위도(latitude)') # y축 라벨 지정
# plt.title('한국 주요 도시의 인구 밀도') # 그래프 제목 지정
# for x, y, name in zip(lon, lat, city): # 위도 경도와 도시 이름을 묶음
#     plt.text(x, y, name) # 위도 경도에 맞게 도시 이름 출력
# plt.show()





# member_IDs = ['m_01', 'm_02', 'm_03', 'm_04'] # 회원 ID
# before_ex = [27, 35, 40, 33] # 운동 시작 전
# after_ex = [30, 38, 42, 37] # 운동 한 달 후

# n_data = len(member_IDs) # 회원이 네 명이므로 전체 데이터 수는 4
# index = np.arange(n_data) # NumPy를 이용해 배열 생성 (0, 1, 2, 3)


# plt.bar(index, before_ex) # bar(x,y)에서 x=index, height=before_ex 로 지정
# plt.show()

# plt.bar(index, before_ex, tick_label = member_IDs) # 막대 그래프 그리기
# plt.show()

# colors=['r', 'g', 'b', 'm'] # 막대 그래프의 색상 지정
# plt.bar(index, before_ex, color = colors, tick_label = member_IDs) # 막대 그래프 그리기
# plt.show() 

# plt.bar(index, before_ex, tick_label = member_IDs, width = 0.6) # 막대 그래프 그리기
# plt.show()

# colors=['r', 'g', 'b', 'm']
# plt.barh(index, before_ex, color = colors, tick_label = member_IDs)
# plt.show()

# barWidth = 0.4  # 막대 너비 설정
# plt.bar(index, before_ex, color='c', align='edge', width = barWidth, label='before') # 첫 번째 막대 그래프
# plt.bar(index + barWidth, after_ex , color='m', align='edge', width = barWidth, label='after') # 두 번째 막대 그래프
# plt.xticks(index + barWidth, member_IDs) # x축 눈금 라벨 설정
# plt.legend() # 범례 표시
# plt.xlabel('회원 ID') # x축 라벨 지정
# plt.ylabel('윗몸일으키기 횟수') # y축 라벨 지정
# plt.title('운동 시작 전과 후의 근지구력(복근) 변화 비교') # 그래프 제목 지정
# plt.show()  




# temperature = [25.2, 27.4, 22.9, 26.2, 29.5, 33.1, 30.4, 36.1, 34.4, 29.1] # 기온 데이터
# Ice_cream_sales = [236500, 357500, 203500, 365200, 446600, 574200, 453200, 675400, 598400, 463100] # 아이스크림 판매량 데이터
# dict_data = {'기온':temperature, '아이스크림 판매량':Ice_cream_sales} # 딕셔너리 생성
# df_ice_cream = pd.DataFrame(dict_data, columns=['기온', '아이스크림 판매량']) # 데이터프레임 생성
# df_ice_cream.plot.scatter(x='기온', y='아이스크림 판매량', grid=True, title='최고') # 산점도 그래프 그리기
# plt.show()



# grade_num = [5, 14, 12, 3] # 학점 데이터
# students = ['A', 'B', 'C', 'D'] # 학생 이름 데이터
# df_grade = pd.DataFrame(grade_num, index=students, columns = ['Student']) # 데이터프레임 생성
# print(df_grade) # 데이터프레임 출력

# grade_bar = df_grade.plot.bar(grid = True) # 막대 그래프 그리기
# grade_bar.set_xlabel("학점") # x축 라벨 지정
# grade_bar.set_ylabel("학생수") # y축 라벨 지정
# grade_bar.set_title("학점별 학생 수 막대 그래프") # 그래프 제목 지정
# plt.show()



# math = [76,82,84,83,90,86,85,92,72,71,100,87,81,76,94,78,81,60,79,69,74,87,82,68,79] # 수학 시험 점수 데이터
# df_math = pd.DataFrame(math, columns = ['Student']) # 데이터프레임 생성
# math_hist = df_math.plot.hist(bins=16, grid = True) # 히스토그램 그리기
# math_hist.set_xlabel("시험 점수") # x축 라벨 지정
# math_hist.set_ylabel("도수(frequency)") # y축 라벨 지정
# math_hist.set_title("수학 시험의 히스토그램") # 그래프 제목 지정
# plt.show()




# fruit = ['사과', '바나나', '딸기', '오렌지', '포도'] # 과일 이름 리스트
# result = [7, 6, 3, 2, 2] # 선택한 학생 수 리스트
# df_fruit = pd.Series(result, index = fruit, name = '선택한 학생수') # 시리즈 생성
# print(df_fruit)

# df_fruit.plot.pie() # 
# plt.show()


# explode_value = (0.05, 0, 0, 0, 0) # 첫 번째 조각만 돌출
# fruit_pie = df_fruit.plot.pie(figsize=(5, 5), autopct='%.1f%%', startangle=20, counterclock = False, explode=explode_value, shadow=True, table=True) 
# fruit_pie.set_ylabel("") # 불필요한 y축 라벨 제거
# fruit_pie.set_title("과일 선호도 조사 결과") 
# plt.savefig('saveFigTest3.png', dpi = 200) # 그래프를 이미지 파일로 저장. dpi는 200으로 설정
# plt.show()




