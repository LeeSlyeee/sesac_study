import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# --------------------------------------------------------------------------------------
# [1] 데이터 불러오기 (Data Loading)
# --------------------------------------------------------------------------------------
# os 모듈을 사용하여 현재 스크립트 파일의 경로를 동적으로 구합니다.
path = os.path.dirname(__file__)

# 경로와 파일명을 결합하여 CSV 파일의 절대 경로를 생성합니다.
load_file = os.path.join(path, 'scores_em.csv')

# Pandas 출력 옵션 설정 (소수점 이하 3자리까지 표시)
pd.set_option('display.float_format', '{:,.3f}'.format)

# CSV 파일 읽기 (인덱스를 'student number'로 설정)
df = pd.read_csv(load_file, index_col='student number')


# --------------------------------------------------------------------------------------
# [2] 2차원 데이터 정리 (NumPy Array 및 DataFrame 생성)
# --------------------------------------------------------------------------------------
# 영어와 수학 점수 상위 10개 데이터를 추출하여 분석합니다.
en_scores = np.array(df['english'])[:10]
ma_scores = np.array(df['mathematics'])[:10]

# 점수를 보기 좋게 DataFrame으로 생성합니다.
scores_df = pd.DataFrame(
    {'english': en_scores, 'mathematics': ma_scores},
    index=pd.Index(
        ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
        name='student'
    )
)
print("--- 영어/수학 점수 데이터프레임 ---")
print(scores_df)


# --------------------------------------------------------------------------------------
# [3] 공분산 (Covariance) - 수식으로 직접 계산
# --------------------------------------------------------------------------------------
# 공분산은 두 변수(X, Y)가 얼마나 함께 변하는지를 나타내는 지표입니다.
# - 양수: X가 증가할 때 Y도 증가 (양의 상관관계)
# - 음수: X가 증가할 때 Y는 감소 (음의 상관관계)
# - 0에 가까움: 두 변수 간에 선형적인 관계가 거의 없음
# 수식: Cov(X, Y) = Mean((X - Mean(X)) * (Y - Mean(Y)))

print("\n--- [공분산] 직접 계산 과정 ---")
summary_df = scores_df.copy()

# 영어 점수 편차 계산 (각 점수 - 영어 평균)
summary_df['english_deviation'] = summary_df['english'] - summary_df['english'].mean()

# 수학 점수 편차 계산 (각 점수 - 수학 평균)
summary_df['mathematics_deviation'] = summary_df['mathematics'] - summary_df['mathematics'].mean()

# 편차의 곱 계산 ((X - Mean(X)) * (Y - Mean(Y)))
summary_df['product of deviations'] = summary_df['english_deviation'] * summary_df['mathematics_deviation']

print(summary_df)

print("\n--- [공분산] 편차의 곱의 평균 ---")
# 편차의 곱들의 평균이 바로 공분산입니다.
print(summary_df['product of deviations'].mean())


# --------------------------------------------------------------------------------------
# [4] 공분산 (Covariance) - NumPy 함수 사용
# --------------------------------------------------------------------------------------
# np.cov(x, y): 공분산 행렬(Covariance Matrix)을 반환합니다.
# 반환 형태:
# [[Var(X), Cov(X,Y)],
#  [Cov(Y,X), Var(Y)]]
# ddof=0: 모공분산 계산 (나누는 수 = N). (기본값은 ddof=1로 표본공분산)

print("\n--- [공분산 행렬] NumPy np.cov (ddof=0) ---")
cov_mat = np.cov(en_scores, ma_scores, ddof=0)
print(cov_mat)

print("\n--- 공분산 값 추출 ---")
# (0, 1) 요소와 (1, 0) 요소가 영어와 수학의 공분산입니다.
# (0, 0)은 영어의 분산, (1, 1)은 수학의 분산입니다.
print("Cov(en, ma):", cov_mat[0, 1])
print("Var(en):", cov_mat[0, 0], "/ Var(ma):", cov_mat[1, 1])

# 검증: 각 변수의 분산과 일치하는지 확인
# np.var로 따로 계산한 값과 공분산 행렬의 대각 성분이 같은지 봅니다.
print("NumPy var 함수 결과:", np.var(en_scores, ddof=0), np.var(ma_scores, ddof=0))


# --------------------------------------------------------------------------------------
# [5] 상관계수 (Correlation Coefficient) - 직접 계산
# --------------------------------------------------------------------------------------
# 공분산은 단위(점수*점수)에 의존하고 값의 범위를 가늠하기 어렵습니다.
# 이를 -1 ~ 1 사이의 값으로 표준화한 것이 상관계수(Pearson Correlation Coefficient)입니다.
# 공식: Correlation = Cov(X, Y) / (Std(X) * Std(Y))

print("\n--- [상관계수] 공분산과 표준편차로 직접 계산 ---")
# 수식: 공분산 / (영어표준편차 * 수학표준편차)
# np.std도 ddof=0으로 맞춰주어야 합니다.
correlation = np.cov(en_scores, ma_scores, ddof=0)[0, 1] / (np.std(en_scores) * np.std(ma_scores))
print(correlation)


# --------------------------------------------------------------------------------------
# [6] 상관계수 (NumPy / Pandas 함수 사용)
# --------------------------------------------------------------------------------------
print("\n--- [상관계수 행렬] NumPy np.corrcoef ---")
# np.corrcoef(): 상관계수 행렬 반환
# [[Corr(X,X), Corr(X,Y)],
#  [Corr(Y,X), Corr(Y,Y)]]
# 대각선 성분은 자기 자신과의 상관계수이므로 항상 1입니다.
print(np.corrcoef(en_scores, ma_scores))

print("\n--- [상관계수 행렬] Pandas DataFrame .corr() ---")
# DataFrame의 모든 컬럼 간 상관계수를 계산합니다.
print(scores_df.corr())


# --------------------------------------------------------------------------------------
# [7] 시각화: 산점도 (Scatter Plot)
# --------------------------------------------------------------------------------------
# 두 변수 간의 관계를 좌표평면에 점으로 찍어 나타내는 가장 기본적인 그래프입니다.

# 전체 데이터(50명) 로드
english_scores = np.array(df['english'])
math_scores = np.array(df['mathematics'])

# 캔버스 생성 (크기 8x8)
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)

# 산점도 그리기 (x: 영어점수, y: 수학점수)
ax.scatter(english_scores, math_scores)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')

print("\n--- 산점도를 표시합니다. (팝업 창 확인) ---")
plt.show()


# --------------------------------------------------------------------------------------
# [8] 시각화: 회귀직선 (Regression Line)
# --------------------------------------------------------------------------------------
# 데이터의 경향성을 가장 잘 나타내는 직선(Trend Line)을 그립니다.
# 식: y = β_0 + β_1 * x (1차 함수 형태)

# np.polyfit(x, y, 1): 1차식(직선)의 계수(slope, intercept)를 계산
# 반환값: [기울기(β_1), 절편(β_0)]
poly_fit = np.polyfit(english_scores, math_scores, 1)

# np.poly1d(coefficients): 계수들을 입력받아 함수 식 객체 생성
# 이 함수에 x값을 넣으면 예측된 y값을 반환해 줍니다.
poly_1d = np.poly1d(poly_fit)

# 직선을 그리기 위한 X축 데이터 생성 (최솟값 ~ 최댓값 구간)
xs = np.linspace(english_scores.min(), english_scores.max())
# X축 데이터에 대응하는 Y축 데이터(예측값) 생성
ys = poly_1d(xs)

fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111)
ax.set_xlabel('english')
ax.set_ylabel('mathematics')

# 산점도 그리기
ax.scatter(english_scores, math_scores, label='score')

# 회귀직선 그리기
# color='gray': 회색 선으로 표시
# label에 수식을 문자열로 포맷팅하여 넣어줌 (예: 0.62+0.42x)
ax.plot(xs, ys, color='gray',
        label=f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x')

# 범례 표시 (좌측 상단)
ax.legend(loc='upper left')

print("\n--- 회귀직선을 포함한 산점도를 표시합니다. ---")
plt.show()


# --------------------------------------------------------------------------------------
# [9] 시각화: 히트맵 (Heatmap) - 2차원 히스토그램
# --------------------------------------------------------------------------------------
# 데이터가 많을 때 점들이 겹쳐서 분포를 알기 어려울 경우, 영역별 밀도를 색상으로 표현합니다.

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111)

# hist2d: 2차원 히스토그램 그리기
# bins=[9, 8]: 영어(X)는 9개 구간, 수학(Y)은 8개 구간으로 나눔
# range=[(35, 80), (55, 95)]: X, Y축의 표시 범위 지정
c = ax.hist2d(english_scores, math_scores,
              bins=[9, 8], range=[(35, 80), (55, 95)])

ax.set_xlabel('english')
ax.set_ylabel('mathematics')

# c[1]: X축 구간 경계값들, c[2]: Y축 구간 경계값들
# 눈금을 구간 경계에 맞춰 설정
ax.set_xticks(c[1])
ax.set_yticks(c[2])

# 컬러바(Color Bar) 표시: 색상이 의미하는 빈도수를 나타냄
fig.colorbar(c[3], ax=ax)

print("\n--- 히트맵을 표시합니다. ---")
plt.show()


# --------------------------------------------------------------------------------------
# [10] 앤스콤의 4분할 (Anscombe's Quartet)
# --------------------------------------------------------------------------------------
# 기술통계량(평균, 분산, 상관계수 등)은 동일하지만, 분포나 그래프 모양은 완전히 다른 4개의 데이터셋입니다.
# 시각화의 중요성을 보여주는 대표적인 예시입니다.

# npy 파일 로드 (이전 실행 오류 수정을 위해 절대 경로 사용)
# 파일이 현재 스크립트와 같은 경로에 있다고 가정합니다.
anscombe_file = os.path.join(path, 'anscombe.npy')

if os.path.exists(anscombe_file):
    anscombe_data = np.load(anscombe_file)
    print("\n--- Anscombe 데이터 shape ---")
    print(anscombe_data.shape) # (4, 11, 2) -> 4개의 데이터셋, 각 11개의 데이터, (x, y) 2차원

    print("\n--- 첫 번째 데이터셋 샘플 (Data 1) ---")
    print(anscombe_data[0])
    
    # ----------------------------------------------------------------------------------
    # [10-1] 데이터셋 통계량 비교 (DataFrame 생성)
    # ----------------------------------------------------------------------------------
    # 4개의 데이터셋에 대해 평균, 분산, 상관계수, 회귀직선 식을 계산하고 비교합니다.
    # 결과를 한눈에 보기 위해 Pandas DataFrame을 활용합니다.
    
    # DataFrame의 행 인덱스(Row Index)를 미리 정의합니다.
    # 각 통계 항목(평균, 분산 등)이 행으로 들어갑니다.
    stats_df = pd.DataFrame(index=['X_mean', 'X_variance', 'Y_mean',
                                   'Y_variance', 'X&Y_correlation',
                                   'X&Y_regression line'])
    
    # anscombe_data 리스트를 순회하며 각 데이터셋(d1, d2, d3, d4)의 통계량을 계산합니다.
    # enumerate를 사용하여 인덱스(i)와 데이터(data)를 동시에 가져옵니다.
    for i, data in enumerate(anscombe_data):
        dataX = data[:, 0] # 현재 데이터셋의 X값들 (모든 행, 0번째 열)
        dataY = data[:, 1] # 현재 데이터셋의 Y값들 (모든 행, 1번째 열)
        
        # np.polyfit(x, y, 1): 1차 회귀식(y = ax + b)의 계수를 계산합니다.
        # poly_fit[0]은 기울기, poly_fit[1]은 절편입니다.
        poly_fit = np.polyfit(dataX, dataY, 1)
        
        # 계산된 통계량들을 문자열로 포맷팅하여 리스트에 담습니다.
        # f'{값:.2f}': 소수점 둘째 자리까지 반올림하여 표시
        stats_values = [
            f'{np.mean(dataX):.2f}',                # X의 평균
            f'{np.var(dataX):.2f}',                 # X의 분산
            f'{np.mean(dataY):.2f}',                # Y의 평균
            f'{np.var(dataY):.2f}',                 # Y의 분산
            f'{np.corrcoef(dataX, dataY)[0, 1]:.2f}', # 상관계수
            f'{poly_fit[1]:.2f}+{poly_fit[0]:.2f}x'   # 회귀직선 식 (절편+기울기x)
        ]
        
        # DataFrame에 새로운 컬럼(data1, data2...)을 추가합니다.
        # stats_df의 각 행 순서에 맞춰서 값이 들어갑니다.
        stats_df[f'data{i+1}'] = stats_values
    
    print("\n--- 4개 데이터셋의 통계량 비교 표 ---")
    print(stats_df)
    print("\n[알림] 위 표를 보면 4개 데이터셋의 평균, 분산, 상관계수, 회귀선이 모두 거의 동일합니다.")


    # ----------------------------------------------------------------------------------
    # [10-2] 앤스콤의 4분할 시각화 (Visualization)
    # ----------------------------------------------------------------------------------
    # 수치상은 같아도 실제 데이터 분포는 완전히 다름을 시각적으로 확인합니다.
    # 2행 2열(총 4개)의 서브플롯(Subplot)을 생성하여 각각 그립니다.
    
    # plt.subplots: Figure와 Axes 객체들을 동시에 생성함
    # nrows=2, ncols=2: 2x2 그리드
    # figsize=(10, 10): 전체 그림 크기 (가로 10인치, 세로 10인치)
    # sharex=True, sharey=True: 모든 서브플롯이 동일한 X축, Y축 눈금을 공유함 (비교를 위해 필수)
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 10),
                             sharex=True, sharey=True)
    
    # 회귀직선을 그리기 위한 X축 데이터 생성 (구간: 0 ~ 30)
    # 0부터 30까지 100개의 점을 생성하여 부드러운 직선을 그림
    xs = np.linspace(0, 30, 100)
    
    # 각 데이터셋에 대해 반복하며 그래프 그리기
    for i, data in enumerate(anscombe_data):
        # 1. 회귀식 계산 및 함수 생성 (그래프 위에 그릴 직선)
        poly_fit = np.polyfit(data[:,0], data[:,1], 1)
        poly_1d = np.poly1d(poly_fit) # 계수를 함수로 변환 (x를 넣으면 y가 나오도록)
        ys = poly_1d(xs)              # x값들에 대한 예측 y값 계산
        
        # 2. 현재 그릴 서브플롯(Axes) 선택 로직
        # i // 2 : 행 인덱스 (몫) -> 0, 0, 1, 1
        # i % 2  : 열 인덱스 (나머지) -> 0, 1, 0, 1
        ax = axes[i//2, i%2]
        
        # 3. 축 범위 고정
        # 모든 그래프가 같은 범위를 보여줘야 데이터 분포 차이가 확연히 보임
        ax.set_xlim([4, 20])
        ax.set_ylim([3, 13])
        
        # 4. 그래프 제목 설정
        ax.set_title(f'data{i+1}')
        
        # 5. 산점도(Scatter Plot) 그리기: 실제 데이터 점들을 찍음
        ax.scatter(data[:,0], data[:,1])
        
        # 6. 회귀직선 그리기: 계산된 추세선을 그림
        # color='gray': 회색 실선으로 표시하여 데이터 점을 가리지 않게 함
        ax.plot(xs, ys, color='gray')

    # 그래프 사이의 간격을 자동으로 조정하여 제목이나 축이 겹치지 않게 함
    plt.tight_layout()
    
    print("\n--- 앤스콤의 4분할 그래프를 표시합니다. ---")
    plt.show()

else:
    print(f"\n[Error] '{anscombe_file}' 파일을 찾을 수 없습니다. 경로를 확인해주세요.")