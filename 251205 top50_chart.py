import webbrowser # 웹 브라우저를 제어하는 모듈 (현재 코드에서는 사용되지 않음)
import os           # 운영체제 기능을 제어하는 모듈 (현재 코드에서는 사용되지 않음)
import requests     # HTTP 요청을 보내는 데 사용되는 라이브러리
import bs4          # Beautiful Soup 라이브러리 (BeautifulSoup 클래스를 사용)
from bs4 import BeautifulSoup # HTML 및 XML 파일에서 데이터를 추출하는 데 사용되는 라이브러리
from urllib.request import urlopen # URL을 열기 위한 모듈 (requests를 사용하므로 중복될 수 있음)
import pandas as pd # 데이터 분석 및 조작을 위한 핵심 라이브러리 (데이터프레임 생성/병합에 사용)
import matplotlib.pyplot as plt 
import seaborn as sns
import numpy as np
import korean


# --- 1.1. 크롤링 대상 URL 정의 ---
melon_url = 'https://www.melon.com/chart/'
bugs_url = 'https://music.bugs.co.kr/chart/'
genie_url = 'https://www.genie.co.kr/chart/top200/'


# --- 1.2. HTTP 헤더 설정 ---
# 봇(Bot)으로 인식되어 차단되는 것을 방지하기 위해 User-Agent를 정의
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

# --- 2.1. 멜론 차트 데이터 요청 및 파싱 ---
melon_response = requests.get(melon_url, headers=headers) # 설정된 URL과 헤더로 GET 요청
melon_response.encoding = 'UTF-8'                        # 응답 인코딩을 UTF-8로 설정하여 한글 깨짐 방지

melon_target = melon_response.text                       # 응답의 텍스트 콘텐츠(HTML) 추출
melon_dom = BeautifulSoup(melon_target, "lxml")          # BeautifulSoup 객체 생성 및 HTML 파싱 (lxml 파서 사용)


# --- 2.2. CSS Selector를 이용한 데이터 추출 ---
# 곡 제목 요소 선택: 'table tbody .wrap .wrap_song_info .ellipsis.rank01'
melon_song_title = melon_dom.select('table tbody .wrap .wrap_song_info .ellipsis.rank01')
# 아티스트 이름 요소 선택: 'table tbody .wrap .wrap_song_info .ellipsis.rank02 .checkEllipsis'
melon_song_artist = melon_dom.select('table tbody .wrap .wrap_song_info .ellipsis.rank02 .checkEllipsis')


# --- 2.3. 추출된 데이터를 리스트에 저장 ---
melon_title = []
melon_artist = []


for title_element in melon_song_title[:50]: # 상위 50개 항목만 반복
    song_title = title_element.get_text(strip=True) # 태그 제거 및 공백 제거 후 텍스트 추출
    melon_title.append(song_title)
    
for artist_element in melon_song_artist[:50]: # 상위 50개 항목만 반복
    artist_name = artist_element.get_text(strip=True)
    melon_artist.append(artist_name)


# --- 2.4. 멜론 데이터프레임 생성 및 순위 추가 ---
melon_data = {
    '곡_제목': melon_title,
    '가수': melon_artist
}

df_melon_chart = pd.DataFrame(melon_data) # 리스트를 이용하여 데이터프레임 생성

df_melon_chart.index += 1                     # 0부터 시작하는 인덱스를 1부터 시작하도록 변경 (순위 역할)
df_melon_chart.reset_index(drop=False, inplace=True) # 인덱스를 'index'라는 이름의 새로운 열로 변환 (순위 열 생성)







# --- 3.1. 벅스 차트 데이터 요청 및 파싱 ---
bugs_response = requests.get(bugs_url, headers=headers)
bugs_response.encoding = 'UTF-8'

bugs_target = bugs_response.text
bugs_dom = BeautifulSoup(bugs_target, "lxml")


# --- 3.2. CSS Selector를 이용한 데이터 추출 ---
# 곡 제목 요소 선택
bugs_song_title = bugs_dom.select('table.list.trackList.byChart > tbody > tr > th > p.title > a')
# 아티스트 이름 요소 선택 (첫 번째 a 태그만 선택)
bugs_song_artist = bugs_dom.select('table.list.trackList.byChart > tbody > tr > td.left > p.artist > a:first-child')


# --- 3.3. 추출된 데이터를 리스트에 저장 ---
bugs_title = []
bugs_artist = []


for title_element in bugs_song_title[:50]:
    song_title = title_element.get_text(strip=True)
    bugs_title.append(song_title)
    
for artist_element in bugs_song_artist[:50]:
    artist_name = artist_element.get_text(strip=True)
    bugs_artist.append(artist_name)


# --- 3.4. 벅스 데이터프레임 생성 및 순위 추가 ---
bugs_data = {
    '곡_제목': bugs_title,
    '가수': bugs_artist
}

df_bugs_chart = pd.DataFrame(bugs_data)

df_bugs_chart.index += 1
df_bugs_chart.reset_index(drop=False, inplace=True)








# --- 4.1. 지니 차트 데이터 요청 및 파싱 ---
genie_response = requests.get(genie_url, headers=headers)
genie_response.encoding = 'UTF-8'

genie_target = genie_response.text
genie_dom = BeautifulSoup(genie_target, "lxml")


# --- 4.2. CSS Selector를 이용한 데이터 추출 ---
# 곡 제목 요소 선택
genie_song_title = genie_dom.select('table.list-wrap > tbody > tr.list > td.info > a.title')
# 아티스트 이름 요소 선택
genie_song_artist = genie_dom.select('table.list-wrap > tbody > tr.list > td.info > a.artist')


# --- 4.3. 추출된 데이터를 리스트에 저장 ---
genie_title = []
genie_artist = []


for title_element in genie_song_title[:50]:
    # 지니는 텍스트에 순위 번호나 다른 불필요한 공백이 있을 수 있으므로 추가적인 전처리가 필요할 수 있음
    song_title = title_element.get_text(strip=True)
    genie_title.append(song_title)
    
for artist_element in genie_song_artist[:50]:
    artist_name = artist_element.get_text(strip=True)
    genie_artist.append(artist_name)


# --- 4.4. 지니 데이터프레임 생성 및 순위 추가 ---
genie_data = {
    '곡_제목': genie_title,
    '가수': genie_artist
}

df_genie_chart = pd.DataFrame(genie_data)

df_genie_chart.index += 1
df_genie_chart.reset_index(drop=False, inplace=True)



# --- 5.1. 개별 데이터프레임을 Excel 파일로 저장 ---
df_melon_chart.to_excel('__01.melon_chart.xlsx', index=False)
df_bugs_chart.to_excel('__02.bugs_chart.xlsx', index=False)
df_genie_chart.to_excel('__03.genie_chart.xlsx', index=False)



# --- 5.2. 컬럼명 정의 (차트별 구분을 위해 컬럼명 변경) ---
melon_columns = {'index' : '순위', '곡_제목' : '곡 제목(멜론)', '가수' : '아티스트(멜론)'}
bugs_columns = {'index' : '순위', '곡_제목' : '곡 제목(벅스)', '가수' : '아티스트(벅스)'}
genie_columns = {'index' : '순위', '곡_제목' : '곡 제목(지니)', '가수' : '아티스트(지니)'}


# --- 5.3. 컬럼명 변경 적용 ---
df_melon_chart.rename(columns=melon_columns, inplace=True)
df_bugs_chart.rename(columns=bugs_columns, inplace=True)
df_genie_chart.rename(columns=genie_columns, inplace=True)



# --- 5.4. 데이터프레임 통합 (핵심 로직) ---

# 1. 멜론 차트를 기준으로 벅스 차트와 '순위' 열을 키로 좌측 병합 (LEFT JOIN)
df_integration_chart = pd.merge(df_melon_chart, df_bugs_chart, on='순위', how='left')

# 2. 통합된 데이터프레임에 지니 차트 정보를 '순위' 열을 키로 다시 좌측 병합
df_integration_chart = pd.merge(df_integration_chart, df_genie_chart, on='순위', how='left')


# --- 5.5. 최종 통합 데이터프레임을 Excel 파일로 저장 ---
df_integration_chart.to_excel('__04.integration_chart.xlsx', index=False) # index=False로 순위(index) 열은 제외하고 저장











# --- 1. 통합 데이터프레임에서 곡 정보 추출 및 결합 ---

# 멜론, 벅스, 지니의 곡 제목과 아티스트 리스트를 생성합니다.
melon_songs = df_melon_chart[['곡 제목(멜론)', '아티스트(멜론)']].values.tolist()
bugs_songs = df_bugs_chart[['곡 제목(벅스)', '아티스트(벅스)']].values.tolist()
genie_songs = df_genie_chart[['곡 제목(지니)', '아티스트(지니)']].values.tolist()


# 모든 곡 정보를 하나의 리스트로 통합합니다.
all_songs = melon_songs + bugs_songs + genie_songs

# --- 2. 등장 횟수 집계 ---

# 곡 제목과 아티스트를 결합한 문자열을 키로 사용하여 등장 횟수를 계산합니다.
song_counts = {}
for title, artist in all_songs:
    # 곡과 아티스트를 묶어 고유한 키를 생성합니다. (예: "Ditto - NewJeans")
    key = f"{title} - {artist}"
    song_counts[key] = song_counts.get(key, 0) + 1

# --- 3. 데이터프레임 생성 및 정렬 ---

# 집계된 결과를 데이터프레임으로 변환합니다.
df_counts = pd.DataFrame(song_counts.items(), columns=['곡명 - 아티스트', '등장 횟수'])

# 등장 횟수를 기준으로 내림차순 정렬합니다.
df_counts_sorted = df_counts.sort_values(by='등장 횟수', ascending=False)

# 상위 25개 곡만 선택합니다.
df_top25 = df_counts_sorted.head(25)


# --- 4. 시각화 (막대 그래프) ---

plt.figure(figsize=(10, 7))
# 등장 횟수를 x축, 곡 이름을 y축으로 하는 막대 그래프를 생성합니다.
sns.barplot(
    x='등장 횟수',
    y='곡명 - 아티스트',
    data=df_top25,
    palette='viridis' # 색상 팔레트 설정
)

# 그래프 제목 및 레이블 설정
plt.title('멜론/벅스/지니 50위권 내 최다 등장 곡 (상위 10위)', fontsize=16)
plt.xlabel('등장 횟수 (최대 3회)', fontsize=12)
plt.ylabel('곡명 - 아티스트', fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout()
plt.show()