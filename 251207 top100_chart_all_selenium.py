# --- 1. 라이브러리 임포트 ---
import webbrowser # 웹 브라우저를 제어하는 모듈 (현재 코드에서는 미사용)
import os         # 운영체제 기능을 제어하는 모듈 (현재 코드에서는 미사용)
import requests   # HTTP 요청을 보내는 데 사용되는 라이브러리 (정적 크롤링용이지만 현재 코드에서는 미사용됨)
import bs4        # Beautiful Soup 라이브러리 (BeautifulSoup 클래스를 위해 임포트)
from bs4 import BeautifulSoup # HTML 및 XML 파일에서 데이터를 추출하는 핵심 클래스 (현재 코드에서는 미사용)
from urllib.request import urlopen # URL을 열기 위한 모듈 (현재 코드에서는 미사용)
import pandas as pd # 데이터 분석 및 조작을 위한 핵심 라이브러리 (DataFrame 생성/병합/저장에 사용)
import matplotlib.pyplot as plt # 데이터 시각화를 위한 기본 라이브러리
import seaborn as sns # Matplotlib 기반의 통계 데이터 시각화 라이브러리
import numpy as np # 과학 계산을 위한 라이브러리 (현재 코드에서는 미사용)
import korean # (커스텀 또는 미사용 라이브러리)
from selenium import webdriver # 웹 자동화 및 동적 크롤링을 위한 라이브러리
from selenium.webdriver.chrome.service import Service as ChromeService # 크롬 드라이버 서비스를 설정
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 다운로드/설치
from selenium.webdriver.common.by import By # Selenium에서 요소를 찾을 때 사용할 전략(CSS, ID 등)

# ---------------------------------------------------
# ## 2. URL 및 데이터 리스트 정의
# ---------------------------------------------------

# --- 1.1. 크롤링 대상 URL 정의 ---
melon_url = 'https://www.melon.com/chart/'
bugs_url = 'https://music.bugs.co.kr/chart/'
# 지니 URL (페이지 번호는 함수 내에서 조합)
genie_url = 'https://www.genie.co.kr/chart/top200/?ditc=D&ymd=20251206&hh=16&rtm=Y&pg='


# 멜론 크롤링 결과를 저장할 전역 리스트를 초기화합니다.
melon_song_title = []
melon_song_artist = []


# ---------------------------------------------------
# ## 3. 멜론 차트 크롤링 (Selenium)
# ---------------------------------------------------

def get_melon_music():
    # Chrome WebDriver를 초기화하고 드라이버를 자동으로 설치/관리합니다.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 멜론 차트 페이지로 이동합니다.
    driver.get(melon_url)
    
    # CSS 선택자를 이용해 차트 테이블의 각 행(<tr>, 하나의 곡 정보)을 찾습니다.
    music_info = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    
    # 1. 곡 제목 추출
    for title_container in music_info:
        try:
            # 현재 행 내에서 곡 제목 엘리먼트(.ellipsis.rank01)를 찾습니다.
            tmp_elements = title_container.find_elements(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank01')
            
            if tmp_elements:
                # 엘리먼트의 텍스트를 추출합니다.
                title = tmp_elements[0].text.strip()
            else:
                title = "해당 정보 없음"
            
            melon_song_title.append(title)
        except:
            print("멜론 제목 추출 중 에러 발생!")
            
            
    # 2. 아티스트 이름 추출
    for artist_container in music_info:
        try:
            # 현재 행 내에서 아티스트 이름 엘리먼트(.ellipsis.rank02 a)를 찾습니다.
            tmp_elements = artist_container.find_elements(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank02 a')
            
            if tmp_elements:
                # 엘리먼트의 텍스트를 추출합니다.
                artist = tmp_elements[0].text.strip()
            else:
                artist = "해당 정보 없음"
            
            melon_song_artist.append(artist)
        except:
            print("멜론 아티스트 추출 중 에러 발생!")
            
    # 작업이 완료되면 WebDriver를 종료합니다.
    driver.quit()

# 멜론 크롤링 함수를 실행합니다.
get_melon_music()

# 멜론 데이터를 딕셔너리로 구성합니다.
melon_data = {
    '곡_제목': melon_song_title,
    '가수': melon_song_artist
}

# 딕셔너리를 Pandas DataFrame으로 변환합니다.
df_melon_chart = pd.DataFrame(melon_data)

# DataFrame의 인덱스를 1부터 시작하도록 변경합니다.
df_melon_chart.index += 1
# 새로운 인덱스를 'index' 컬럼으로 추가하고 원본에 반영합니다.
df_melon_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 4. 벅스 차트 크롤링 (Selenium)
# ---------------------------------------------------

# 벅스 크롤링 결과를 저장할 전역 리스트를 초기화합니다.
bugs_song_title = []
bugs_song_artist = []


def get_bugs_music():
    # Chrome WebDriver 초기화
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 벅스 차트 페이지로 이동합니다.
    driver.get(bugs_url)
    
    # CSS 선택자를 이용해 차트 테이블의 각 행(<tr>)을 찾습니다.
    music_info = driver.find_elements(By.CSS_SELECTOR, 'table.list.trackList.byChart tbody tr')
    
    # 1. 곡 제목 추출
    for title_container in music_info:
        try:
            # 현재 행 내에서 곡 제목 엘리먼트(p.title a)를 찾습니다.
            tmp_elements = title_container.find_elements(By.CSS_SELECTOR, 'p.title a')
            
            if tmp_elements:
                title = tmp_elements[0].text.strip()
            else:
                title = "해당 정보 없음"
            
            bugs_song_title.append(title)
        except:
            print("벅스 제목 추출 중 에러 발생!")
            
            
    # 2. 아티스트 이름 추출
    for artist_container in music_info:
        try:
            # 현재 행 내에서 아티스트 이름 엘리먼트(p.artist a)를 찾습니다.
            tmp_elements = artist_container.find_elements(By.CSS_SELECTOR, 'p.artist a')
            
            if tmp_elements:
                # 벅스는 아티스트 이름 외 다른 텍스트가 있을 수 있으므로 첫 번째 요소만 선택합니다.
                artist = tmp_elements[0].text.strip()
            else:
                artist = "해당 정보 없음"
            
            bugs_song_artist.append(artist)
        except:
            print("벅스 아티스트 추출 중 에러 발생!")
            
    # WebDriver 종료
    driver.quit()

# 벅스 크롤링 함수를 실행합니다.
get_bugs_music()

# 벅스 데이터를 딕셔너리로 구성하고 DataFrame으로 변환합니다.
bugs_data = {
    '곡_제목': bugs_song_title,
    '가수': bugs_song_artist
}

df_bugs_chart = pd.DataFrame(bugs_data)

# 인덱스를 1부터 시작하도록 설정하고 'index' 컬럼을 추가합니다.
df_bugs_chart.index += 1
df_bugs_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 5. 지니 차트 크롤링 (Selenium)
# ---------------------------------------------------

# 지니 크롤링 결과를 저장할 전역 리스트를 초기화합니다.
genie_song_title = []
genie_song_artist = []


def get_genie_music(page):
    # Chrome WebDriver 초기화
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 지니 차트 URL에 페이지 번호를 붙여 접속합니다.
    driver.get(genie_url + str(page))
    
    # CSS 선택자를 이용해 음악 정보(td.info) 엘리먼트들을 찾습니다.
    music_info = driver.find_elements(By.CSS_SELECTOR,'table.list-wrap td.info')
    
    # 1. 곡 제목 추출
    for title_container in music_info:
        try:
            # 현재 info 엘리먼트 내에서 곡 제목 엘리먼트(a.title)를 찾습니다.
            tmp_elements = title_container.find_elements(By.CSS_SELECTOR, 'a.title')
            
            if tmp_elements:
                title = tmp_elements[0].text.strip()
            else:
                title = "해당 정보 없음"
            
            genie_song_title.append(title)
        except:
            print("지니 제목 추출 중 에러 발생!")
            
            
    # 2. 아티스트 이름 추출
    for artist_container in music_info:
        try:
            # 현재 info 엘리먼트 내에서 아티스트 엘리먼트(a.artist)를 찾습니다.
            tmp_elements = artist_container.find_elements(By.CSS_SELECTOR, 'a.artist')
            
            if tmp_elements:
                artist = tmp_elements[0].text.strip()
            else:
                artist = "해당 정보 없음"
            
            genie_song_artist.append(artist)
        except:
            print("지니 아티스트 추출 중 에러 발생!")
            
    print("end :", page)
    # WebDriver 종료
    driver.quit()


# 1페이지와 2페이지를 순회하며 (총 100위까지) 지니 차트를 크롤링합니다.
for page in range(1, 3):
    get_genie_music(page)
    
    
# 지니 데이터를 딕셔너리로 구성하고 DataFrame으로 변환합니다.
genie_data = {
    '곡_제목': genie_song_title,
    '가수': genie_song_artist
}

df_genie_chart = pd.DataFrame(genie_data)

# 인덱스를 1부터 시작하도록 설정하고 'index' 컬럼을 추가합니다.
df_genie_chart.index += 1
df_genie_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 6. 데이터프레임 저장, 컬럼명 변경 및 통합
# ---------------------------------------------------

# --- 6.1. 개별 데이터프레임을 Excel 파일로 저장 ---
# 각 차트별 데이터를 개별 Excel 파일로 저장합니다.
df_melon_chart.to_excel('__01.melon_chart.xlsx', index=False)
df_bugs_chart.to_excel('__02.bugs_chart.xlsx', index=False)
df_genie_chart.to_excel('__03.genie_chart.xlsx', index=False)


# --- 6.2. 컬럼명 정의 및 변경 ---
# 병합 시 충돌을 피하고 출처를 명확히 하기 위해 컬럼 이름을 변경할 딕셔너리를 정의합니다.
melon_columns = {'index' : '순위', '곡_제목' : '곡 제목(멜론)', '가수' : '아티스트(멜론)'}
bugs_columns = {'index' : '순위', '곡_제목' : '곡 제목(벅스)', '가수' : '아티스트(벅스)'}
genie_columns = {'index' : '순위', '곡_제목' : '곡 제목(지니)', '가수' : '아티스트(지니)'}

# DataFrame의 컬럼 이름을 변경합니다.
df_melon_chart.rename(columns=melon_columns, inplace=True)
df_bugs_chart.rename(columns=bugs_columns, inplace=True)
df_genie_chart.rename(columns=genie_columns, inplace=True)


# --- 6.3. 데이터프레임 통합 (Pandas merge) ---

# 1. 멜론 차트(df_melon_chart)를 기준으로 벅스 차트(df_bugs_chart)를 '순위' 열을 키로 좌측 병합 (LEFT JOIN).
df_integration_chart = pd.merge(df_melon_chart, df_bugs_chart, on='순위', how='left')

# 2. 통합된 데이터프레임에 지니 차트 정보(df_genie_chart)를 '순위' 열을 키로 좌측 병합합니다.
df_integration_chart = pd.merge(df_integration_chart, df_genie_chart, on='순위', how='left')


# --- 6.4. 최종 통합 데이터프레임을 Excel 파일로 저장 ---
# 모든 차트 정보가 순위별로 병합된 파일을 저장합니다.
df_integration_chart.to_excel('__04.integration_chart.xlsx', index=False) # index=False로 순위(index) 열은 제외하고 저장


# ---------------------------------------------------
# ## 7. 데이터 분석 및 시각화
# ---------------------------------------------------

# --- 7.1. 통합 데이터프레임에서 곡 정보 추출 및 결합 ---

# 멜론 DataFrame에서 곡 제목과 아티스트 컬럼을 추출하여 [제목, 아티스트] 리스트로 변환합니다.
melon_songs = df_melon_chart[['곡 제목(멜론)', '아티스트(멜론)']].values.tolist()
# 벅스 차트 정보 추출
bugs_songs = df_bugs_chart[['곡 제목(벅스)', '아티스트(벅스)']].values.tolist()
# 지니 차트 정보 추출
genie_songs = df_genie_chart[['곡 제목(지니)', '아티스트(지니)']].values.tolist()


# 모든 세 차트의 곡 정보를 하나의 리스트로 통합합니다.
all_songs = melon_songs + bugs_songs + genie_songs

# --- 7.2. 등장 횟수 집계 ---

# 곡 제목과 아티스트를 결합한 문자열을 키로 사용하여 각 곡의 등장 횟수를 계산할 딕셔너리를 초기화합니다.
song_counts = {}
for title, artist in all_songs:
    # 곡과 아티스트를 묶어 고유한 키를 생성합니다. (예: "Ditto - NewJeans")
    key = f"{title} - {artist}"
    # 딕셔너리에서 해당 키의 값을 가져오고 (없으면 0), 1을 더해 업데이트합니다.
    song_counts[key] = song_counts.get(key, 0) + 1


# --- 7.3. 데이터프레임 생성 및 정렬 ---

# 집계된 결과를 데이터프레임으로 변환합니다.
df_counts = pd.DataFrame(song_counts.items(), columns=['곡명 - 아티스트', '등장 횟수'])

# '등장 횟수' 컬럼을 기준으로 내림차순 정렬합니다.
df_counts_sorted = df_counts.sort_values(by='등장 횟수', ascending=False)

# 상위 50개 곡만 선택합니다.
df_top25 = df_counts_sorted.head(50)


# --- 7.4. 시각화 (막대 그래프) ---

plt.figure(figsize=(10, 7))
# Seaborn의 barplot을 사용하여 막대 그래프를 생성합니다.
sns.barplot(
    x='등장 횟수',
    y='곡명 - 아티스트',
    data=df_top25,
    palette='viridis' # 색상 팔레트 설정
)

# 그래프 제목 및 레이블 설정
plt.title('멜론/벅스/지니 100위권 내 최다 등장 곡 (상위 50위)', fontsize=16)
plt.xlabel('등장 횟수 (최대 3회)', fontsize=12) # 최대 3개 차트에 등장할 수 있습니다.
plt.ylabel('곡명 - 아티스트', fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout() # 그래프 요소가 잘리지 않도록 레이아웃 조정

# 생성된 그래프를 PNG 파일로 저장합니다.
plt.savefig('music_top_100_chart.png')
# 그래프 저장 완료 메시지를 출력합니다.
print("\n그래프가 'music_top_100_chart.png'로 저장되었습니다.")

# 그래프를 화면에 출력합니다.
plt.show()