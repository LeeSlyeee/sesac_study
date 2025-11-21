import pandas as pd # 판다스 불러오기
import numpy as np # 넘파이 불러오기


## pd.Series(집합적 자료형)
## pd.Series(리스트)
# s_list = pd.Series([1,2,3])
# print(s_list)


## 시리즈 생성시 반드시 집합적 자료형을 이용해야 함
# s_tuple = pd.Series((1,2,3))
# print(s_tuple)


## pd.Series(1,2,3) # 시리즈 생성시 반드시 집합적 자료형을 이용해야 함
# s2 = pd.Series(['a','b','c'])
# print(s2)


## 리스트내에 서로 다른 type의 data가 있으면 형변환 일어남- 문자열로 변환됨
# s_1 = pd.Series(['a',1,3.0])
# print(s_1)


s = pd.Series(range(10,14)) # index 인수는 생략됨
print(s)
