import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# 한글 폰트 설정 (Windows)
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

def main():
    # 현재 실행 중인 파일의 전체 경로를 역슬래시("\\") 기준으로 분리하여 리스트로 만듭니다.
    file_list = __file__.split("\\") 
    # 파일 경로에서 리스트의 마지막 요소(파일 이름)를 "cctv_result.csv"로 대체하여
    # 로드할 CSV 파일의 전체 경로를 만듭니다. (동일 디렉토리에 있다고 가정)
    load_file = __file__.replace(file_list[-1], "data\서울시 부동산 실거래가 정보(2022~2025).csv")
    
    try:
        df = pd.read_csv(load_file, encoding='cp949', low_memory=False)
    except UnicodeDecodeError:
        df = pd.read_csv(load_file, encoding='utf-8', low_memory=False)

    # 데이터 전처리
    # 계약일을 datetime으로 변환 (YYYYMMDD 형식)
    df['계약일'] = pd.to_datetime(df['계약일'], format='%Y%m%d', errors='coerce')
    
    # 2022년 ~ 2025년 데이터 필터링
    df = df[df['계약일'].dt.year.isin([2022, 2023, 2024, 2025])]
    
    # 물건금액(만원) 전처리: 쉼표 제거 및 숫자로 변환
    if df['물건금액(만원)'].dtype == 'object':
        df['물건금액(만원)'] = df['물건금액(만원)'].astype(str).str.replace(',', '').astype(float)
    
    # 월별 평균 거래금액 집계
    df['계약월'] = df['계약일'].dt.to_period('M')
    monthly_prices = df.groupby('계약월')['물건금액(만원)'].mean()
    
    # Series를 DataFrame으로 변환 및 인덱스(Period)를 timestamp로 변환하여 플로팅 준비
    monthly_prices.index = monthly_prices.index.to_timestamp()
    
    # 시각화
    plt.figure(figsize=(12, 6))
    plt.plot(monthly_prices.index, monthly_prices.values, marker='o', linestyle='-', color='purple', label='월별 평균 거래금액')
    
    # 그래프 꾸미기
    plt.title('서울시 부동산 월별 평균 실거래가 추이 (2022~2025)', fontsize=16)
    plt.xlabel('년-월', fontsize=12)
    plt.ylabel('평균 거래금액 (만원)', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # X축 포맷 설정
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=3)) # 3개월 간격
    plt.gcf().autofmt_xdate() # X축 라벨 회전
    
    # 주요 구간 강조 (2023 하락, 2024 반등, 2025 안정화)
    # 2023년 하락 구간 (파란색 배경)
    plt.axvspan(pd.Timestamp('2023-01-01'), pd.Timestamp('2023-12-31'), color='blue', alpha=0.1, label='2023년 (하락)')
    
    # 2024년 반등 구간 (빨간색 배경) - 부동산에서 상승은 통상 붉은색
    plt.axvspan(pd.Timestamp('2024-01-01'), pd.Timestamp('2024-12-31'), color='red', alpha=0.1, label='2024년 (소폭 반등)')
    
    # 2025년 안정화 구간 (녹색 배경)
    plt.axvspan(pd.Timestamp('2025-01-01'), pd.Timestamp('2025-12-31'), color='green', alpha=0.1, label='2025년 (안정화)')

    plt.legend()
    plt.tight_layout()
    
    # 그래프 확인 (저장)
    output_path = __file__.replace(file_list[-1], "price_trend.png")
    plt.savefig(output_path)
    print(f"Graph saved to {output_path}")

if __name__ == "__main__":
    print("Script started...")
    try:
        main()
        print("Script finished successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")