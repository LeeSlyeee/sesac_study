# 'webbrowser' 모듈: 웹 브라우저를 제어하고 URL을 열 수 있게 해줍니다.
import webbrowser
# 'os' 모듈: 운영체제(Operating System)의 기능에 접근할 수 있게 해줍니다. (이 코드에서는 사용되지 않음)
import os
# 'requests' 모듈: HTTP 요청(GET, POST 등)을 보내 웹 페이지의 데이터를 가져올 수 있게 해줍니다.
import requests
# 'bs4'의 'BeautifulSoup' 클래스: HTML이나 XML 파일의 구문 분석(파싱)을 돕고, 데이터를 추출하기 쉽게 만듭니다.
from bs4 import BeautifulSoup





# --- 네이버 검색 예제 ---

# 네이버 검색 기본 URL을 변수에 저장합니다.
naver_search_url = 'http://search.naver.com/search.naver?query='
# 검색할 단어를 지정합니다. ('파이썬'은 한국어로 'Python'을 의미)
search_word = '파이썬'
# 기본 URL과 검색어를 결합하여 전체 검색 URL을 완성합니다.
url = naver_search_url + search_word
# 완성된 URL을 운영체제의 기본 웹 브라우저의 "새 창" 또는 "새 탭"으로 엽니다.
webbrowser.open_new(url)






# --- 구글 검색 예제 (영어) ---

# 구글 검색 기본 URL을 변수에 저장합니다.
google_url = 'http://www.google.com/search?q='
# 검색할 단어를 지정합니다. (여기서는 'python' 영어 단어)
search_word = 'python'
# 기본 URL과 검색어를 결합하여 전체 검색 URL을 완성합니다.
url = google_url + search_word
# 완성된 URL을 "새 창" 또는 "새 탭"으로 엽니다.
webbrowser.open_new(url)





# --- 다중 웹사이트 열기 예제 ---

# 열고자 하는 여러 웹사이트 URL을 리스트로 정의합니다. (접속 시 'http://'가 자동으로 붙음)
urls = ['www.naver.com', 'www.daum.net', 'www.google.com']

# 리스트에 있는 각 URL을 반복문(for loop)을 통해 순서대로 처리합니다.
for url in urls:
    # 각 URL을 "새 창" 또는 "새 탭"으로 엽니다.
    webbrowser.open_new(url)





# --- 다중 검색어 구글 검색 예제 ---

# 구글 검색 기본 URL을 변수에 저장합니다.
google_url = "www.google.com/search?q="
# 검색할 여러 키워드를 리스트로 정의합니다.
search_words = ['python web scraping', 'python webbrowser']
# 리스트에 있는 각 검색어를 반복문으로 처리합니다.
for search_word in search_words:
    # 기본 URL과 검색어를 결합하여 검색을 수행합니다.
    # 'webbrowser.open()'은 이미 열려있는 창이 있으면 "새 탭"으로 열릴 가능성이 높습니다.
    # 'webbrowser.open_new()'와 달리 "새 창"을 강제하지 않을 수 있습니다.
    webbrowser.open(google_url + search_word)





# --- 'requests' 모듈을 이용한 웹 페이지 요청 예제 ---

# 'requests.get()' 함수를 사용하여 지정된 URL("https://www.google.co.kr")로 "GET" 요청을 보냅니다.
# 요청의 결과는 'r' 변수(Response 객체)에 저장됩니다.
r = requests.get("https://www.google.co.kr")
# Response 객체 'r'을 출력합니다.
# 보통 "<Response [200]>"과 같은 형태로 출력되며, 여기서 '200'은 HTTP 상태 코드로 요청이 "성공적"이었음을 나타냅니다.
print(r)

# Response 객체의 'text' 속성(가져온 웹 페이지의 HTML 소스 코드 문자열)에서
# "처음 100자"만을 잘라서(슬라이싱) 출력합니다.
# 이를 통해 웹 페이지의 "HTML 소스가 성공적으로 수신"되었는지 확인할 수 있습니다.
print(r.text[0:100])





# --- 'BeautifulSoup'을 이용한 HTML 파싱(Parsing) 예제 ---

# HTML 코드를 포함하는 문자열을 정의합니다.
html = """ <html> <body> <div> <span> <a href=http://www.naver.com>naver</a> <a href=https://www.google.com>google</a> <a href=http://www.daum.net/>daum</a> </span> </div> </body> </html> """

# BeautifulSoup 객체를 생성합니다.
# 첫 번째 인수는 파싱할 HTML 데이터, 두 번째 인수는 사용할 파서("lxml"이 빠르고 강력함)입니다.
soup = BeautifulSoup(html, 'lxml')
print(soup) # 파싱된 BeautifulSoup 객체 전체를 출력합니다. (입력된 HTML과 거의 같습니다)


print(soup.prettify()) # HTML을 들여쓰기하여 가독성 좋게 출력합니다. (Pretty Print)

# "soup.find('a')"는 HTML 문서에서 "첫 번째"로 발견되는 "a" 태그 요소를 찾습니다.
# ".get_text()"는 해당 태그 안의 텍스트 콘텐츠("naver")만 가져옵니다.
soup.find('a').get_text()

# "soup.find_all('a')"는 HTML 문서에서 "모든" "a" 태그 요소를 리스트 형태로 찾습니다.
soup.find_all('a')

# 찾은 모든 "a" 태그 요소를 "site_names" 변수에 저장합니다.
site_names = soup.find_all('a')
# 리스트의 각 태그에 대해 반복합니다.
for site_name in site_names:
    print(site_name.get_text()) # 각 태그의 텍스트 콘텐츠("naver", "google", "daum")를 출력합니다.





# --- ID 속성으로 요소 찾기 (Finding Elements by ID Attribute) ---


# 새로운 HTML 코드를 정의합니다. 여러 개의 같은 태그("p")에 다른 "id" 속성이 할당되어 있습니다.
html2 = """<html> <head>  <title>작품과 작가 모음</title> </head> <body>  <h1>책 정보</h1>  <p id="book_title">토지</p>  <p id="author">박경리</p>    <p id="book_title">태백산맥</p>  <p id="author">조정래</p>  <p id="book_title">감옥으로부터의 사색</p><p id="author">신영복</p> </body></html>"""

soup2 = BeautifulSoup(html2, "lxml") # BeautifulSoup 객체를 생성합니다.

soup2 # 객체 자체를 출력합니다.

print(soup2.prettify()) # 보기 좋게 출력합니다.

print(soup2.title) # HTML 문서의 "<title>" 태그 전체를 출력합니다.

print(soup2.body) # HTML 문서의 "<body>" 태그 전체를 출력합니다.

print(soup2.body.h1) # "body" 태그 안의 "h1" 태그 전체를 출력합니다.

# 태그 이름이 "p"인 모든 요소를 리스트로 찾습니다.
print(soup2.find_all('p'))

# "p" 태그 중 "id" 속성이 "book_title"인 "첫 번째" 요소를 찾습니다.
print(soup2.find('p', {"id":"book_title"}))

# "p" 태그 중 "id" 속성이 "author"인 "첫 번째" 요소를 찾습니다.
print(soup2.find('p', {"id":"author"}))

# "p" 태그 중 "id" 속성이 "book_title"인 "모든" 요소를 리스트로 찾습니다.
print(soup2.find_all('p', {"id":"book_title"}))

# "p" 태그 중 "id" 속성이 "author"인 "모든" 요소를 리스트로 찾습니다.
print(soup2.find_all('p', {"id":"author"}))








# --- zip을 이용한 데이터 매칭 및 추출 (Data Matching and Extraction using zip) ---


soup2 = BeautifulSoup(html2, "lxml")
# 모든 책 제목 요소를 찾습니다.
book_titles = soup2.find_all('p', {"id":"book_title"})
# 모든 작가 이름 요소를 찾습니다.
authors = soup2.find_all('p', {"id":"author"})

# "zip" 함수를 사용하여 책 제목 리스트와 작가 이름 리스트의 요소를 순서대로 묶어 반복합니다.
for book_title, author in zip(book_titles, authors):
    # 각 요소에서 텍스트만 추출하여 "책제목/작가이름" 형태로 출력합니다.
    print(book_title.get_text() + '/' + author.get_text())






# --- CSS 선택자 (select) 사용 (Using CSS Selectors) ---


# CSS 선택자("select")를 사용하여 "body" 태그 아래의 "h1" 태그를 모두 찾습니다.
print(soup2.select('body h1'))

# CSS 선택자를 사용하여 "body" 태그 아래의 "p" 태그를 모두 찾습니다. (공백은 하위 요소를 의미)
print(soup2.select('body p'))

# 문서 내의 모든 "p" 태그를 찾습니다.
print(soup2.select('p'))

# "p" 태그 중에서 "id"가 "book_title"인 요소를 찾습니다. ("#"은 ID를 나타냄)
print(soup2.select('p#book_title'))

# "p" 태그 중에서 "id"가 "author"인 요소를 찾습니다.
print(soup2.select('p#author'))





# --- 파일에서 HTML 읽기 및 클래스/ID 선택자 사용 (Reading HTML from File and Class/ID Selectors) ---


# 'C:/Myexam/HTML_example_my_site.html' 파일을 UTF-8 인코딩으로 열어 "f"에 할당합니다.
f = open('C:/Myexam/HTML_example_my_site.html', encoding='utf-8')
html3 = f.read() # 파일의 내용을 모두 읽어 "html3"에 저장합니다.
f.close() # 파일을 닫습니다.
soup3 = BeautifulSoup(html3, "lxml") # BeautifulSoup 객체를 생성합니다.


print(soup3.select('a')) # 문서 내의 모든 "a" 태그를 찾습니다.

# "a" 태그 중에서 "class" 속성이 "portal"인 요소를 찾습니다. ("."은 클래스를 나타냄)
print(soup3.select('a.portal'))

# "a" 태그 중에서 "id" 속성이 "naver"인 요소를 찾습니다. ("#"은 ID를 나타냄)
print(soup3.select('a#naver'))





# --- 텍스트 추출 및 <br/> 태그 처리 - 1 (Text Extraction and $<br/>$ Handling - Part 1) ---


# 'C:/Myexam/br_example_constitution.html' 파일을 읽어옵니다.
f = open('C:/Myexam/br_example_constitution.html', encoding='utf-8')
html_source = f.read()
f.close()
soup = BeautifulSoup(html_source, "lxml")

# "id"가 "title"인 "p" 태그를 찾습니다.
title = soup.find('p', {"id":"title"})
# "id"가 "content"인 "p" 태그를 "모두" 찾습니다.
contents = soup.find_all('p', {"id":"content"})

print(title.get_text()) # 제목의 텍스트를 출력합니다.
# 내용 리스트를 반복하며 각 내용의 텍스트를 출력합니다.
for content in contents:
    print(content.get_text())

# 핵심 기능: 파일에서 데이터를 읽고, **find**와 **find_all**을 사용하여 제목과 내용을 추출합니다.



html1 = '<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나</p>'
soup1 = BeautifulSoup(html1, "lxml")

print("==> 태그 p로 찾은 요소")
content1 = soup1.find('p', {"id":"content"})
print(content1, "\n")

# 찾은 "content1" 태그 안에서 "첫 번째" "<br/>" 태그를 찾습니다.
br_content = content1.find("br")
print("==> 결과에서 태그 br로 찾은 요소:", br_content, "\n")

# 찾은 "<br/>" 태그를 Python의 개행 문자("\n")로 대체합니다.
br_content.replace_with("\n")
print("==> 태그 br을 개행문자로 바꾼 결과")
# 변경된 "content1" 태그를 출력합니다. (첫 번째 "<br/>"만 변경됨)
print(content1)

# 핵심 기능: replace_with("\n") 메서드를 사용하여 HTML의 줄 바꿈 태그인 **<br/>**을 텍스트 줄 바꿈(\n) 문자로 바꾸는 방법을 보여줍니다. 다만, 이 예시에서는 "첫 번째" <br/>만 처리됩니다.




# --- <br/> 태그 전체 처리 (Handling All $<br/>$ Tags) ---


soup2 = BeautifulSoup(html1, "lxml")
content2 = soup2.find('p', {"id":"content"})

# "content2" 태그 안에서 "모든" "<br/>" 태그를 리스트로 찾습니다.
br_contents = content2.find_all("br")

# 찾은 모든 "<br/>" 태그에 대해 반복합니다.
for br_content in br_contents:
    br_content.replace_with("\n") # 각 "<br/>" 태그를 개행 문자("\n")로 대체합니다.

# 모든 "<br/>"이 "\n"으로 대체된 최종 결과를 출력합니다.
print(content2)

# 핵심 기능: **find_all("br")**로 모든 <br/> 태그를 찾은 후, 
# for 루프를 돌면서 각각 **replace_with("\n")**를 적용하여 
# HTML 내용 안의 모든 줄 바꿈을 텍스트 형식으로 변경합니다. 
# 이는 텍스트 데이터를 깔끔하게 정리하는 데 유용합니다.





# --- replace_newline 함수 ---


def replace_newline(soup_html):
    # 함수 정의: HTML 파싱 객체(BeautifulSoup 객체)를 인수로 받습니다.
    # 인수로 받는 변수 이름은 "soup_html"이며, 함수 실행 후 변환된 객체를 반환합니다.

    # 1. 모든 <br> 태그 찾기
    # "soup_html" 객체에서 "find_all()" 메서드를 사용하여 HTML 문서 내의 모든 "<br>" 태그 요소를 찾습니다.
    # 찾은 모든 요소들은 리스트 형태로 "br_to_newlines" 변수에 저장됩니다.
    br_to_newlines = soup_html.find_all("br")

    # 2. 반복문을 사용한 태그 변환
    # "br_to_newlines" 리스트의 각 요소(각 "<br>" 태그)에 대해 반복합니다.
    for br_to_newline in br_to_newlines:
        # ".replace_with('\n')" 메서드를 사용합니다.
        # 현재 반복 중인 "<br>" 태그를 Python의 개행 문자("\n")로 "대체"합니다.
        # 이 작업은 원본 "soup_html" 객체에 직접 반영됩니다.
        br_to_newline.replace_with("\n")

    # 3. 변환된 객체 반환
    # 모든 `<br/>` 태그가 `\n`으로 대체되어 텍스트가 정리된 "soup_html" 객체를 반환합니다.
    return soup_html





# --- replace_newline 함수 적용 코드 ---

# 'html1' 변수에 저장된 HTML 문자열을 사용하여 새로운 BeautifulSoup 객체 "soup2"를 생성합니다.
# 이 객체는 이전 `<br/>` 처리의 영향을 받지 않은 초기 상태입니다.
# html1 = '<p id="content">제1조 <br/>①대한민국은 민주공화국이다.<br/>②대한민국의 주권은 국민에게 있고, 모든 권력은 국민으로부터 나</p>'
soup2 = BeautifulSoup(html1, "lxml")

# "soup2" 객체에서 "id" 속성이 "content"인 "p" 태그 요소를 찾습니다.
# 이 요소는 "<br/>" 태그들을 포함하고 있습니다.
content2 = soup2.find('p', {"id":"content"})

# 앞서 정의된 "replace_newline" 함수를 호출하여 "content2" 요소 내의 작업을 수행합니다.
# 1. 함수는 "content2" 객체 안의 모든 "<br/>" 태그를 찾습니다.
# 2. 각 "<br/>" 태그를 개행 문자("\n")로 대체합니다.
# 3. 변경된 객체를 반환하며, 이 결과가 "content3"에 저장됩니다. (content2와 content3는 같은 객체를 참조)
content3 = replace_newline(content2)

# 최종적으로, 변환 작업이 완료된 "content3" 객체에서 순수한 "텍스트 내용"만을 추출하여 출력합니다.
# get_text() 결과에는 "<br/>" 대신 삽입된 "\n" 문자열이 반영되어 줄 바꿈이 적용됩니다.
print(content3.get_text())

# 이 과정은 웹 스크래핑에서 **"HTML 줄 바꿈과 텍스트 줄 바꿈을 일치"**시키는 매우 실용적인 기술을 보여줍니다. 
# content2에서 get_text()를 바로 호출하면 모든 텍스트가 한 줄로 이어지지만, 
# replace_newline 함수를 적용함으로써 원본 HTML의 의도된 줄 바꿈을 텍스트 데이터에 그대로 반영할 수 있습니다.




# --- 파일 읽기 및 <br/> 처리 ---

# 'html_source' 변수에 저장된 HTML 전체 내용을 사용하여 BeautifulSoup 객체 "soup"를 새로 생성합니다.
# 이 HTML은 아마도 'C:/Myexam/br_example_constitution.html' 파일에서 읽어온 내용일 것입니다.
soup = BeautifulSoup(html_source, "lxml")

# 1. 제목(Title) 추출
# "id" 속성이 "title"인 "p" 태그 요소를 문서 전체에서 "첫 번째"로 찾아 "title" 변수에 저장합니다.
title = soup.find('p', {"id":"title"})

# 2. 내용(Contents) 추출
# "id" 속성이 "content"인 "p" 태그 요소를 문서 전체에서 "모두" 찾아 리스트 형태로 "contents" 변수에 저장합니다.
contents = soup.find_all('p', {"id":"content"})

# 3. 제목 출력
# 찾은 제목 요소에서 순수한 텍스트만 추출하여 출력합니다.
# 출력 후, 다음 내용과의 구분을 위해 두 줄(\n)을 띄웁니다. (title.get_text() + '\n')
print(title.get_text(), '\n')

# 4. 내용 반복 처리 및 출력
# 내용 리스트("contents")의 각 요소(예: 각 조항의 내용)에 대해 반복합니다.
for content in contents:
    # 현재 내용 요소("content")를 앞서 정의된 "replace_newline" 함수에 전달합니다.
    # 함수 내에서 해당 요소의 모든 "<br/>" 태그가 "\n"으로 대체되어 텍스트가 정리됩니다.
    # 변환된 결과(content1)는 원본 객체와 동일하며, 정리된 HTML 조각을 담고 있습니다.
    content1 = replace_newline(content)

    # 정리된 HTML 조각("content1")에서 순수한 텍스트를 추출하여 출력합니다.
    # 출력 후, 다음 조항과의 구분을 위해 한 줄(\n)을 띄웁니다.
    print(content1.get_text(),'\n')
    
    
    
    
    
    
    
    
# --- 이미지 파일 다운로드 ---    
    
# 1. 이미지 URL 정의
# 다운로드하려는 이미지 파일의 전체 URL을 문자열로 'url' 변수에 저장합니다.
# 이 URL은 Python 공식 웹사이트의 로고 이미지(.png 파일)를 가리킵니다.
url = 'https://www.python.org/static/img/python-logo.png'

# 2. HTTP GET 요청 전송 및 응답 객체 저장
# 'requests.get(url)' 함수를 사용하여 해당 URL로 HTTP GET 요청을 보냅니다.
# 웹 서버는 이 요청에 대한 응답으로 이미지 파일의 바이너리 데이터를 포함하는 "Response 객체"를 반환합니다.
# 이 객체는 'html_image' 변수에 저장됩니다.
html_image = requests.get(url)

# 3. 응답 객체 출력
# Response 객체('html_image') 자체를 출력합니다.
# 이 코드는 서버로부터 요청이 성공했는지 여부를 즉시 확인하는 데 사용됩니다.
print(html_image)








# --- 파일 이름 추출 --- 

# 1. 파일 이름 추출
# 'os.path.basename(url)' 함수를 호출합니다.
# 이 함수는 주어진 경로(여기서는 URL)에서 **"가장 마지막 요소"**, 즉 **파일 이름**을 반환합니다.
# URL의 경로 구분자('/') 이후의 모든 문자열('python-logo.png')이 추출되어 'image_file_name' 변수에 저장됩니다.
image_file_name = os.path.basename(url)
print(image_file_name)