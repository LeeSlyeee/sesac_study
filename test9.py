import numpy as np # numpy 불러오기

# data1 = [0, 1, 2, 3, 4, 5] # 1차원 리스트
# data2 = [0.1, 5, 4, 12 , 0.5] # 1차원 리스트
# data3 = [[1,2,3],[4,5,6],[7,8,9]] # 2차원 리스트(리스트 안에 리스트)


# a1 = np.array(data1) # 1차원 배열 생성
# a2 = np.array(data2) # 1차원 배열 생성
# a3 = np.array(data3)  # 2차원 배열 생성

# print(a1)
# print(a2)
# print(a3)


# print(np.arange(1,10).reshape(3,3)) # 1~9까지 1차원 배열 생성 후 3X3 2차원 배열로 변환

# t = np.array(data3) # 2차원 배열 생성

# print(t.shape) # 배열의 형태 출력

# print(type(t)) # 배열의 자료형 출력    

# t.shape = (9,) # 배열의 형태 변경 



# b2 = np.arange(6) # 0~5까지 1차원 배열 생성

# print(b2.reshape(3,2)) # 3X2 2차원 배열로 변환 후 출력



# print(np.linspace(1, 10, 10).dtype) # 1~10까지 균등 간격으로 10개 생성 후 자료형 출력




import pandas as pd # pandas 불러오기

# s1 = pd.Series([10,20,30,40,50]) # 시리즈 생성

# print(s1.index) # 시리즈의 인덱스 출력


# s2 = pd.Series(['a','b','c',1,2,3]) # 시리즈 생성
# print(s2) # 시리즈 출력   

# s3 = pd.Series([np.nan,10,30]) # 시리즈 생성    

# print(s3) # 시리즈 출력

# index_date = ["2025-08-07", "2025-08-08", "2025-08-09", "2025-08-10"] # 인덱스 생성
# s4 = pd.Series([200,195,np.nan,205], index= index_date) # 시리즈 생성

# print(s4) # 시리즈 출력

# s5 = pd.Series({"국어": 100, "영어": 95, "수학": 90}) # 시리즈 생성
# print(s5) # 시리즈 출력

# print(pd.date_range(start="2025.01.01", end="2025.01.07")) # 날짜 범위 생성

# print(pd.date_range(start="2025.01.01", periods = 12, freq="2bme")) # 2개월 간격의 영업일 기준 날짜 범위 생성

# print(pd.date_range(start="2025.01.01", periods = 4, freq="QS")) # 분기 시작일 기준 날짜 범위 생성

# print(pd.date_range(start="2025.01.01", periods = 3, freq="YS")) # 연도 시작일 기준 날짜 범위 생성

# print(pd.date_range(start="2025.01.01 08:00", periods = 10, freq="h")) # 시간 단위 날짜 범위 생성

# print(pd.date_range(start="2025.01.01 08:00", periods = 10, freq="bh")) # 영업시간 단위 날짜 범위 생성

# print(pd.date_range(start="2025.01.01 08:00", periods = 4, freq="30min")) # 30분 단위 날짜 범위 생성

# print(pd.date_range(start="2025.01.01 10:00:00", periods = 4, freq="10s")) # 10초 단위 날짜 범위 생성


# index_date = pd.date_range(start="2025.03.01", periods = 5, freq="d") # 날짜 범위 생성
# print(pd.Series([51,62,55,49,58], index=index_date)) # 시리즈 생성 및 출력


# print(pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])) # 데이터프레임 생성 및 출력


# data = np.array([[1,2,3], [4,5,6], [7,8,9], [10,11,12]]) # 2차원 배열 생성 
# index_date = pd.date_range("2019-09-01", periods=4) # 인덱스 생성
# columns_list = ["A", "B", "C"] # 열 이름 생성
# print(pd.DataFrame(data, index=index_date, columns=columns_list)) # 데이터프레임 생성 및 출력


# table_data = {
#     "연도": [2015,2016,2016,2017,2017],
#     "지사": ["한국","한국","미국","한국","미국"],
#     "고객 수": [200,250,450,300,500]
# } # 딕셔너리 생성
# print(pd.DataFrame(table_data))
# print(pd.DataFrame(table_data, columns=["연도","지사","고객 수"]))
# print(pd.DataFrame(table_data, columns=["지사", "연도", "고객 수"]))

# print(pd.DataFrame(table_data, columns=["연도","지사","고객 수"]).index)
# print(pd.DataFrame(table_data, columns=["연도","지사","고객 수"]).columns)
# print(pd.DataFrame(table_data, columns=["연도","지사","고객 수"]).values)




# arr1 = np.array([1,2,3]) # 1차원 배열 생성
# arr2 = np.array([4,5,6]) # 1차원 배열 생성
# arr3 = np.array([7,8,9]) # 1차원 배열 생성

# data_list = [arr1, arr2, arr3] # 리스트 생성

# print(pd.DataFrame(data_list)) # 데이터프레임 생성 및 출력





# s1 = pd.Series([1,2,3,4,5]) # 시리즈 생성
# s2 = pd.Series([10,20,30,40,50]) # 시리즈 생성

# print(s1+s2) # 시리즈 덧셈
# print(s2-s1) # 시리즈 뺄셈
# print(s1*s2) # 시리즈 곱셈
# print(s2/s1) # 시리즈 나눗셈

# s3 = pd.Series([1,2,3,4]) # 시리즈 생성
# s4 = pd.Series([10,20,30,40,50]) # 시리즈 생성

# print(s3+s4)  # 시리즈 덧셈
# print(s4-s3)  # 시리즈 뺄셈
# print(s3*s4)  # 시리즈 곱셈
# print(s4/s3)  # 시리즈 나눗셈




# table_data1 = {
#     "A": [1,2,3,4,5],
#     "B": [10,20,30,40,50],
#     "C": [100,200,300,400,500]
# } # 딕셔너리 생성

# df1 = pd.DataFrame(table_data1) # 데이터프레임 생성
# print(df1) # 데이터프레임 출력






# table_data2 = {
#     "A": [6,7,8],
#     "B": [60,70,80],
#     "C": [600,700,800]
# } # 딕셔너리 생성

# df2 = pd.DataFrame(table_data2) # 데이터프레임 생성
# print(df2) # 데이터프레임 출력

# print(df1+df2) # 데이터프레임 덧셈









# table_data3 = {
#     '봄':  [256.5, 264.3, 215.9, 223.2, 312.8],
#     '여름': [770.6, 567.5, 599.8, 387.1, 446.2],
#     '가을': [363.5, 231.2, 293.1, 247.7, 381.6],
#     '겨울': [139.3, 59.9, 76.9, 109.1, 108.1]
# }   # 온도 데이터
# columns_list = ['봄', '여름', '가을', '겨울'] # 열 이름
# index_list = ['2012', '2013', '2014', '2015', '2016'] # 행 인덱스

# df3 = pd.DataFrame(table_data3, columns = columns_list, index = index_list) # 계절별 강수량 데이터프레임 생성
# print(df3) # 전체 데이터 출력
# print(df3.mean()) # 열 방향 평균값 출력
# print(df3.std())  # 열 방향 표준편차 출력
# print(df3.mean(axis=1)) # 행 방향 평균값 출력
# print(df3.std(axis=1)) # 행 방향 표준편차 출력
# print(df3.describe()) # 기술 통계량 출력






# KTX_data = {'경부선 KTX': [39060, 39896, 42005, 43621, 41702, 41266, 32427],
#             '호남선 KTX': [7313, 6967, 6873, 6626, 8675, 10622, 9228],
#             '경전선 KTX': [3627, 4168, 4088, 4424, 4606, 4984, 5570],
#             '전라선 KTX': [309, 1771, 1954, 2244, 3146, 3945, 5766],
#             '동해선 KTX': [np.nan, np.nan, np.nan, np.nan, 2395, 3786, 6667]} # 승차 인원 데이터
# col_list = ['경부선 KTX','호남선 KTX','경전선 KTX','전라선 KTX','동해선 KTX'] # 열 이름
# index_list = ['2011', '2012', '2013', '2014', '2015', '2016', '2017'] # 행 인덱스

# df_KTX = pd.DataFrame(KTX_data, columns = col_list, index = index_list) # KTX 승차 인원 데이터프레임 생성


# print(df_KTX) #전체 데이터 출력
# print(df_KTX.index) # 행 인덱스 출력
# print(df_KTX.columns) # 열 이름 출력
# print(df_KTX.values) # 데이터 값 출력
# print(df_KTX.head(3)) # 처음 3행 출력
# print(df_KTX.tail(3)) # 마지막 3행 출력
# print(df_KTX[0:3]) # 처음 3행 출력

# 2011년 데이터 출력
# 시리즈로 출력됨
# print(df_KTX.loc['2011']) 


# 2011년과 2016년의 경전선 KTX 승차 인원 출력 데이터 프레임으로 출력 
# 시리즈가 아닌 데이터프레임으로 출력하려면 2중 대괄호 사용
# print(df_KTX.loc[['2011'],["경전선 KTX"]]) 


# print(df_KTX.loc['2013':'2016']) # 2013년부터 2016년까지의 행 데이터 출력
# print(df_KTX['호남선 KTX']) # 호남선 KTX 열 데이터 출력
# print(df_KTX['경부선 KTX'][2:5]) # 경부선 KTX 열의 2013년부터 2015년까지의 행 데이터 출력

# print(df_KTX.loc['2016']['호남선 KTX']) # 2016년 호남선 KTX 승차 인원 출력
# print(df_KTX.loc['2016', '호남선 KTX']) # 2016년 호남선 KTX 승차 인원 출력
# print(df_KTX['2016']['호남선 KTX']) # 2016년 호남선 KTX 승차 인원 출력
# print(df_KTX['호남선 KTX'][5]) # 2016년 호남선 KTX 승차 인원 출력
# print(df_KTX.T) # 행과 열을 바꾼 데이터프레임 출력
# print(df_KTX[['호남선 KTX','경부선 KTX','경전선 KTX','동해선 KTX','전라선 KTX']]) # 선택한 열들로 구성된 데이터프레임 출력



# 데이터프레임 행 또는 열 추가/삭제
# df_KTX['신규노선 KTX'] = [1000,2000,3000,4000,5000,6000,7000] # 신규 열 추가
# print(df_KTX)         



# del df_KTX['신규노선 KTX'] # 열 삭제
# print(df_KTX) # 열 삭제 후 출력



# 행 추가
# df_KTX.loc['2018'] = [45000, 12000, 6000, 7000, 8000, 9000] # 2018년 행 추가
# print(df_KTX) # 행 추가 후 출력   



# 행 삭제
# df_KTX = df_KTX.drop('2018') # 2018년 행      
# print(df_KTX) # 행 삭제 후 출력


# 데이터프레임 append() 메서드 이용 행 추가
# 추가할 행 데이터프레임 생성
# new_row = pd.DataFrame({'경부선 KTX': [46000], '호남선 KTX': [13000], '경전선 KTX': [7000], '전라선 KTX': [8000], '동해선 KTX': [9000]}, index=['2019'])
# new_df_KTX = pd.concat([df_KTX, new_row]) # concate() 메서드로 행 추가
# print(new_df_KTX) # 행 추가 후 출력   


# 데이터프레임 병합 
# 병합은 행 방향으로 합치는 것
# dfA = pd.DataFrame({'key': ['A', 'B', 'C'], 'value1': [1, 2, 3]}) # 데이터프레임 생성
# dfB = pd.DataFrame({'key': ['A', 'B', 'D'], 'value2': [4, 5, 6]}) # 데이터프레임 생성
# print(pd.concat([dfA, dfB], axis=0)) # 행 방향 병합
# print(pd.concat([dfA, dfB], axis=1)) # 열 방향 병합





# 조인은 데이터프레임끼리 합치는 것
# df1 = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'value1': [1, 2, 3, 4]})
# df2 = pd.DataFrame({'key': ['B', 'C', 'D', 'E'], 'value2': [5, 6, 7, 8]})      
# print(pd.merge(df1, df2, on='key', how='inner')) # 내부 조인
# print(pd.merge(df1, df2, on='key', how='outer')) # 외부 조인
# print(pd.merge(df1, df2, on='key', how='left')) # 왼쪽 외부 조인
# print(pd.merge(df1, df2, on='key', how='right')) # 오른쪽 외부 조인






df1 = pd.DataFrame({"class1": [95,92,98,100], "class2": [91,93,97,99]}) # 데이터프레임 생성
# print(df1) # 데이터프레임 출력

# df2 = pd.DataFrame({"class1": [87,89], "class2": [85,90]}) # 데이터프레임 생성
# print(df2) # 데이터프레임 출력

# print(pd.concat([df1, df2])) # 행 방향 병합 및 출력


# df3 = pd.DataFrame({"class1": [96,83]}) # 데이터프레임 생성

# print(pd.concat([df2, df3])) # 행 방향 병합


df4 = pd.DataFrame({"class3": [93,91,95,98]}) # 데이터프레임 생성
# print(df4) # 데이터프레임 출력

print(df1.join(df4)) # 열 방향 병합



# index_label = ['a', 'b', 'c', 'd'] # 행 인덱스 생성
# df1a = pd.DataFrame({"class1": [95,92,98,100], "class2": [91,93,97,99]}, index=index_label) # 데이터프레임 생성
# df4a = pd.DataFrame({"class3": [93,91,95,98]}, index=index_label) # 데이터프레임 생성
# df1a.join(df4a) # 열 방향 병합

# df5 = pd.DataFrame({"class4": [82,92]}) # 데이터프레임 생성

# print(df1.join(df5))


df_left = pd.DataFrame({'key': ['A', 'B', 'C', 'D'], 'left': [1, 2, 3, 4]}) # 데이터프레임 생성
df_right = pd.DataFrame({'key': ['E', 'F', 'G', 'H'], 'left': [5, 6, 7, 8]}) # 데이터프레임 생성
df_center = pd.DataFrame({'key': ['I', 'J', 'K', 'L'], 'left': [5, 6, 7, 8]}) # 데이터프레임 생성

# print(df_left.merge(df_right, how='outer', on='key')) # 내부 조인

df_total = pd.concat([df_left,df_right, df_center]) # 행 방향 병합

print(df_total)
