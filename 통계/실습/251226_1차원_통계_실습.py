import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------------------------------------------
# [1] 데이터 불러오기 (Data Loading)
# --------------------------------------------------------------------------------------
# os 모듈을 사용하여 현재 스크립트 파일의 경로를 동적으로 구합니다.
# __file__: 현재 실행 중인 파이썬 스크립트의 경로를 담고 있는 내장 변수
path = os.path.dirname(__file__)

# 경로와 파일명을 결합하여 CSV 파일의 절대 경로를 생성합니다.
# os.path.join을 사용하면 운영체제(Windows, Mac/Linux)에 맞는 경로 구분자(/ 또는 \)를 자동으로 처리해줍니다.
load_file = os.path.join(path, 'scores_em.csv')

# Pandas 출력 옵션 설정
# 'display.float_format': 부동소수점(float) 데이터를 출력할 때의 형식을 지정합니다.
# '{:,.3f}'.format: 천 단위 구분 기호(,)를 넣고, 소수점 이하 3자리까지 표시하라는 의미입니다.
pd.set_option('display.float_format', '{:,.3f}'.format)

# CSV 파일을 읽어와 DataFrame으로 저장합니다.
# index_col='student number': 'student number' 컬럼을 행의 인덱스(Row Index)로 사용하겠다고 지정합니다.
df = pd.read_csv(load_file, index_col='student number')

# 데이터가 제대로 불러와졌는지 확인하기 위해 상위 5개 행을 출력합니다.
print("--- 데이터프레임 상위 5행 (df.head()) ---")
print(df.head())


# --------------------------------------------------------------------------------------
# [2] 1차원 데이터 정리 (NumPy Array 및 Series 생성)
# --------------------------------------------------------------------------------------
# 실습을 위해 'english' 과목의 점수 중 처음 10개만 슬라이싱하여 사용합니다.
# np.array(): Pandas Series를 NumPy 배열(ndarray)로 변환합니다.
scores = np.array(df['english'])[:10]

print("\n--- 영어 점수 (상위 10개) ---")
print(scores)

# 점수를 더 보기 좋게 관리하기 위해 새로운 DataFrame을 생성합니다.
# 인덱스를 0, 1, 2... 대신 'A', 'B', 'C'... 로 지정하여 학생을 구별합니다.
scores_df = pd.DataFrame(
    {'score': scores},  # 'score'라는 컬럼명으로 scores 데이터를 넣음
    index=pd.Index(     # 인덱스 객체 생성
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        name='student'  # 인덱스의 이름을 'student'로 설정
    )
)
print("\n--- 점수 데이터프레임 (scores_df) ---")
print(scores_df)


# --------------------------------------------------------------------------------------
# [3] 평균 (Mean)
# --------------------------------------------------------------------------------------
# 평균(Mean)은 데이터의 중심을 나타내는 대표적인 대푯값입니다.
# 공식: (모든 데이터의 합) / (데이터의 개수)

print("\n--- [평균] 기본 파이썬 함수 사용 ---")
# sum(scores): 점수의 총합
# len(scores): 점수의 개수
print(sum(scores) / len(scores))

print("\n--- [평균] NumPy 함수 사용 (np.mean) ---")
# np.mean(): 배열의 평균을 계산하는 효율적인 함수
print(np.mean(scores))

print("\n--- [평균] Pandas DataFrame 메서드 사용 (.mean) ---")
# DataFrame의 각 컬럼별 평균을 계산해서 반환합니다.
print(scores_df.mean())


# --------------------------------------------------------------------------------------
# [4] 중앙값 (Median)
# --------------------------------------------------------------------------------------
# 중앙값(Median)은 데이터를 크기 순서대로 정렬했을 때, 정확히 중앙에 위치하는 값입니다.
# 이상치(outlier)가 있을 때 평균보다 데이터의 중심을 더 잘 설명할 수 있습니다.

# 먼저 데이터를 오름차순으로 정렬합니다.
sorted_scores = np.sort(scores)
print("\n--- 정렬된 점수 (sorted_scores) ---")
print(sorted_scores)

# 데이터의 개수를 구합니다.
n = len(sorted_scores)

# 중앙값 계산 로직 구현
# 데이터 개수(n)가 짝수일 때와 홀수일 때 계산 방법이 다릅니다.
if n % 2 == 0:
    # 짝수일 경우: 가운데 두 값의 평균을 중앙값으로 합니다.
    # 인덱스는 0부터 시작하므로, n//2 - 1과 n//2가 가운데 두 인덱스입니다.
    m0 = sorted_scores[n//2 - 1]
    m1 = sorted_scores[n//2]
    median = (m0 + m1) / 2
else:
    # 홀수일 경우: 정확히 가운데 있는 값을 가져옵니다.
    median = sorted_scores[(n+1)//2 - 1]

print("\n--- [중앙값] 직접 계산 ---")
print(median)

print("\n--- [중앙값] NumPy 함수 사용 (np.median) ---")
# np.median(): 정렬과 짝수/홀수 처리를 내부적으로 수행하여 중앙값을 반환합니다.
print(np.median(scores))

print("\n--- [중앙값] Pandas DataFrame 메서드 사용 (.median) ---")
print(scores_df.median())


# --------------------------------------------------------------------------------------
# [5] 최빈값 (Mode)
# --------------------------------------------------------------------------------------
# 최빈값(Mode)은 데이터 집합에서 가장 자주 등장하는(빈도가 가장 높은) 값을 의미합니다.

print("\n--- [최빈값] Pandas Series 메서드 사용 (.mode) ---")

# 예제 1: [1, 1, 1, 2, 2, 3] -> 1이 3번으로 가장 많음
print("데이터: [1, 1, 1, 2, 2, 3]")
print("최빈값:", pd.Series([1, 1, 1, 2, 2, 3]).mode().tolist()) # tolist()로 리스트 변환하여 출력

# 예제 2: [1, 2, 3, 4, 5] -> 모든 값이 1번씩 등장 (모두가 최빈값이 됨)
print("데이터: [1, 2, 3, 4, 5]")
print("최빈값:", pd.Series([1, 2, 3, 4, 5]).mode().tolist())


# --------------------------------------------------------------------------------------
# [6] 편차 (Deviation)
# --------------------------------------------------------------------------------------
# 편차(Deviation)는 각 데이터 값이 평균으로부터 얼마나 떨어져 있는지를 나타냅니다.
# 편차 = 데이터 값 - 평균
# 편차가 크다는 것은 평균에서 멀리 떨어져 있다는 뜻입니다.

mean = np.mean(scores)
deviation = scores - mean

print("\n--- 편차 (각 점수 - 평균) ---")
print(deviation)

# 비교를 위한 다른 데이터셋 예시
# 평균은 비슷하지만, 값들의 퍼짐 정도가 다를 수 있습니다.
another_scores = [50, 60, 58, 54, 51, 56, 57, 53, 52, 59]
another_mean = np.mean(another_scores)
another_deviation = another_scores - another_mean

print("\n--- 다른 데이터셋(another_scores)의 편차 ---")
print(another_deviation)

# 중요 성질: 편차들의 합(또는 평균)은 항상 0이 되어야 합니다.
# 왜냐하면 평균이 데이터의 무게중심이기 때문입니다.
print("\n--- 편차의 평균 확인 (0에 가까워야 함) ---")
print(np.mean(deviation))
print(np.mean(another_deviation))

# 보기 편하게 DataFrame에 'deviation' 컬럼을 추가합니다.
summary_df = scores_df.copy()
summary_df['deviation'] = deviation
print("\n--- 편차가 포함된 요약 데이터프레임 ---")
print(summary_df)

print("\n--- 요약 데이터프레임 전체 평균 확인 ---")
# deviation 컬럼의 평균도 0.000으로 나오는지 확인
print(summary_df.mean())


# --------------------------------------------------------------------------------------
# [7] 분산 (Variance)
# --------------------------------------------------------------------------------------
# 편차의 평균이 0이므로, 산포도(데이터가 퍼진 정도)를 알기 위해 편차를 그냥 더할 수 없습니다.
# 따라서 편차를 제곱하여 모두 양수로 만든 뒤, 그 값들의 평균을 구한 것이 '분산'입니다.
# 분산 = (편차^2)의 평균

print("\n--- [분산] 직접 계산 (편차 제곱의 평균) ---")
print(np.mean(deviation ** 2))

print("\n--- [분산] NumPy 함수 사용 (np.var) ---")
# NumPy의 np.var 기본값은 '모분산'을 계산합니다. (나누는 수 = n)
print(np.var(scores))

print("\n--- [분산] Pandas 메서드 사용 (.var) ---")
# 주의: Pandas의 .var() 메서드는 기본적으로 '불편분산(Unbiased Variance)'을 계산합니다.
# 불편분산은 표본(Sample)을 통해 모집단을 추정할 때 사용하며, 나누는 수가 (n - 1)입니다.
# 그래서 NumPy 결과(모분산)보다 값이 약간 더 큽니다.
print(scores_df.var())

# 편차 제곱 컬럼 추가
summary_df['square of deviation'] = np.square(deviation)
print("\n--- 편차 제곱이 포함된 데이터프레임 ---")
print(summary_df)

print("\n--- 각 컬럼의 평균 확인 ---")
# 'square of deviation'의 평균이 바로 분산입니다.
print(summary_df.mean())


# --------------------------------------------------------------------------------------
# [8] 표준편차 (Standard Deviation)
# --------------------------------------------------------------------------------------
# 분산은 데이터를 제곱했기 때문에 단위가 원래 데이터와 다릅니다. (예: 점수 -> 점수^2)
# 원래 단위로 되돌리기 위해 분산에 제곱근(루트)을 씌운 것이 '표준편차'입니다.

print("\n--- [표준편차] 직접 계산 (분산의 제곱근) ---")
# np.sqrt(): 제곱근 함수
# np.var(scores, ddof=0): 모분산 (ddof=0은 자유도를 0으로 설정하여 n으로 나눔)
print(np.sqrt(np.var(scores, ddof=0)))

print("\n--- [표준편차] NumPy 함수 사용 (np.std) ---")
# np.std(): 표준편차 계산 함수. 기본적으로 모표준편차를 계산합니다.
print(np.std(scores, ddof=0))

# --------------------------------------------------------------------------------------
# [9] 범위 (Range)
# --------------------------------------------------------------------------------------
# 범위는 데이터의 퍼짐 정도를 가장 간단하게 나타내는 지표입니다.
# 범위 = 최댓값 - 최솟값

print("\n--- [범위] Range (최댓값 - 최솟값) ---")
print(np.max(scores) - np.min(scores))


# --------------------------------------------------------------------------------------
# [10] 사분위수 (Quartiles)
# --------------------------------------------------------------------------------------
# 사분위수는 데이터를 크기순으로 나열했을 때 4등분하는 지점(25%, 50%, 75%)의 값입니다.
# Q1: 하위 25% 지점 (제1사분위수)
# Q2: 하위 50% 지점 (중앙값과 동일)
# Q3: 하위 75% 지점 (제3사분위수)

scores_Q1 = np.percentile(scores, 25)
scores_Q3 = np.percentile(scores, 75)

# 사분위 범위 (Interquartile Range, IQR)
# 데이터의 중간 50% 구간의 범위를 의미하며, 이상치에 영향을 덜 받는 산포도 지표입니다.
# IQR = Q3 - Q1
scores_IQR = scores_Q3 - scores_Q1

print("\n--- 사분위 범위 (IQR) ---")
print(scores_IQR)

print("\n--- [요약 통계] Pandas Describe ---")
# count, mean, std, min, 25%, 50%, 75%, max 값을 한 번에 보여줍니다.
print(pd.Series(scores).describe())


# --------------------------------------------------------------------------------------
# [11] 데이터 정규화 (Standardization)
# --------------------------------------------------------------------------------------
# 정규화는 서로 다른 평균과 표준편차를 가진 데이터들을 비교하기 위해 통일된 기준으로 변환하는 것입니다.
# 가장 일반적인 정규화 방법은 Z-score 변환입니다.
# Z-score = (데이터 - 평균) / 표준편차
# 변환 후 데이터는 평균이 0, 표준편차가 1이 됩니다.

z = (scores - np.mean(scores)) / np.std(scores)
print("\n--- Z-score (표준화된 점수) ---")
print(z)

print("\n--- Z-score의 평균과 표준편차 확인 ---")
# 평균은 0에 수렴하고, 표준편차는 1이 되어야 합니다.
print(f"평균: {np.mean(z):.3f}, 표준편차: {np.std(z, ddof=0):.3f}")


# --------------------------------------------------------------------------------------
# [12] 편차치 (Deviation Value, T-score 등)
# --------------------------------------------------------------------------------------
# 편차치(T-score 등)는 평균이 50, 표준편차가 10이 되도록 변환한 값입니다.
# 흔히 시험 점수의 '표준점수'나 지능지수(IQ) 등에서 볼 수 있는 형태입니다.
# 공식: 50 + 10 * Z-score

z = 50 + 10 * (scores - np.mean(scores)) / np.std(scores)
print("\n--- 편차치 (평균 50, 표준편차 10 기준) ---")
print(z)

# 데이터프레임에 편차치 컬럼을 추가하여 원본 점수와 비교합니다.
scores_df['deviation value'] = z
print("\n--- 점수와 편차치가 포함된 최종 데이터프레임 ---")
print(scores_df)

# (참고) 전체 데이터 셋(50명)에 대한 요약 통계
english_scores = np.array(df['english'])
print("\n--- 전체 50명 영어 점수에 대한 요약 통계 ---")
print(pd.Series(english_scores).describe())


# --------------------------------------------------------------------------------------
# [13] 도수분포표 (Frequency Distribution)
# --------------------------------------------------------------------------------------
# 도수분포표는 데이터를 구간(계급)으로 나누어 각 구간에 속한 데이터의 개수(도수)를 나타낸 표입니다.
# 데이터의 전반적인 분포 형태를 파악할 때 유용합니다.

# np.histogram 함수 사용
# data: 분석할 데이터 (english_scores)
# bins=10: 계급(구간)의 개수를 10개로 설정
# range=(0, 100): 점수의 범위를 0점부터 100점까지로 설정

freq, _ = np.histogram(english_scores, bins=10, range=(0, 100))

print("\n--- 도수분포표 (0~100점, 10점 단위 구간) ---")
print(freq)
# 출력 결과 예시: [0 0 0 2 8 16 18 6 0 0]
# 의미:
# 0~10점: 0명
# ...
# 30~40점: 2명
# ...
# 60~70점: 18명
# ...


# --------------------------------------------------------------------------------------
# [14] 시각화 (Visualization)
# --------------------------------------------------------------------------------------
# Matplotlib을 사용하여 도수분포표를 히스토그램으로 시각화합니다.
# 시각화를 통해 데이터의 분포를 직관적으로 이해할 수 있습니다.

# 캔버스(Figure)를 생성합니다.
# figsize=(10, 6): 가로 10인치, 세로 6인치 크기로 설정
fig = plt.figure(figsize=(10, 6))

# 캔버스 위에 그래프를 그릴 영역(Axes)을 지정합니다.
# add_subplot(111): 1x1 그리드의 첫 번째 영역을 의미합니다. (행, 열, 인덱스)
ax = fig.add_subplot(111)

# 히스토그램(Histogram) 그리기
# bins=10: 계급 수를 10으로 설정
# range=(0, 100): 0~100점 사이의 데이터만 표시
# freq: 각 계급의 도수, _: 계급 경계값, _ : patches(그래프 객체)
freq, _, _ = ax.hist(english_scores, bins=10, range=(0, 100))

# 축 레이블(Label) 설정
ax.set_xlabel('score')          # X축 이름: score
ax.set_ylabel('person number')  # Y축 이름: person number (학생 수)

# 축 눈금(Ticks) 설정
# X축: 0부터 100까지 10점 간격으로 눈금 표시 (0, 10, 20, ..., 100)
# np.linspace(0, 100, 11): 0부터 100까지 11개의 숫자를 균등하게 생성
ax.set_xticks(np.linspace(0, 100, 11))

# Y축: 0부터 최대 도수(freq.max())까지 1단위로 눈금 표시
# np.arange(0, freq.max()+1): 0, 1, 2, ..., max값
ax.set_yticks(np.arange(0, freq.max() + 1))

# 그래프 표시
plt.show()


# --------------------------------------------------------------------------------------
# [15] 상대도수 히스토그램과 누적 상대도수 꺾은선 그래프
# --------------------------------------------------------------------------------------
# 히스토그램(도수)과 함께 누적 상대도수(비율)를 하나의 그래프에 표현합니다.

# 캔버스 생성 (크기 10x6)
fig = plt.figure(figsize=(10, 6))

# 첫 번째 Y축 (왼쪽): 도수(Frequency) 및 상대도수 히스토그램을 그릴 영역
ax1 = fig.add_subplot(111)

# 두 번째 Y축 (오른쪽): 누적 상대도수(Cumulative Relative Frequency)를 그릴 영역
# twinx(): X축은 공유하면서 Y축만 서로 다른 스케일을 사용할 수 있게 만들어줍니다.
ax2 = ax1.twinx()

# 상대도수(Relative Frequency) 계산을 위한 가중치(weights) 생성
# np.ones_like(english_scores): 점수 데이터와 동일한 길이의 1로 채워진 배열 생성
# len(english_scores): 전체 데이터 개수 (50)
# 각 데이터가 전체에서 차지하는 비율(1/50 = 0.02)을 가중치로 줌.
weights = np.ones_like(english_scores) / len(english_scores)

# 상대도수 히스토그램 그리기
# weights 인수에 위에서 계산한 가중치를 전달하여, Y축이 '빈도수'가 아닌 '비율'이 되도록 함
# bins=25: 구간을 25개로 더 잘게 나눔 (0~100점을 4점 단위로)
rel_freq, _, _ = ax1.hist(english_scores, bins=25,
                          range=(0, 100), weights=weights)

# 누적 상대도수(Cumulative Relative Frequency) 계산
# np.cumsum(): 배열의 누적 합을 계산하는 NumPy 함수
cum_rel_freq = np.cumsum(rel_freq)

# 꺾은선 그래프의 X축 좌표(계급값) 생성
# 구간이 0~4, 4~8 ... 이므로 각 구간의 중심값(2, 6 ...)을 구해야 함
# i: 0, 4, 8 ... (구간의 시작값)
# (i + (i+4)) // 2 : 구간의 시작과 끝의 평균 = 계급값
class_value = [(i+(i+4))//2 for i in range(0, 100, 4)]

# 누적 상대도수 꺾은선 그래프 그리기 (ax2 사용)
# ls='--': 선 스타일을 점선(dashed)으로 설정
# marker='o': 데이터 위치에 원형 마커 표시
# color='gray': 선과 마커 색상을 회색으로 설정
ax2.plot(class_value, cum_rel_freq,
         ls='--', marker='o', color='gray')

# 오른쪽 Y축(ax2)의 눈금선(grid)은 제거 (왼쪽 Y축 기준과 겹쳐서 복잡해지는 것 방지)
ax2.grid(visible=False)

# 축 레이블 및 눈금 설정
ax1.set_xlabel('score')                           # X축: 점수
ax1.set_ylabel('relative frequency')              # 왼쪽 Y축: 상대도수
ax2.set_ylabel('cumulative relative frequency')   # 오른쪽 Y축: 누적 상대도수

# X축 눈금을 0부터 100까지 25개 구간(4점 간격)에 맞춰 설정 (0, 4, 8, ..., 100)
ax1.set_xticks(np.linspace(0, 100, 25+1))

# 그래프 표시
plt.show()


# --------------------------------------------------------------------------------------
# [16] 상자 그림 (Boxplot)
# --------------------------------------------------------------------------------------
# 데이터의 분포(최솟값, Q1, 중앙값, Q3, 최댓값)를 한눈에 보여주는 시각화 도구입니다.

# 캔버스 생성 (크기 5x6)
fig = plt.figure(figsize=(5, 6))
ax = fig.add_subplot(111)

# 상자 그림 그리기
# labels=['english']: X축의 해당 데이터 레이블을 'english'로 설정
ax.boxplot(english_scores, labels=['english'])

# 그래프 표시
plt.show()