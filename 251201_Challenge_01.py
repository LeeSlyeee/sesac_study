import matplotlib.pyplot as plt
import matplotlib as mpl
import korean
import pandas as pd
import numpy as np


"""
##### 서울시 서대문구에서 치킨집이 가장 많은 동은? #####



"""


# 현재 실행 중인 파일의 전체 경로를 역슬래시("\\") 기준으로 분리하여 리스트로 만듭니다.
file_list = __file__.split("\\") 
# 파일 경로에서 리스트의 마지막 요소(파일 이름)를 "cctv_result.csv"로 대체하여
# 로드할 CSV 파일의 전체 경로를 만듭니다. (동일 디렉토리에 있다고 가정)
load_file = __file__.replace(file_list[-1], "서울특별시_일반음식점.csv")


# 데이터프레임에서 "상세영업상태코드", "소재지전체주소", "도로명전체주소", "업태구분명" 컬럼만 읽어와 df1에 저장합니다.
df1 = pd.read_csv(
    load_file,
    usecols = ['상세영업상태코드', '소재지전체주소', '도로명전체주소', '업태구분명']
)

# "상세영업상태코드"가 1인 행만 필터링하여 "영업 중"인 가게 데이터만 open_store에 저장합니다.
open_store = df1[df1['상세영업상태코드'] == 1]

# "combine_first"를 사용하여 "소재지전체주소"가 결측치일 경우 "도로명전체주소"의 값으로 채워 "소재지주소" 컬럼을 새로 만듭니다.
# 즉, 두 주소 컬럼 중 하나라도 값이 있는 것을 우선적으로 사용해 주소 컬럼을 통합합니다.
open_store['소재지주소'] = open_store['소재지전체주소'].combine_first(open_store['도로명전체주소'])

# 사용이 끝난 "소재지전체주소"와 "도로명전체주소" 컬럼을 데이터프레임에서 삭제합니다 (axis=1).
open_store.drop(columns=['소재지전체주소', '도로명전체주소'], axis=1, inplace=True)

# "소재지주소" 컬럼 값에 "서울특별시 서대문구" 문자열이 포함된 행만 필터링하여 seodaemun에 저장합니다.
seodaemun = open_store[open_store['소재지주소'].str.contains('서울특별시 서대문구', na=False)]

# 서대문구 데이터 중 "업태구분명"에 "통닭 또는 치킨" 문자열이 포함된 행만 필터링하여 seodaemun_chiken에 저장합니다.
seodaemun_chiken = seodaemun[seodaemun['업태구분명'].str.contains('통닭|치킨', na=False)]


# (사용되지 않는 코드) "소재지주소" 컬럼을 공백(' ') 기준으로 분리하여 tmp에 저장합니다.
tmp = seodaemun_chiken['소재지주소'].str.split(' ')


# "소재지주소"를 받아 동 이름을 추출하는 사용자 정의 함수를 정의합니다.
def dong_name(x):
    # 주소를 공백 기준으로 분리한 후, 세 번째 요소(인덱스 2)를 동 이름으로 가정하여 반환합니다.
    # 예: "서울특별시 서대문구 홍제동 123" -> '서울특별시', '서대문구', '홍제동', ... -> '홍제동' 추출
    x = x.split(" ")[2]
    return x

# "apply" 함수를 사용하여 "소재지주소"의 모든 값에 "dong_name" 함수를 적용하고, 결과를 "동이름" 컬럼에 저장합니다.
seodaemun_chiken['동이름'] = seodaemun_chiken['소재지주소'].apply(dong_name)

# "동이름" 컬럼의 각 값(동 이름)별 빈도수(치킨집 개수)를 계산하여 dong_counts에 저장합니다.
dong_counts = seodaemun_chiken['동이름'].value_counts()

# 계산된 빈도수를 "오름차순"으로 정렬합니다. (가장 많은 동이 Series의 맨 위에 위치)
dong_counts = dong_counts.sort_values(ascending=True)

# 그래프 크기를 가로 10, 세로 6으로 설정합니다.
plt.figure(figsize=(10, 6))
# 정렬된 dong_counts Series를 수평 막대 그래프("barh")로 그립니다.
dong_counts.plot(kind='barh')

# 그래프 제목, x축, y축 레이블을 설정합니다.
plt.title('서대문구 동별 치킨집 현황')
plt.xlabel('치킨집 개수')
plt.ylabel('동이름')

# 그래프를 화면에 출력합니다.
plt.show()