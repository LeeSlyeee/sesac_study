import webbrowser
import os
import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
import pandas as pd



melon_url = 'https://www.melon.com/chart/'
bugs_url = 'https://music.bugs.co.kr/chart/'
genie_url = 'https://www.genie.co.kr/chart/top200/'


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

melon_response = requests.get(melon_url, headers=headers)
melon_response.encoding = 'UTF-8'

melon_target = melon_response.text
melon_dom = BeautifulSoup(melon_target, "lxml")


# melon_song_rank = melon_dom.select('.service_list_song table tbody .rank')
melon_song_title = melon_dom.select('.service_list_song table tbody .wrap .wrap_song_info .ellipsis.rank01 > span > a')
melon_song_artist = melon_dom.select('.service_list_song table tbody .wrap .wrap_song_info .ellipsis.rank02 > span > a:first-child')


# melon_rank = []
melon_title = []
melon_artist = []



# for rank_element in melon_song_rank:
#     rank_number = int(rank_element.get_text(strip=True))
#     melon_rank.append(rank_number)
    
for title_element in melon_song_title:
    song_title = title_element.get_text(strip=True)
    melon_title.append(song_title)
    
for artist_element in melon_song_artist:
    artist_name = artist_element.get_text(strip=True)
    melon_artist.append(artist_name)


melon_data = {
    # '순위': melon_rank,
    '곡_제목': melon_title,
    '가수': melon_artist
}



df_melon_chart = pd.DataFrame(melon_data)









bugs_response = requests.get(bugs_url, headers=headers)
bugs_response.encoding = 'UTF-8'

bugs_target = bugs_response.text
bugs_dom = BeautifulSoup(bugs_target, "lxml")



# bugs_song_rank = bugs_dom.select('table.list.trackList.byChart > tbody > tr > td > div.ranking > strong')
bugs_song_title = bugs_dom.select('table.list.trackList.byChart > tbody > tr > th > p.title > a')
bugs_song_artist = bugs_dom.select('table.list.trackList.byChart > tbody > tr > td.left > p.artist > a:first-child')


# bugs_rank = []
bugs_title = []
bugs_artist = []



# for rank_element in bugs_song_rank:
#     rank_number = int(rank_element.get_text(strip=True))
#     bugs_rank.append(rank_number)
    
for title_element in bugs_song_title:
    song_title = title_element.get_text(strip=True)
    bugs_title.append(song_title)
    
for artist_element in bugs_song_artist:
    artist_name = artist_element.get_text(strip=True)
    bugs_artist.append(artist_name)


bugs_data = {
    # '순위': bugs_rank,
    '곡_제목': bugs_title,
    '가수': bugs_artist
}

df_bugs_chart = pd.DataFrame(bugs_data)











genie_response = requests.get(genie_url, headers=headers)
genie_response.encoding = 'UTF-8'

genie_target = genie_response.text
genie_dom = BeautifulSoup(genie_target, "lxml")


# genie_song_rank = genie_dom.select('table.list-wrap > tbody > tr.list > td.number')[0]
# print(f">>>>>>>>> {genie_song_rank}")

genie_song_title = genie_dom.select('table.list-wrap > tbody > tr.list > td.info > a.title')
genie_song_artist = genie_dom.select('table.list-wrap > tbody > tr.list > td.info > a.artist')


# genie_rank = []
genie_title = []
genie_artist = []



# for rank_element in genie_song_rank:
#     rank_number = int(rank_element.get_text(strip=True))
#     genie_rank.append(rank_number)
    
for title_element in genie_song_title:
    song_title = title_element.get_text(strip=True)
    genie_title.append(song_title)
    
for artist_element in genie_song_artist:
    artist_name = artist_element.get_text(strip=True)
    genie_artist.append(artist_name)


genie_data = {
    # '순위': genie_rank,
    '곡_제목': genie_title,
    '가수': genie_artist
}



df_genie_chart = pd.DataFrame(genie_data)


df_melon_chart.to_excel('__01.melon_chart.xlsx', index=False)
df_bugs_chart.to_excel('__02.bugs_chart.xlsx', index=False)
df_genie_chart.to_excel('__03.genie_chart.xlsx', index=False)




print()













