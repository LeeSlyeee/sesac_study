import pandas as pd
import os

# --- 1. 파일 경로 정의 ---
# 각 데이터 파일의 상대 경로를 정의합니다.
mart_path = 'mini_project/대형마트_공공데이터/대형마트_진짜_최종-sig.csv'
hospital_path = 'mini_project/병원_공공데이터/최종_노원구_강동구_성북구_병원데이터-sig.csv'
subway_path = 'mini_project/지하철_공공데이터/지하철_진짜_최종-sig.csv'

# --- 2. 데이터 로드 및 기본 검사 함수 정의 ---
def load_and_inspect(path, name):
    """
    지정된 경로에서 CSV 파일을 불러오고 파일 존재 여부 및 로드 오류를 확인합니다.

    Args:
        path (str): CSV 파일 경로
        name (str): 데이터셋 이름 (출력용)

    Returns:
        pd.DataFrame or None: 성공적으로 로드된 데이터프레임 또는 실패 시 None
    """
    print(f"\n--- 파일을 불러오고 있습니다. {name} ---")
    # 파일 경로에 파일이 실제로 존재하는지 확인
    if not os.path.exists(path):
        print(f"파일을 찾을 수 없음: {path}")
        return None
    try:
        # CSV 파일 로드. 'utf-8-sig' 인코딩은 BOM(Byte Order Mark)이 있는 경우를 처리하여
        # 한글 깨짐 및 특정 헤더 문제를 방지하는 데 유용합니다.
        df = pd.read_csv(path, encoding='utf-8-sig')
        # 데이터프레임이 성공적으로 로드되었는지 확인 (선택적)
        # print(f"{name} 데이터 로드 성공. Shape: {df.shape}")
        return df
    except Exception as e:
        # 파일 로드 중 발생한 모든 예외(예: 인코딩, 파일 형식 등)를 처리
        print(f"에러 {name}: {e}")
        return None

# --- 3. 데이터 로드 실행 ---
df_mart = load_and_inspect(mart_path, "Mart")
df_hospital = load_and_inspect(hospital_path, "Hospital")
df_subway = load_and_inspect(subway_path, "Subway")

# 모든 데이터프레임이 성공적으로 로드되었는지 확인
if df_mart is None or df_hospital is None or df_subway is None:
    print("모든 데이터를 읽는데 실패했습니다. 스크립트를 종료합니다.")
    exit() # 하나라도 로드 실패 시 스크립트 종료

# --- 4. 데이터프레임 전처리 및 컬럼 표준화 ---
# 데이터프레임의 컬럼 개수가 동일하다고 가정하고, 헤더 인코딩 문제로 인해
# 컬럼 이름이 불규칙할 수 있는 상황에 대비하여 인덱스 기반으로 컬럼 이름을 표준화합니다.
standard_columns = ['Unnamed', '자치구', '법정동', 'Count']

# 마트 데이터프레임 컬럼 표준화
if df_mart.shape[1] == 4:
    df_mart.columns = standard_columns # 표준 컬럼 이름 적용
    df_mart = df_mart.rename(columns={'Count': '마트개수'}) # 'Count' 컬럼을 '마트개수'로 변경
else:
    # 컬럼 개수가 4개가 아닌 경우 경고 메시지 출력
    print(f"경고: 마트 데이터에 {df_mart.shape[1]} 열이 있으며, 예상치는 4입니다.. 컬럼 이름 변경 건너뜀.")

# 병원 데이터프레임 컬럼 표준화
if df_hospital.shape[1] == 4:
    df_hospital.columns = standard_columns
    df_hospital = df_hospital.rename(columns={'Count': '병원수'})

# 지하철 데이터프레임 컬럼 표준화
if df_subway.shape[1] == 4:
    df_subway.columns = standard_columns
    df_subway = df_subway.rename(columns={'Count': '역개수'})

# --- 5. 필요한 컬럼 선택 ---
# 병합 키가 될 '자치구', '법정동'과 개수 정보만 선택하여 데이터프레임 단순화
df_mart = df_mart[['자치구', '법정동', '마트개수']]
df_hospital = df_hospital[['자치구', '법정동', '병원수']]
df_subway = df_subway[['자치구', '법정동', '역개수']]

# --- 6. 데이터 병합 (Merge) ---
print("\n데이터 병합 중...")
try:
    # 1. 마트와 병원 데이터 병합: '자치구'와 '법정동'을 기준으로 `outer` join 수행
    # `outer` join은 한쪽 데이터에만 존재하는 행(동네)도 모두 포함합니다.
    df_merged = pd.merge(df_mart, df_hospital, on=['자치구', '법정동'], how='outer')
    
    # 2. 병합된 결과에 지하철 데이터 병합: 동일한 기준 및 방식으로 `outer` join 수행
    df_merged = pd.merge(df_merged, df_subway, on=['자치구', '법정동'], how='outer')
except Exception as e:
    # 병합 중 발생한 예외 처리
    print(f"데이터 병합 중 에러: {e}")
    exit()

# --- 7. 결측치 처리 및 데이터 타입 변환 ---
# 'outer' join으로 인해 데이터가 없는 동네는 NaN(Not a Number, 결측치)이 됩니다.
# NaN 값을 0으로 채웁니다. (시설이 없는 경우 0개)
df_merged = df_merged.fillna(0)

# 개수 컬럼들을 정수형(int)으로 변환
for col in ['마트개수', '병원수', '역개수']:
    df_merged[col] = df_merged[col].astype(int)

# --- 8. 총 시설 수 계산 ---
# 각 동네별로 마트, 병원, 지하철역의 총 개수를 합산하여 '총_시설_수' 컬럼 생성
df_merged['총_시설_수'] = df_merged['마트개수'] + df_merged['병원수'] + df_merged['역개수']

# --- 9. 최대값 동네 찾기 (Top 1) ---
# 각 시설별 및 총 시설 수의 최대값을 가진 행(동네 정보)을 찾습니다.
# idxmax()는 최대값이 있는 행의 인덱스를 반환합니다.
top_mart = df_merged.loc[df_merged['마트개수'].idxmax()]
top_hospital = df_merged.loc[df_merged['병원수'].idxmax()]
top_subway = df_merged.loc[df_merged['역개수'].idxmax()]
top_total = df_merged.loc[df_merged['총_시설_수'].idxmax()]

# --- 10. 분석 결과 출력 ---
print("\n=== 분석 결과 ===")
print(f"근처의 마트: {top_mart['자치구']} {top_mart['법정동']} ({top_mart['마트개수']}개)")
print(f"근처의 병원: {top_hospital['자치구']} {top_hospital['법정동']} ({top_hospital['병원수']}개)")
print(f"근처의 지하철역: {top_subway['자치구']} {top_subway['법정동']} ({top_subway['역개수']}개)")
print(f"근처의 총 시설 수: {top_total['자치구']} {top_total['법정동']} ({top_total['총_시설_수']}개)")

# --- 11. 결과 저장 ---
output_path = 'mini_project/Data/동별_주요시설_현황.csv' # 최종 병합 데이터 저장 경로
# 출력 디렉토리가 없으면 생성 (exist_ok=True는 이미 있어도 오류 발생시키지 않음)
os.makedirs(os.path.dirname(output_path), exist_ok=True)
# 병합된 결과를 CSV 파일로 저장 (인덱스 제외, 'utf-8-sig' 인코딩 사용)
df_merged.to_csv(output_path, index=False, encoding='utf-8-sig')
print(f"\n병합된 데이터는 {output_path}에 저장되었습니다.")

# --- 12. 총 시설 기준 상위 5개 동네 출력 및 저장 ---
print("\n총 시설 기준 상위 5개 동네:")
# '총_시설_수'를 기준으로 내림차순 정렬하고 상위 5개 행만 선택
df_top5 = df_merged.sort_values(by='총_시설_수', ascending=False).head(5)
# 상위 5개 결과를 별도의 CSV 파일로 저장
df_top5.to_csv('mini_project/Data/동별_주요시설_현황_top5.csv', index=False, encoding='utf-8-sig')
# 상위 5개 데이터프레임 출력
print(df_top5)