from urllib.request import urlopen
import bs4
import pandas as pd
import requests


jtbc_url = 'https://media.naver.com/press/437' # 크롤링할 JTBC 네이버 언론사 페이지 URL 정의


# 1. HTML 문서 가져오기 (requests)
jtbc_response = requests.get(jtbc_url) # 해당 URL로 HTTP GET 요청을 보내 응답을 받음
jtbc_response.encoding = 'UTF-8' # 응답 내용을 UTF-8로 인코딩 설정 (한글 깨짐 방지)

jtbc_target = jtbc_response.text # 응답 객체에서 텍스트(HTML 소스 코드)를 추출
# 2. HTML 파싱 (BeautifulSoup)
jtbc_dom = bs4.BeautifulSoup(jtbc_target, "lxml") # 추출한 HTML 텍스트를 lxml 파서를 사용하여 BeautifulSoup 객체로 변환


# 3. 필요한 요소 선택 (CSS Selector 사용)
# 기사 링크 요소들을 선택 (<a> 태그)
news_link = jtbc_dom.select("ul.press_edit_news_list a.press_edit_news_link")
# 기사 제목 요소들을 선택 (<span> 태그)
news_titles = jtbc_dom.select("ul.press_edit_news_list a span.press_edit_news_title")
# 썸네일 이미지 요소들을 선택 (<img> 태그)
news_thumb = jtbc_dom.select("ul.press_edit_news_list a span.press_edit_news_thumb img")


# 4. 데이터 저장을 위한 빈 리스트 초기화
jtbc_news_link = [] # 기사 링크(href 속성 값)를 저장할 리스트
jtbc_news_thumb = [] # 썸네일 이미지 URL(data-src 속성 값)을 저장할 리스트
jtbc_news_titles = [] # 기사 제목(텍스트 내용)을 저장할 리스트


# 5. 각 리스트에 데이터 추출 및 저장
# 링크 요소들(news_link)을 반복하며 'href' 속성 값을 추출하여 리스트에 추가
for link in news_link:
    jtbc_news_link.append(link.get('href'))

# 제목 요소들(news_titles)을 반복하며 텍스트 내용('strip=True'로 공백 제거)을 추출하여 리스트에 추가
for title in news_titles:
    jtbc_news_titles.append(title.get_text(strip=True))

# 썸네일 요소들(news_thumb)을 반복하며 'data-src' 속성 값(실제 이미지 URL)을 추출하여 리스트에 추가
for thumb in news_thumb:
    jtbc_news_thumb.append(thumb.get('data-src'))
    

# 6. Pandas DataFrame 생성
jtbc_data = {
    '제목': jtbc_news_titles, # '제목' 컬럼에 기사 제목 리스트 할당
    '썸네일': jtbc_news_thumb, # '썸네일' 컬럼에 썸네일 URL 리스트 할당
    '링크': jtbc_news_link     # '링크' 컬럼에 기사 링크 리스트 할당
}

df_jtbc_news = pd.DataFrame(jtbc_data) # 딕셔너리를 사용하여 DataFrame 생성

# 7. 인덱스 조정 및 재설정
df_jtbc_news.index += 1 # 기본 0부터 시작하는 인덱스를 1부터 시작하도록 +1 조정
df_jtbc_news.reset_index(drop=False, inplace=True) # 기존 인덱스를 'index'라는 새로운 컬럼으로 만들고, 인덱스를 0부터 새로 재설정
                                                   # (주석이 필요한 경우: 이 부분은 index 컬럼을 생성합니다. 컬럼명이 'index'가 아닌 다른 이름(예: 'No')이라면 rename을 추가하는 것이 좋습니다.)


# 8. Excel 파일로 저장
df_jtbc_news.to_excel('__jtbc_news.xlsx', index=False) # DataFrame을 '__jtbc_news.xlsx' 파일로 저장 (DataFrame 인덱스는 파일에 포함하지 않음)