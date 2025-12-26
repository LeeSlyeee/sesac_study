import pandas as pd

# 1. 'pandas' 라이브러리를 'pd'라는 별칭으로 불러옵니다.
#    데이터 분석과 조작을 위한 핵심 라이브러리입니다.
import pandas as pd

# 2. 현재 실행 중인 파일(__file__)의 전체 경로 문자열을 
#    역슬래시(\)를 기준으로 잘라(split) 리스트로 만듭니다.
#    예: ['c:', 'Users', ..., '실습', '251226_통계_실습.py']
file_list = __file__.split("\\") 

# 3. 현재 파일의 전체 경로(__file__)에서,
#    마지막 부분인 현재 파일명(file_list[-1])을 "sport_test.csv"로 바꿉니다(replace).
#    이렇게 하면 현재 파이썬 파일과 같은 폴더에 있는 CSV 파일의 경로를 얻게 됩니다.
load_file = __file__.replace(file_list[-1], "sport_test.csv")

# 4. pd.read_csv 함수를 사용하여 CSV 파일을 데이터프레임(DataFrame)으로 읽어옵니다.
#    index_col="학생번호" 옵션은 '학생번호' 컬럼을 0, 1, 2... 같은 기본 인덱스 대신 
#    이 데이터프레임의 행 인덱스(Row Index)로 사용하겠다는 뜻입니다.
df = pd.read_csv(load_file, index_col="학생번호")

print("\n--- [전체 데이터프레임 출력] ---")
# 5. 불러온 데이터프레임 'df'의 전체 내용을 출력합니다.
print(df)

print("\n--- [특정 컬럼(Series) 출력] ---")
# 6. 데이터프레임에서 '악력'이라는 이름의 컬럼만 선택하여 출력합니다.
#    이때 반환되는 형태는 pandas의 Series(시리즈)입니다.
print(df['악력'])

print("\n--- [데이터프레임 크기(Shape) 출력] ---")
# 7. 데이터프레임의 행(Row) 개수와 열(Column) 개수를 튜플(Tuple) 형태로 확인합니다.
#    예: (10, 5)는 10개의 행과 5개의 열이 있다는 뜻입니다.
print(df.shape)