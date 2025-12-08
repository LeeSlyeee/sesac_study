# --- 1. 라이브러리 임포트 ---
from selenium import webdriver # 웹 자동화 및 동적 크롤링을 위한 라이브러리
from selenium.webdriver.chrome.service import Service as ChromeService # 크롬 드라이버 서비스를 설정
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 다운로드/설치 및 관리
from selenium.webdriver.common.by import By # Selenium에서 요소를 찾을 때 사용할 전략(CSS, ID 등)
from selenium.webdriver.support.ui import WebDriverWait # 명시적 대기(Explicit Wait)를 위한 클래스
from selenium.webdriver.support import expected_conditions as EC # 명시적 대기에 사용할 조건들을 정의
import pandas as pd # 데이터 분석 및 조작을 위한 핵심 라이브러리 (DataFrame 생성/저장에 사용)
import matplotlib.pyplot as plt # 데이터 시각화를 위한 기본 라이브러리
import seaborn as sns # Matplotlib 기반의 통계 데이터 시각화 라이브러리
import korean # (커스텀 라이브러리)


# --- 2. 전역 리스트 초기화 ---
# 크롤링한 데이터를 저장할 전역 리스트를 정의합니다.
category_list = []
title_list = []
subscribes_list = []


# --- 3. 데이터 수집 함수 정의 (get_data) ---
def get_data(page):
    # Chrome WebDriver를 초기화하고 드라이버를 자동으로 설치/관리합니다.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 1. 페이지 접속 URL 조합 및 이동
    # 현재 페이지 번호(page)를 URL에 삽입하여 접속할 주소를 만듭니다.
    target_url = "https://youtube-rank.com/board/bbs/board.php?bo_table=youtube&page=" + str(page)
    driver.get(target_url)
    
    # 2. 명시적 대기 (Explicit Wait) 적용
    # 데이터가 완전히 로드될 때까지 기다리는 로직입니다.
    try:
        # 최대 10초 동안 대기합니다.
        WebDriverWait(driver, 10).until(
            # 'form table tbody tr' CSS 선택자에 해당하는 엘리먼트(테이블 행, 즉 채널 정보)가
            # DOM에 로드될 때까지 기다립니다.
            EC.presence_of_element_located((By.CSS_SELECTOR, 'form table tbody tr'))
        )
    except Exception as e:
        # 10초 내에 엘리먼트가 로드되지 않으면 에러 메시지를 출력하고 함수를 종료합니다.
        print(f"페이지 로드 대기 중 에러 발생: {e}")
        driver.quit()
        return # 에러 발생 시 현재 함수 호출을 즉시 종료
        
    # 3. 스크롤 다운 (Optional)
    # JavaScript 명령을 실행하여 페이지를 가장 아래로 스크롤합니다.
    # 동적 로딩되는 데이터가 있을 경우 모두 로드되도록 합니다.
    driver.execute_script("window.scrollTo(0, 99999);")
    
    # 4. 데이터 엘리먼트 추출
    # CSS 선택자를 이용해 차트 테이블의 각 행(<tr>, 하나의 채널 정보) 엘리먼트들을 모두 찾습니다.
    articles = driver.find_elements(By.CSS_SELECTOR,'form table tbody tr') 
    
    # 임시 리스트 초기화 (현재 페이지에서 추출한 데이터를 저장하기 위함)
    tmp_category = []
    tmp_title = []
    tmp_subscribes = []
    
    # 각 채널 정보 행(row)을 순회하며 데이터를 추출합니다.
    for row in articles:
        try:
            # 카테고리 추출
            # 현재 행 내에서 '.subject p.category' 엘리먼트를 찾습니다.
            category_element = row.find_elements(By.CSS_SELECTOR, '.subject p.category')
            if category_element:
                tmp_category.append(category_element[0].text.strip())
            else:
                tmp_category.append("해당 정보 없음")
            
            # 타이틀(채널명) 추출
            # 현재 행 내에서 '.subject a' 엘리먼트를 찾습니다.
            title_element = row.find_elements(By.CSS_SELECTOR, '.subject a')
            if title_element:
                tmp_title.append(title_element[0].text.strip())
            else:
                tmp_title.append("해당 정보 없음")
            
            # 구독자수 추출
            # 현재 행 내에서 '.subscriber_cnt' 엘리먼트를 찾습니다.
            subscribes_element = row.find_elements(By.CSS_SELECTOR, '.subscriber_cnt')
            if subscribes_element:
                tmp_subscribes.append(subscribes_element[0].text.strip())
            else:
                tmp_subscribes.append("해당 정보 없음")
                
        except Exception as e:
            # 개별 데이터 추출 중 예상치 못한 에러가 발생했을 때 처리합니다.
            print(f"데이터 추출 중 에러 발생: {e}")


    # 전역 리스트에 임시 리스트의 결과를 병합(extend)합니다.
    global category_list, title_list, subscribes_list
    category_list.extend(tmp_category)
    title_list.extend(tmp_title)
    subscribes_list.extend(tmp_subscribes)
    
    print("end :", page)
    # 작업이 완료되면 WebDriver를 종료하여 브라우저 창을 닫습니다.
    driver.quit()
    
    
# --- 4. 데이터 수집 루프 실행 ---
# for 루프를 사용하여 1페이지부터 4페이지까지 데이터를 순차적으로 수집합니다.
for page in range(1, 5):
    get_data(page)
    
    
# --- 5. Pandas 데이터프레임 생성 및 저장 ---

# 수집된 리스트를 딕셔너리로 구성합니다.
youtube_rank_data = {
    '카테고리' : category_list,
    '채널명' : title_list,
    '구독자수' : subscribes_list
}

# 딕셔너리를 Pandas DataFrame으로 변환합니다.
df_youtube_rank_data = pd.DataFrame(youtube_rank_data)
# DataFrame의 인덱스를 1부터 시작하도록 변경합니다.
df_youtube_rank_data.index += 1
# 인덱스를 새로운 컬럼으로 추가합니다. (기존 인덱스 드롭하지 않음)
df_youtube_rank_data.reset_index(drop=False, inplace=True)
# 새로 생성된 'index' 컬럼의 이름을 '순위'로 변경합니다.
df_youtube_rank_data.rename(columns={'index' : '순위'}, inplace=True)

# 최종 DataFrame을 Excel 파일로 저장합니다.
df_youtube_rank_data.to_excel('__05.youtube_rank_data.xlsx', index=False)




df_top100 = df_youtube_rank_data[df_youtube_rank_data['순위'] <= 100]

category_counts = df_top100['카테고리'].value_counts()

category_percentages = (category_counts / category_counts.sum()) * 100



plt.figure(figsize=(10, 10)) # 그래프 크기 설정

# 파이 그래프 그리기
# labels: 카테고리 이름
# autopct: 각 조각의 비율을 소수점 첫째 자리까지 표시 ('%.1f%%')
# startangle: 시작 각도 (90도로 설정하여 첫 번째 조각이 위에서 시작)
# shadow: 그림자 효과
wedges, texts, autotexts = plt.pie(
    category_counts,
    labels=category_counts.index,
    autopct='%.1f%%',
    startangle=90,
    pctdistance=0.85, # 비율 텍스트가 표시될 위치
    wedgeprops={'edgecolor': 'black'} # 조각 경계선 설정
)

# 그래프 제목 설정
plt.title('유튜브 순위 100위권 카테고리별 비중', fontsize=18)

# 범례 추가 (옵션)
# plt.legend(wedges, category_counts.index,
#            title="카테고리",
#            loc="center left",
#            bbox_to_anchor=(1, 0, 0.5, 1))

# 텍스트 크기 및 색상 조정
for autotext in autotexts:
    autotext.set_color('white')
    autotext.set_fontsize(10)
for text in texts:
    text.set_fontsize(10)


# 파이 차트를 원형으로 유지
plt.axis('equal') 

# 그래프 저장 및 출력
plt.savefig('__06.youtube_top100_category_pie.png')
print("\n파이 그래프가 '__06.youtube_top100_category_pie.png'로 저장되었습니다.")
plt.show() # 그래프 출력

# --- 5. 데이터프레임 출력 (참고용) ---
print("\n--- 상위 100위 카테고리별 집계 결과 (%) ---")
print(category_percentages.round(2).to_string())