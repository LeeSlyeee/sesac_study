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
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


# --- 1.1. 크롤링 대상 URL 정의 ---
melon_url = 'https://www.melon.com/chart/'
bugs_url = 'https://music.bugs.co.kr/chart/'
# genie_url = 'https://www.genie.co.kr/chart/top200/'



melon_song_title = []
melon_song_artist = []


def get_melon_music():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get(melon_url)
    
    music_info = driver.find_elements(By.CSS_SELECTOR, 'table tbody tr')
    
    for title in music_info:
        try:
            # 1. 일반적인 기사 제목을 포함하는 요소를 찾습니다.
            tmp_elements = title.find_elements(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank01')
            
            if tmp_elements:
                title = tmp_elements[0].text
            else:
                title = "해당 정보 없음"
            
            melon_song_title.append(title)
        except:
            print("에러 발생!")
            
            
    for artist in music_info:
        try:
            tmp_elements = artist.find_elements(By.CSS_SELECTOR, '.wrap_song_info .ellipsis.rank02 a')
            
            if tmp_elements:
                artist = tmp_elements[0].text
            else:
                artist = "해당 정보 없음"
            
            melon_song_artist.append(artist)
        except:
            print("에러 발생!")
            
    driver.quit()

get_melon_music()

# --- 2.4. 멜론 데이터프레임 생성 및 순위 추가 ---
melon_data = {
    '곡_제목': melon_song_title,
    '가수': melon_song_artist
}

df_melon_chart = pd.DataFrame(melon_data) # 리스트를 이용하여 데이터프레임 생성

df_melon_chart.index += 1                     # 0부터 시작하는 인덱스를 1부터 시작하도록 변경 (순위 역할)
df_melon_chart.reset_index(drop=False, inplace=True) # 인덱스를 'index'라는 이름의 새로운 열로 변환 (순위 열 생성)







# --- 3.1. 벅스 차트 데이터 요청 및 파싱 ---

# --- 3.2. CSS Selector를 이용한 데이터 추출 ---
# 곡 제목 요소 선택
bugs_song_title = []
# 아티스트 이름 요소 선택 (첫 번째 a 태그만 선택)
bugs_song_artist = []


def get_bugs_music():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get(bugs_url)
    
    music_info = driver.find_elements(By.CSS_SELECTOR, 'table.list.trackList.byChart tbody tr')
    
    for title in music_info:
        try:
            # 1. 일반적인 기사 제목을 포함하는 요소를 찾습니다.
            tmp_elements = title.find_elements(By.CSS_SELECTOR, 'p.title a')
            
            if tmp_elements:
                title = tmp_elements[0].text
            else:
                title = "해당 정보 없음"
            
            bugs_song_title.append(title)
        except:
            print("에러 발생!")
            
            
    for artist in music_info:
        try:
            tmp_elements = artist.find_elements(By.CSS_SELECTOR, 'p.artist a')
            
            if tmp_elements:
                artist = tmp_elements[0].text
            else:
                artist = "해당 정보 없음"
            
            bugs_song_artist.append(artist)
        except:
            print("에러 발생!")
            
    driver.quit()

get_bugs_music()

# --- 3.4. 벅스 데이터프레임 생성 및 순위 추가 ---
bugs_data = {
    '곡_제목': bugs_song_title,
    '가수': bugs_song_artist
}

df_bugs_chart = pd.DataFrame(bugs_data)

df_bugs_chart.index += 1
df_bugs_chart.reset_index(drop=False, inplace=True)








# # --- 4.1. 지니 차트 데이터 요청 및 파싱 ---
# genie_response = requests.get(genie_url, headers=headers)
# genie_response.encoding = 'UTF-8'

# genie_target = genie_response.text



# --- 4.3. 추출된 데이터를 리스트에 저장 ---
genie_song_title = []
genie_song_artist = []


def get_genie_music(page):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get("https://www.genie.co.kr/chart/top200/?ditc=D&ymd=20251206&hh=16&rtm=Y&pg=" + str(page))
    
    music_info = driver.find_elements(By.CSS_SELECTOR,'table.list-wrap td.info')
    
    for title in music_info:
        try:
            # 1. 일반적인 기사 제목을 포함하는 요소를 찾습니다.
            tmp_elements = title.find_elements(By.CSS_SELECTOR, 'td.info a.title')
            
            if tmp_elements:
                title = tmp_elements[0].text
            else:
                title = "해당 정보 없음"
            
            genie_song_title.append(title)
        except:
            print("에러 발생!")
            
            
    for artist in music_info:
        try:
            tmp_elements = artist.find_elements(By.CSS_SELECTOR, 'td.info a.artist')
            
            if tmp_elements:
                artist = tmp_elements[0].text
            else:
                artist = "해당 정보 없음"
            
            genie_song_artist.append(artist)
        except:
            print("에러 발생!")
            
    print("end :", page)
    driver.quit()


for page in range(1, 3):
    get_genie_music(page)
    
    
# --- 4.4. 지니 데이터프레임 생성 및 순위 추가 ---
genie_data = {
    '곡_제목': genie_song_title,
    '가수': genie_song_artist
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
df_top25 = df_counts_sorted.head(50)


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
plt.title('멜론/벅스/지니 100위권 내 최다 등장 곡 (상위 50위)', fontsize=16)
plt.xlabel('등장 횟수 (최대 3회)', fontsize=12)
plt.ylabel('곡명 - 아티스트', fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout()

# 생성된 그래프를 'music_top_100_chart.png' 파일로 저장합니다.
plt.savefig('music_top_100_chart.png')
# 그래프 저장 완료 메시지를 출력합니다.
print("\n그래프가 'music_top_100_chart.png'로 저장되었습니다.")

plt.show()