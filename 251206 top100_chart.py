# --- 1. 라이브러리 임포트 ---
import webbrowser # 웹 브라우저를 제어하는 모듈 (현재 코드에서는 사용되지 않음)
import os         # 운영체제 기능을 제어하는 모듈 (현재 코드에서는 사용되지 않음)
import requests   # HTTP 요청을 보내는 데 사용되는 라이브러리 (멜론/벅스 정적 크롤링에 사용)
import bs4        # Beautiful Soup 라이브러리 (사용되지 않으나 bs4.BeautifulSoup으로 사용 가능)
from bs4 import BeautifulSoup # HTML 및 XML 파일에서 데이터를 추출하는 핵심 클래스 임포트
from urllib.request import urlopen # URL을 열기 위한 모듈 (requests를 사용하므로 현재 코드에서는 중복/미사용)
import pandas as pd # 데이터 분석 및 조작을 위한 핵심 라이브러리 (데이터프레임 생성/병합/저장에 사용)
import matplotlib.pyplot as plt # 데이터 시각화를 위한 기본 라이브러리
import seaborn as sns # Matplotlib 기반의 통계 데이터 시각화 라이브러리 (더 예쁜 그래프 생성)
import numpy as np # 과학 계산을 위한 라이브러리 (현재 코드에서는 미사용)
import korean # (주석 처리됨 또는 커스텀 라이브러리로 추정됨, 현재 코드에서 직접적인 역할 없음)
from selenium import webdriver # 웹 자동화 및 동적 크롤링을 위한 라이브러리
from selenium.webdriver.chrome.service import Service as ChromeService # 크롬 드라이버 서비스를 설정
from webdriver_manager.chrome import ChromeDriverManager # 크롬 드라이버 자동 다운로드/설치
from selenium.webdriver.common.by import By # Selenium에서 요소를 찾을 때 사용할 전략(CSS, ID 등)

# --- 2. URL 및 헤더 정의 ---
melon_url = 'https://www.melon.com/chart/' # 멜론 차트 URL (정적 크롤링 대상)
bugs_url = 'https://music.bugs.co.kr/chart/' # 벅스 차트 URL (정적 크롤링 대상)
# genie_url = 'https://www.genie.co.kr/chart/top200/' # 지니 URL (Selenium 동적 크롤링 대상)

# HTTP 요청 헤더 정의. 서버가 봇을 차단하는 것을 막기 위해 브라우저 정보를 포함합니다.
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# ---------------------------------------------------
# ## 멜론 차트 크롤링 (Requests + BeautifulSoup)
# ---------------------------------------------------

# headers를 포함하여 멜론 URL에 GET 요청을 보냅니다.
melon_response = requests.get(melon_url, headers=headers) 
# 응답의 인코딩을 UTF-8로 명시적으로 설정하여 한글 깨짐을 방지합니다.
melon_response.encoding = 'UTF-8'

# 응답 본문(HTML)을 텍스트로 추출합니다.
melon_target = melon_response.text
# Beautiful Soup 객체를 생성하여 HTML을 파싱합니다. 파서로 'lxml'을 사용합니다.
melon_dom = BeautifulSoup(melon_target, "lxml")


# CSS 선택자(Selector)를 사용하여 곡 제목 엘리먼트들을 선택합니다.
# 멜론 차트 구조에 맞는 정확한 경로를 지정합니다.
melon_song_title = melon_dom.select('table tbody .wrap .wrap_song_info .ellipsis.rank01')
# CSS 선택자를 사용하여 아티스트 이름 엘리먼트들을 선택합니다.
melon_song_artist = melon_dom.select('table tbody .wrap .wrap_song_info .ellipsis.rank02 .checkEllipsis')


# 크롤링한 제목과 아티스트를 저장할 빈 리스트를 초기화합니다.
melon_title = []
melon_artist = []


# 추출된 제목 엘리먼트들을 순회하며 텍스트를 추출합니다.
for title_element in melon_song_title:
    # .get_text(strip=True)를 사용하여 태그 내부의 텍스트만 추출하고 양 끝의 공백을 제거합니다.
    song_title = title_element.get_text(strip=True) 
    melon_title.append(song_title)
    
# 추출된 아티스트 엘리먼트들을 순회하며 텍스트를 추출합니다.
for artist_element in melon_song_artist:
    artist_name = artist_element.get_text(strip=True)
    melon_artist.append(artist_name)


# 추출된 데이터를 딕셔너리 형태로 구성합니다. (Pandas DataFrame 생성을 위함)
melon_data = {
    '곡_제목': melon_title,
    '가수': melon_artist
}

# 딕셔너리를 Pandas DataFrame으로 변환합니다.
df_melon_chart = pd.DataFrame(melon_data)

# DataFrame의 기본 인덱스를 1부터 시작하도록 변경합니다. (0 -> 1)
df_melon_chart.index += 1
# 새로운 인덱스를 'index'라는 컬럼으로 추가하고 (drop=False), 변경 사항을 원본에 즉시 반영합니다 (inplace=True).
df_melon_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 벅스 차트 크롤링 (Requests + BeautifulSoup)
# ---------------------------------------------------

# 벅스 URL에 GET 요청을 보냅니다.
bugs_response = requests.get(bugs_url, headers=headers)
# 인코딩 설정
bugs_response.encoding = 'UTF-8'

# 응답 본문(HTML)을 텍스트로 추출합니다.
bugs_target = bugs_response.text
# Beautiful Soup 객체 생성 및 HTML 파싱
bugs_dom = BeautifulSoup(bugs_target, "lxml")


# CSS 선택자를 사용하여 곡 제목 엘리먼트들을 선택합니다.
bugs_song_title = bugs_dom.select('table.list.trackList.byChart > tbody > tr > th > p.title > a')
# CSS 선택자를 사용하여 아티스트 이름 엘리먼트들을 선택합니다.
bugs_song_artist = bugs_dom.select('table.list.trackList.byChart > tbody > tr > td.left > p.artist > a:first-child')


# 벅스 데이터를 저장할 빈 리스트를 초기화합니다.
bugs_title = []
bugs_artist = []


# 추출된 제목 엘리먼트들을 순회하며 텍스트를 추출합니다.
for title_element in bugs_song_title:
    song_title = title_element.get_text(strip=True)
    bugs_title.append(song_title)
    
# 추출된 아티스트 엘리먼트들을 순회하며 텍스트를 추출합니다.
for artist_element in bugs_song_artist:
    artist_name = artist_element.get_text(strip=True)
    bugs_artist.append(artist_name)


# 추출된 데이터를 딕셔너리 형태로 구성합니다.
bugs_data = {
    '곡_제목': bugs_title,
    '가수': bugs_artist
}

# 딕셔너리를 Pandas DataFrame으로 변환합니다.
df_bugs_chart = pd.DataFrame(bugs_data)

# DataFrame의 인덱스를 1부터 시작하도록 변경합니다.
df_bugs_chart.index += 1
# 새로운 인덱스를 'index' 컬럼으로 추가하고 원본에 반영합니다.
df_bugs_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 지니 차트 크롤링 (Selenium 동적 크롤링)
# ---------------------------------------------------

# 지니 데이터를 저장할 전역 리스트를 초기화합니다.
genie_song_title = []
genie_song_artist = []

# 지니 차트 페이지를 순회하며 데이터를 가져오는 함수를 정의합니다.
def get_genie_music(page):
    # Chrome WebDriver를 초기화하고 드라이버를 자동으로 설치/관리합니다.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 지니 차트 URL과 페이지 번호를 조합하여 접속합니다. (날짜/시간은 고정값 사용)
    driver.get("https://www.genie.co.kr/chart/top200/?ditc=D&ymd=20251206&hh=16&rtm=Y&pg=" + str(page))
    
    # CSS 선택자를 이용해 음악 정보(곡 제목, 가수 정보가 포함된 td)가 있는 모든 엘리먼트를 찾습니다.
    music_info = driver.find_elements(By.CSS_SELECTOR,'table.list-wrap td.info')
    
    # music_info 리스트를 순회하며 곡 제목을 추출합니다. (반복문이 중복되어 있음 - 비효율적)
    # *참고: 여기서는 title과 artist를 각각 순회하므로 크롤링이 두 번 발생하여 비효율적입니다.
    
    # 1. 곡 제목 추출
    for title_container in music_info:
        try:
            # 현재 info 엘리먼트 내에서 'a.title' 선택자를 가진 엘리먼트(제목)를 찾습니다.
            tmp_elements = title_container.find_elements(By.CSS_SELECTOR, 'a.title')
            
            if tmp_elements:
                # 찾은 엘리먼트의 텍스트를 추출합니다. (지니는 종종 불필요한 공백을 포함하므로 strip()이 필요할 수 있습니다)
                title = tmp_elements[0].text.strip()
            else:
                title = "해당 정보 없음" # 제목을 찾지 못한 경우 기본값 설정
            
            genie_song_title.append(title)
        except:
            print("제목 추출 중 에러 발생!")
            
            
    # 2. 아티스트 이름 추출
    for artist_container in music_info:
        try:
            # 현재 info 엘리먼트 내에서 'a.artist' 선택자를 가진 엘리먼트(아티스트)를 찾습니다.
            tmp_elements = artist_container.find_elements(By.CSS_SELECTOR, 'a.artist')
            
            if tmp_elements:
                # 찾은 엘리먼트의 텍스트를 추출합니다.
                artist = tmp_elements[0].text.strip()
            else:
                artist = "해당 정보 없음" # 아티스트를 찾지 못한 경우 기본값 설정
            
            genie_song_artist.append(artist)
        except:
            print("아티스트 추출 중 에러 발생!")
            
    print("end :", page)
    # 작업이 완료되면 WebDriver를 종료하고 관련 프로세스를 정리합니다.
    driver.quit()


# 1페이지부터 2페이지까지 (총 2페이지, 즉 100위까지) get_genie_music 함수를 호출합니다.
for page in range(1, 3):
    get_genie_music(page)
    
    
# 추출된 지니 데이터를 딕셔너리로 구성합니다.
genie_data = {
    '곡_제목': genie_song_title,
    '가수': genie_song_artist
}

# 딕셔너리를 Pandas DataFrame으로 변환합니다.
df_genie_chart = pd.DataFrame(genie_data)

# DataFrame의 인덱스를 1부터 시작하도록 변경합니다.
df_genie_chart.index += 1
# 새로운 인덱스를 'index' 컬럼으로 추가하고 원본에 반영합니다.
df_genie_chart.reset_index(drop=False, inplace=True)


# ---------------------------------------------------
# ## 5. 데이터프레임 처리 및 통합
# ---------------------------------------------------

# --- 5.1. 개별 데이터프레임을 Excel 파일로 저장 ---
# 각 차트별 데이터를 개별 Excel 파일로 저장합니다.
df_melon_chart.to_excel('__01.melon_chart.xlsx', index=False) # index=False는 순위 컬럼을 중복 저장하지 않기 위함
df_bugs_chart.to_excel('__02.bugs_chart.xlsx', index=False)
df_genie_chart.to_excel('__03.genie_chart.xlsx', index=False)



# --- 5.2. 컬럼명 정의 (차트별 구분을 위해 컬럼명 변경) ---
# 병합 시 충돌을 피하고 출처를 명확히 하기 위해 컬럼 이름을 변경할 딕셔너리를 정의합니다.
melon_columns = {'index' : '순위', '곡_제목' : '곡 제목(멜론)', '가수' : '아티스트(멜론)'}
bugs_columns = {'index' : '순위', '곡_제목' : '곡 제목(벅스)', '가수' : '아티스트(벅스)'}
genie_columns = {'index' : '순위', '곡_제목' : '곡 제목(지니)', '가수' : '아티스트(지니)'}


# --- 5.3. 컬럼명 변경 적용 ---
# DataFrame의 컬럼 이름을 정의된 딕셔너리를 이용해 변경합니다.
df_melon_chart.rename(columns=melon_columns, inplace=True)
df_bugs_chart.rename(columns=bugs_columns, inplace=True)
df_genie_chart.rename(columns=genie_columns, inplace=True)



# --- 5.4. 데이터프레임 통합 (핵심 로직: Pandas merge) ---

# 1. 멜론 차트(df_melon_chart)를 기준으로 벅스 차트(df_bugs_chart)를 '순위' 열을 키(on='순위')로 좌측 병합 (LEFT JOIN).
# 결과는 df_integration_chart에 저장됩니다. (멜론 순위에 맞춰 벅스 정보를 붙임)
df_integration_chart = pd.merge(df_melon_chart, df_bugs_chart, on='순위', how='left')

# 2. 통합된 데이터프레임에 지니 차트 정보(df_genie_chart)를 '순위' 열을 키로 다시 좌측 병합합니다.
# 최종 통합 데이터프레임이 완성됩니다.
df_integration_chart = pd.merge(df_integration_chart, df_genie_chart, on='순위', how='left')


# --- 5.5. 최종 통합 데이터프레임을 Excel 파일로 저장 ---
# 모든 차트 정보가 순위별로 병합된 파일을 저장합니다.
df_integration_chart.to_excel('__04.integration_chart.xlsx', index=False) # index=False로 순위(index) 열은 제외하고 저장


# ---------------------------------------------------
# ## 6. 통합 데이터 분석 및 시각화
# ---------------------------------------------------

# --- 1. 통합 데이터프레임에서 곡 정보 추출 및 결합 ---

# 멜론 DataFrame에서 곡 제목과 아티스트 컬럼을 선택하고, .values.tolist()를 사용하여 [제목, 아티스트] 형태의 리스트로 변환합니다.
melon_songs = df_melon_chart[['곡 제목(멜론)', '아티스트(멜론)']].values.tolist()
# 벅스 차트 정보 추출
bugs_songs = df_bugs_chart[['곡 제목(벅스)', '아티스트(벅스)']].values.tolist()
# 지니 차트 정보 추출
genie_songs = df_genie_chart[['곡 제목(지니)', '아티스트(지니)']].values.tolist()


# 모든 세 차트의 곡 정보를 하나의 리스트로 통합합니다.
all_songs = melon_songs + bugs_songs + genie_songs

# --- 2. 등장 횟수 집계 ---

# 곡 제목과 아티스트를 결합한 문자열을 키로 사용하여 각 곡의 등장 횟수를 계산할 딕셔너리를 초기화합니다.
song_counts = {}
for title, artist in all_songs:
    # 곡과 아티스트를 묶어 고유한 키를 생성합니다. (예: "Ditto - NewJeans")
    key = f"{title} - {artist}"
    # 딕셔너리에서 해당 키의 값을 가져오고 (없으면 0), 1을 더해 업데이트합니다.
    song_counts[key] = song_counts.get(key, 0) + 1

# --- 3. 데이터프레임 생성 및 정렬 ---

# 집계된 딕셔너리(song_counts)의 (키, 값) 항목들을 데이터프레임으로 변환합니다.
df_counts = pd.DataFrame(song_counts.items(), columns=['곡명 - 아티스트', '등장 횟수'])

# '등장 횟수' 컬럼을 기준으로 내림차순 정렬합니다. (가장 많이 등장한 곡이 위로)
df_counts_sorted = df_counts.sort_values(by='등장 횟수', ascending=False)

# 상위 50개 곡만 선택하여 시각화에 사용할 데이터프레임을 생성합니다.
df_top25 = df_counts_sorted.head(50)


# --- 4. 시각화 (막대 그래프) ---
# 
# 그래프 크기를 설정합니다.
plt.figure(figsize=(10, 7))
# Seaborn을 사용하여 막대 그래프 (Bar Plot)를 생성합니다.
sns.barplot(
    # x축: 등장 횟수
    x='등장 횟수',
    # y축: 곡명 - 아티스트 (가장 많이 등장한 순으로 정렬됨)
    y='곡명 - 아티스트',
    data=df_top25,
    palette='viridis' # 색상 팔레트 설정
)

# 그래프 제목 및 레이블 설정
plt.title('멜론/벅스/지니 100위권 내 최다 등장 곡 (상위 50위)', fontsize=16)
# x축 레이블 (최대 등장 횟수는 3회입니다)
plt.xlabel('등장 횟수 (최대 3회)', fontsize=12)
# y축 레이블
plt.ylabel('곡명 - 아티스트', fontsize=12)
# x축에만 그리드 라인 (점선)을 추가하여 가독성을 높입니다.
plt.grid(axis='x', linestyle='--')
# 그래프 요소가 잘리지 않도록 레이아웃을 자동으로 조정합니다.
plt.tight_layout()

# 생성된 그래프를 PNG 파일로 저장합니다.
plt.savefig('music_top_100_chart.png')
# 그래프 저장 완료 메시지를 출력합니다.
print("\n그래프가 'music_top_100_chart.png'로 저장되었습니다.")

# 그래프를 화면에 출력합니다.
plt.show()