import matplotlib.pyplot as plt
import matplotlib as mpl
import korean
import pandas as pd
import numpy as np


"""
##### 서울시 도봉구에서 시설총규모 상위 10개 치킨집? #####

01. 영업중인 가게만 필터링
02. "소재지전체주소"와 "도로명전체주소"가 결측치일 경우 둘 중에 하나만이라도 있는 데이터의 값을 사용
03. 사용이 끝난 "상세영업상태코드", "소재지전체주소", "도로명전체주소" 컬럼들을 데이터프레임에서 삭제
04. "소재지주소" 컬럼 값에 "서울특별시 도봉구" 문자열이 포함된 행만 필터링
05. 도봉구 데이터 중 "업태구분명"에 '통닭' 또는 '치킨'이 포함된 행만 필터링 후 그 결과를 "시설총규모" 컬럼 기준으로 "내림차순" 정렬
06. DataFrame의 "상위 10개 행"만 추출
07. bar 차트로 시각 화

"""


# 현재 실행 중인 파일의 전체 경로를 역슬래시("\\") 기준으로 분리하여 리스트로 만듭니다.
file_list = __file__.split("\\") 
# 파일 경로에서 리스트의 마지막 요소(파일 이름)를 "cctv_result.csv"로 대체하여
# 로드할 CSV 파일의 전체 경로를 만듭니다. (동일 디렉토리에 있다고 가정)
load_file = __file__.replace(file_list[-1], "서울특별시_일반음식점.csv")


# 지정된 경로의 CSV 파일을 읽어 DataFrame 변수 df1에 저장합니다.
# 이때, "상세영업상태코드", "사업장명", "소재지전체주소", "도로명전체주소", "업태구분명", "시설총규모" 컬럼만 가져옵니다 (usecols).
df1 = pd.read_csv(
    load_file,
    usecols = ['상세영업상태코드', '사업장명', '소재지전체주소', '도로명전체주소', '업태구분명', '시설총규모']
)

# "상세영업상태코드"가 1인 행만 필터링하여 "영업 중"인 가게 데이터만 open_store에 저장합니다.
open_store = df1[df1['상세영업상태코드'] == 1].copy() # SettingWithCopyWarning 방지용 .copy() 사용 권장

# "combine_first"를 사용하여 "소재지전체주소"가 결측치일 경우 "도로명전체주소"의 값으로 채워 "소재지주소" 컬럼을 새로 만듭니다.
# (두 주소 중 하나라도 값이 있는 것을 우선적으로 사용해 주소 컬럼을 통합)
open_store['소재지주소'] = open_store['소재지전체주소'].combine_first(open_store['도로명전체주소'])

# 사용이 끝난 "상세영업상태코드", "소재지전체주소", "도로명전체주소" 컬럼들을 데이터프레임에서 삭제합니다 (axis=1).
open_store.drop(columns=['상세영업상태코드', '소재지전체주소', '도로명전체주소'], axis=1, inplace=True)

# "소재지주소" 컬럼 값에 "서울특별시 도봉구" 문자열이 포함된 행만 필터링하여 dobong에 저장합니다.
dobong = open_store[open_store['소재지주소'].str.contains('서울특별시 도봉구', na=False)]

# 도봉구 데이터 중 "업태구분명"에 '통닭' 또는 '치킨'이 포함된 행만 필터링합니다.
# 그 결과를 "시설총규모" 컬럼 기준으로 "내림차순"(ascending=False) 정렬하여 dobong_chiken에 저장합니다.
dobong_chiken = dobong[dobong['업태구분명'].str.contains('통닭|치킨', na=False)].sort_values(by='시설총규모', ascending=False)

# 정렬된 dobong_chiken DataFrame의 "상위 10개 행"만 추출하여 top10_dobong에 저장합니다.
top10_dobong = dobong_chiken.head(10)

# 그래프(figure) 크기를 가로 12인치, 세로 8인치로 설정합니다.
plt.figure(figsize=(12, 8))

# "bar" 함수를 사용하여 수직 막대 그래프를 그립니다.
# x축에 "사업장명"을, y축(막대 높이)에 "시설총규모" 값을 사용합니다.
plt.bar(top10_dobong['사업장명'], top10_dobong['시설총규모'])

# 그래프 제목을 설정합니다.
plt.title('도봉구 시설총규모 상위 10개 치킨집')

# x축 레이블을 '사업장명'으로 설정합니다.
plt.xlabel('사업장명')

# y축 레이블을 '시설총규모'로 설정합니다.
plt.ylabel('시설총규모')

# x축 레이블(사업장명)이 겹치지 않도록 25도 회전하여 표시합니다.
plt.xticks(rotation=25)


# 생성된 그래프를 'chiken_analysis02.png' 파일로 저장합니다.
plt.savefig('chiken_analysis02.png')
# 그래프 저장 완료 메시지를 출력합니다.
print("\n그래프가 'chiken_analysis02.png'로 저장되었습니다.")

# 그래프를 화면에 출력합니다.
plt.show()



"""
이번에도 데이터가 너무 많아서 결과를 속단할 수 없었다. 
결국 문자열을 split하고 데이터를 필터링하는 과정을 통해서 
도봉구의 시설총규모가 가장 큰 10개의 치킨집을 찾아낼 수 있었다.


"""