import numpy as np
import pandas as pd
import os

# -----------------------------------------------------
# 1. 데이터 불러오기 (Data Loading)
# -----------------------------------------------------
# 현재 실행 중인 파일(__file__)의 디렉토리 경로를 구합니다.
path = os.path.dirname(__file__)

# 경로와 파일명을 결합하여 CSV 파일의 절대 경로를 생성합니다.
load_file = os.path.join(path, 'scores_em.csv')

# 출력할 때 소수점 이하 3자리까지 표시하도록 Pandas 옵션을 설정합니다.
pd.set_option('display.float_format', '{:,.3f}'.format)

# CSV 파일을 읽어옵니다. 'student number' 컬럼을 인덱스로 지정합니다.
df = pd.read_csv(load_file, index_col='student number')

# 데이터의 상위 5행을 출력하여 제대로 불러와졌는지 확인합니다.
print("--- 데이터프레임 상위 5행 ---")
print(df.head())

# -----------------------------------------------------
# 2. 1차원 데이터 정리 (NumPy Array 및 Series 생성)
# -----------------------------------------------------
# 'english' 과목의 점수 중 처음 10개 데이터를 가져와 NumPy 배열로 만듭니다.
scores = np.array(df['english'])[:10]
print("\n--- 영어 점수 (상위 10개) ---")
print(scores)

# 점수를 보기 좋게 DataFrame으로 생성합니다. 인덱스를 A~J 학생으로 지정합니다.
scores_df = pd.DataFrame({'score': scores},
    index=pd.Index(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        name='student'
    )
)
print("\n--- 점수 데이터프레임 ---")
print(scores_df)

# -----------------------------------------------------
# 3. 평균 (Mean)
# -----------------------------------------------------
# 평균값 계산: (모든 데이터의 합) / (데이터의 개수)
print("\n--- 평균 계산 ---")
print(sum(scores) / len(scores))

# NumPy 함수를 이용한 평균 계산
print(np.mean(scores))

# Pandas DataFrame 메서드를 이용한 평균 계산
print(scores_df.mean())

# -----------------------------------------------------
# 4. 중앙값 (Median)
# -----------------------------------------------------
# 중앙값: 데이터를 크기 순서대로 정렬했을 때 중앙에 위치하는 값
sorted_scores = np.sort(scores)
print("\n--- 정렬된 점수 ---")
print(sorted_scores)

n = len(sorted_scores)
# 데이터 개수가 짝수일 경우: 가운데 두 값의 평균을 취합니다.
if n % 2 == 0:
    m0 = sorted_scores[n//2 - 1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1) / 2
else:
    # 데이터 개수가 홀수일 경우: 정확히 가운데 있는 값을 취합니다.
    median = sorted_scores[(n+1)//2 - 1]
print("\n--- 중앙값 계산 ---")
print(median)

# NumPy를 이용한 중앙값 계산
print(np.median(scores))

# Pandas를 이용한 중앙값 계산
print(scores_df.median())

# -----------------------------------------------------
# 5. 최빈값 (Mode)
# -----------------------------------------------------
# 최빈값: 데이터에서 가장 자주 등장하는 값
print("\n--- 최빈값 ---")
# [1, 1, 1, 2, 2, 3] -> 1이 가장 많으므로 최빈값은 1
print(pd.Series([1, 1, 1, 2, 2, 3]).mode())
# [1, 2, 3, 4, 5] -> 모두 한 번씩 등장하므로 전부 최빈값이 됨
print(pd.Series([1, 2, 3, 4, 5]).mode())

# -----------------------------------------------------
# 6. 편차 (Deviation)
# -----------------------------------------------------
# 각 데이터가 평균으로부터 얼마나 떨어져 있는지를 나타내는 값
# 편차 = 데이터 값 - 평균
mean = np.mean(scores)
deviation = scores - mean
print("\n--- 편차 ---")
print(deviation)

# 다른 데이터셋 예시
another_scores = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean
print("\n--- 다른 데이터셋의 편차 ---")
print(another_deviation)

# 편차의 평균은 항상 0이어야 합니다. (평균을 중심으로 분포하기 때문)
print("\n--- 편차의 평균 (0이어야 함) ---")
print(np.mean(deviation))
print(np.mean(another_deviation))

# DataFrame에 편차 컬럼 추가해서 확인
summary_df = scores_df.copy()
summary_df['deviation'] = deviation
print("\n--- 편차가 포함된 요약 데이터프레임 ---")
print(summary_df)

# 편차 컬럼의 평균도 0에 가까운지 확인
print(summary_df.mean())

# -----------------------------------------------------
# 7. 분산 (Variance)
# -----------------------------------------------------
# 편차의 평균이 0이므로, 산포도를 계산하기 위해 편차를 제곱하여 평균을 냄
# 분산 = 편차 제곱의 평균
print("\n--- 분산 (편차 제곱의 평균) ---")
print(np.mean(deviation ** 2))

# NumPy를 이용한 분산 계산 (기본적으로 모분산)
print(np.var(scores))

# Pandas의 var는 기본적으로 불편분산(sample variance)을 계산함
# NumPy 값과 비교
print(scores_df.var())

# DataFrame에 '편차 제곱' 컬럼 추가
summary_df['square of deviation'] = np.square(deviation)
print("\n--- 편차 제곱이 포함된 요약 데이터프레임 ---")
print(summary_df)

# 편차 제곱의 평균(=분산) 확인
print(summary_df.mean())

# -----------------------------------------------------
# 8. 표준편차 (Standard Deviation)
# -----------------------------------------------------
# 분산은 제곱된 값이므로 원래 단위로 돌리기 위해 제곱근(루트)을 씌움
print("\n--- 표준편차 ---")
# 분산(모분산 기준 ddof=0)의 제곱근
print(np.sqrt(np.var(scores, ddof=0)))

# NumPy std 함수 사용 (ddof=0으로 모표준편차 계산)
print(np.std(scores, ddof=0))

# -----------------------------------------------------
# 9. 범위 (Range)
# -----------------------------------------------------
# 최댓값 - 최솟값
print("\n--- 범위 (Range) ---")
print(np.max(scores) - np.min(scores))

# -----------------------------------------------------
# 10. 사분위수 (Quartiles)
# -----------------------------------------------------
# 데이터를 4등분하는 지점들
# Q1(25%지점), Q3(75%지점)
scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)
# 사분위 범위 (IQR) = Q3 - Q1
scores_IQR = scores_Q3 - scores_Q1
print("\n--- 사분위 범위 (IQR) ---")
print(scores_IQR)

# Pandas describe()로 요약 통계량 한 번에 확인
print("\n--- Series 요약 통계 (Describe) ---")
print(pd.Series(scores).describe())

# -----------------------------------------------------
# 11. 데이터 정규화 (Standardization)
# -----------------------------------------------------
# 평균이 0, 표준편차가 1이 되도록 변환 (Z-score)
# 식: (데이터 - 평균) / 표준편차
z = (scores - np.mean(scores)) / np.std(scores)
print("\n--- Z-score 계산 (정규화) ---")
print(z)

# 정규화된 데이터의 평균은 0, 표준편차는 1이 됨을 확인
print("\n--- Z-score의 평균과 표준편차 ---")
print(np.mean(z), np.std(z, ddof=0))

# -----------------------------------------------------
# 12. 편차치 (Deviation Value / T-score 등)
# -----------------------------------------------------
# 평균을 50, 표준편차를 10으로 맞춘 점수 (예: 수능 표준점수, IQ 등과 유사한 개념)
# 식: 50 + 10 * z
z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
print("\n--- 편차치 (평균 50, 표준편차 10) ---")
print(z)

# DataFrame에 편차치 컬럼 추가
scores_df['deviation value'] = z
print("\n--- 편차치가 포함된 최종 데이터프레임 ---")
print(scores_df)

# 전체 영어 점수에 대한 요약 통계
english_scores = np.array(df['english'])
print("\n--- 전체 영어 점수 요약 통계 ---")
print(pd.Series(english_scores).describe())


# -----------------------------------------------------
# 13. 도수분포표 (Frequency Distribution)
# -----------------------------------------------------
# np.histogram 함수를 사용하여 도수분포를 계산합니다.
# bins=10: 데이터를 10개의 구간(계급)으로 나눕니다.
# range=(0, 100): 0점부터 100점까지의 범위를 대상으로 합니다.
# freq: 각 구간(계급)에 속하는 데이터의 개수(도수)
# _: 각 구간의 경계값 (여기서는 사용하지 않으므로 _로 받음)
freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))
print("\n--- 도수분포표 (0-100, 계급수=10) ---")
print(freq)