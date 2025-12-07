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
genie_url = 'https://www.genie.co.kr/chart/top200/?ditc=D&ymd=20251206&hh=16&rtm=Y&pg='



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

melon_data = {
    '곡_제목': melon_song_title,
    '가수': melon_song_artist
}

df_melon_chart = pd.DataFrame(melon_data)

df_melon_chart.index += 1
df_melon_chart.reset_index(drop=False, inplace=True)







bugs_song_title = []
bugs_song_artist = []


def get_bugs_music():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get(bugs_url)
    
    music_info = driver.find_elements(By.CSS_SELECTOR, 'table.list.trackList.byChart tbody tr')
    
    for title in music_info:
        try:
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

bugs_data = {
    '곡_제목': bugs_song_title,
    '가수': bugs_song_artist
}

df_bugs_chart = pd.DataFrame(bugs_data)

df_bugs_chart.index += 1
df_bugs_chart.reset_index(drop=False, inplace=True)








genie_song_title = []
genie_song_artist = []


def get_genie_music(page):
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    driver.get(genie_url + str(page))
    
    music_info = driver.find_elements(By.CSS_SELECTOR,'table.list-wrap td.info')
    
    for title in music_info:
        try:
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
    
    
genie_data = {
    '곡_제목': genie_song_title,
    '가수': genie_song_artist
}

df_genie_chart = pd.DataFrame(genie_data)

df_genie_chart.index += 1
df_genie_chart.reset_index(drop=False, inplace=True)






df_melon_chart.to_excel('__01.melon_chart.xlsx', index=False)
df_bugs_chart.to_excel('__02.bugs_chart.xlsx', index=False)
df_genie_chart.to_excel('__03.genie_chart.xlsx', index=False)



melon_columns = {'index' : '순위', '곡_제목' : '곡 제목(멜론)', '가수' : '아티스트(멜론)'}
bugs_columns = {'index' : '순위', '곡_제목' : '곡 제목(벅스)', '가수' : '아티스트(벅스)'}
genie_columns = {'index' : '순위', '곡_제목' : '곡 제목(지니)', '가수' : '아티스트(지니)'}


df_melon_chart.rename(columns=melon_columns, inplace=True)
df_bugs_chart.rename(columns=bugs_columns, inplace=True)
df_genie_chart.rename(columns=genie_columns, inplace=True)




df_integration_chart = pd.merge(df_melon_chart, df_bugs_chart, on='순위', how='left')


df_integration_chart = pd.merge(df_integration_chart, df_genie_chart, on='순위', how='left')


df_integration_chart.to_excel('__04.integration_chart.xlsx', index=False) # index=False로 순위(index) 열은 제외하고 저장











melon_songs = df_melon_chart[['곡 제목(멜론)', '아티스트(멜론)']].values.tolist()
bugs_songs = df_bugs_chart[['곡 제목(벅스)', '아티스트(벅스)']].values.tolist()
genie_songs = df_genie_chart[['곡 제목(지니)', '아티스트(지니)']].values.tolist()


all_songs = melon_songs + bugs_songs + genie_songs

song_counts = {}
for title, artist in all_songs:
    key = f"{title} - {artist}"
    song_counts[key] = song_counts.get(key, 0) + 1


df_counts = pd.DataFrame(song_counts.items(), columns=['곡명 - 아티스트', '등장 횟수'])

df_counts_sorted = df_counts.sort_values(by='등장 횟수', ascending=False)

df_top25 = df_counts_sorted.head(50)



plt.figure(figsize=(10, 7))
sns.barplot(
    x='등장 횟수',
    y='곡명 - 아티스트',
    data=df_top25,
    palette='viridis'
)

plt.title('멜론/벅스/지니 100위권 내 최다 등장 곡 (상위 50위)', fontsize=16)
plt.xlabel('등장 횟수 (최대 3회)', fontsize=12)
plt.ylabel('곡명 - 아티스트', fontsize=12)
plt.grid(axis='x', linestyle='--')
plt.tight_layout()

plt.savefig('music_top_100_chart.png')
print("\n그래프가 'music_top_100_chart.png'로 저장되었습니다.")

plt.show()