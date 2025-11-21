import pandas as pd # pandas 불러오기

# print(pd.read_csv('sea_rain1.csv', index_col="연도")) # index_col 옵션 사용하여 '연도' 열을 인덱스로 지정


df_WH = pd.DataFrame(
    {'Weight':[62, 67, 55, 74], 'Height':[165, 177, 160, 180]},
    index=['ID_1', 'ID_2', 'ID_3', 'ID_4']
) # DataFrame 생성
df_WH.index.name = 'User' # 인덱스 이름 지정

bmi = df_WH['Weight'] / (df_WH['Height'] / 100) ** 2 # BMI 계산
df_WH['BMI'] = bmi # DataFrame에 BMI 열 추가

# print(df_WH) # DataFrame 출력

df_WH.to_csv('save_DataFrame.csv') # DataFrame을 CSV 파일로 저장

# print(pd.read_csv('save_DataFrame.csv', index_col="User")) # 저장된 CSV 파일 불러오기


df_pr = pd.DataFrame(
        {"판매가격": [2000, 3000, 5000, 10000], "판매수량": [32, 53, 40, 25]},
        index=["p1001", "p1002", "p1003", "p1004"]
    ) # DataFrame 생성
df_pr.index.name = '제품번호' # 인덱스 이름 지정

print(df_pr) # DataFrame 출력

file_name = 'save_product.csv'
df_pr.to_csv(file_name) # DataFrame을 CSV 파일로 저장