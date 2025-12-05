import webbrowser
import os
import requests
import bs4
from urllib.request import urlopen # 사이트에 요청 신호를 보내는 함수
import pandas as pd


# --- 1. "Tistory 요청 및 응답 분석" (Tistory Request and Analysis) ----

# Tistory 홈페이지의 URL을 'url' 변수에 저장합니다.
url = 'https://www.tistory.com'

# "requests.get(url)" 함수를 사용하여 해당 URL로 HTTP GET 요청을 보냅니다.
# 서버로부터 받은 "Response 객체"를 'response' 변수에 저장합니다.
response = requests.get(url)

# Response 객체의 "status_code" 속성을 출력합니다.
# "status_code"는 요청의 성공/실패 여부를 나타내는 HTTP 응답 코드입니다.
# "200"이 출력되면 요청이 "성공적"이었음을 의미합니다.
print(response.status_code)

# Response 객체의 "text" 속성(응답으로 받은 HTML 소스 코드) 중 
# 인덱스 5036부터 6983까지의 문자열 조각을 잘라내어 출력합니다.
# 이 코드는 웹페이지의 "특정 부분"만 확인하고자 할 때 사용됩니다.
print(response.text[5036:6983])





# --- 2. "Google 요청 및 응답 분석" (Google Request and Analysis) ---

# Google Korea로 HTTP GET 요청을 보내고, Response 객체를 'r' 변수에 저장합니다.
r = requests.get("https://www.google.co.kr")

# Response 객체 자체를 출력합니다. (예: "<Response [200]>")
print(r)

# Response 객체의 "text" 속성(HTML 소스 코드 전체)을 출력합니다.
# Google의 HTML은 대부분 JavaScript로 이루어져 있어 읽기 어려울 수 있습니다.
print(r.text)

# Response 객체의 HTML 소스 코드 문자열의 "총 길이"(문자 수)를 출력합니다.
print(len(r.text))

# HTML 소스 코드의 "앞에서 100자"까지만 잘라내어 출력합니다.
# 이는 응답이 제대로 왔는지 빠르게 확인하는 용도로 사용됩니다.
print(r.text[0:100])




# --- 3. "Naver 요청 및 응답 분석" (Naver Request and Analysis) ---


# Naver 홈페이지의 URL을 'url' 변수에 저장합니다.
url = 'http://www.naver.com'

# Naver로 HTTP GET 요청을 보내고, Response 객체를 'res' 변수에 저장합니다.
res = requests.get(url)

# Response 객체의 "status_code"를 출력합니다. ("200"이면 성공)
print(res.status_code)

# Response 객체의 "text" 속성(HTML 소스 코드 전체)을 출력합니다.
print(res.text)

# HTML 소스 코드 문자열의 "총 길이"를 출력합니다.
print(len(res.text))








# --- "requests" 모듈을 이용한 GET 요청 방식 ---



# 1. "URL에 직접 파라미터 포함" 방식 (Direct Parameter in URL)

# 네이버 스포츠 뉴스의 기본 URL을 'base_url' 변수에 저장합니다.
base_url = "https://sports.news.naver.com/news" 

# 쿼리 스트링(Query String, 파라미터)이 "직접 포함된" 최종 URL을 'param_url' 변수에 저장합니다.
# '?' 뒤의 'oid=079&aid=0004089508' 부분이 서버로 전달할 데이터(파라미터)입니다.
param_url ="https://sports.news.naver.com/news?oid=079&aid=0004089508"



# "requests.get(param_url)"을 사용하여 파라미터가 포함된 전체 URL로 HTTP GET 요청을 보냅니다.
res1 = requests.get(param_url)

# Response 객체 'res1'의 "status_code"를 출력합니다.
# "200"이 출력되면 요청이 "성공적"이었음을 의미하며, 페이지 데이터를 정상적으로 받았다는 뜻입니다.
print(res1.status_code)



# 2. "params 인수를 사용한 파라미터 전달" 방식 (Using the params Argument)

# 네이버 스포츠 뉴스의 기본 URL입니다. (쿼리 스트링은 포함하지 않습니다.)
# base_url = "https://sports.news.naver.com/news" 

# 서버로 전달할 파라미터를 Python "딕셔너리" 형태로 정의합니다.
# key: value 쌍이 웹의 파라미터 이름과 값으로 매핑됩니다.
param = {'oid':'079', 'aid':'0004089508'}

# "requests.get(base_url, params=param)" 함수를 사용하여 GET 요청을 보냅니다.
# "requests" 모듈이 "base_url" 뒤에 딕셔너리 'param'의 내용을 자동으로 붙여 쿼리 스트링을 완성합니다.
# 즉, requests가 내부적으로 'base_url?oid=079&aid=0004089508' 형태의 URL을 만들어 요청합니다.
# 이 방식은 한글이나 특수문자가 포함된 파라미터 처리(URL 인코딩) 시 "매우 안전"하고 "가독성"이 좋습니다.
res2 = requests.get(base_url, params=param)

# Response 객체 'res2'의 "status_code"를 출력합니다. (역시 "200"이 예상됩니다.)
print(res2.status_code)






# --- URL 연결 및 데이터 읽기 ---


# 1. "URL 연결 및 응답 객체 확인" (URL Connection and Response Object)

# 네이버 홈페이지의 URL을 'url' 변수에 저장합니다.
url ='http://www.naver.com'

# "urlopen(url)" 함수를 사용하여 해당 URL로 연결을 시도하고,
# 서버로부터 받은 "HTTPResponse 객체"를 'html' 변수에 저장합니다.
# 이 객체는 웹 서버와의 연결을 나타냅니다.
# ⚠️ 주의: 이 코드는 'urlopen'이 임포트되었다고 가정합니다.
html = urlopen(url)

# "HTTPResponse 객체"인 'html' 변수의 정보를 출력합니다.
# 출력 결과는 보통 <http.client.HTTPResponse object at 0x...> 형태로 나타나며,
# 이는 서버와의 연결이 성공했음을 의미합니다.
print(html)





# 2. "바이너리 데이터 읽기 및 타입 확인" (Reading Binary Data and Type Check)


# 'html' 객체(HTTPResponse)의 ".read()" 메서드를 사용하여 
# 서버가 보낸 응답 본문(HTML 소스 코드) "전체"를 읽어 'rawtext'에 저장합니다.
# 웹에서 읽어온 데이터는 기본적으로 "바이너리(bytes)" 형태로 저장됩니다.
rawtext = html.read()

# 'rawtext' 변수의 "타입"을 출력합니다.
# 출력 결과는 "<class 'bytes'>"이며, 이는 데이터가 0과 1로 이루어진 "바이트 시퀀스"임을 나타냅니다.
print(type(rawtext))

# 'rawtext' 변수의 "타입"을 출력하고 줄 바꿈 문자를 추가합니다. (재확인)
print(type(rawtext),"\n")

# 'rawtext' 변수를 "bytes" 타입으로 변환(이미 bytes 타입이므로 형태 유지)하고, 
# 데이터의 "앞에서 200 바이트"까지만 잘라내어 출력합니다.
# 바이너리 데이터는 사람이 읽을 수 없는 형태로 보입니다 (예: b'<!DOCTYPE html>...').
print(bytes(rawtext)[:200], "\n")

# 'rawtext' (바이너리 데이터)를 ".decode('utf8')" 메서드를 사용하여 
# 'utf8' 인코딩 방식에 따라 "문자열(string)"로 변환합니다.
# 변환된 문자열의 "앞에서 200자"까지만 잘라내어 출력합니다.
# 이제 데이터가 사람이 읽을 수 있는 HTML 텍스트 형태로 출력됩니다.
print(rawtext.decode('utf8')[:200])


# "핵심 개념: 바이트 vs 문자열"
#  - 웹에서 데이터를 읽어오면 항상 "바이트(bytes)" 형태로 받게 됩니다.
#  - **"바이트"**는 컴퓨터가 이해하는 0과 1의 시퀀스이며, 파일 저장이나 네트워크 전송에 사용됩니다.
#  - 우리가 읽을 수 있는 텍스트로 사용하려면 .decode() 메서드를 사용하여 특정 인코딩(여기서는 utf8)을 통해 **"문자열(str)"**로 변환해야 합니다.





# --- URL 연결, 데이터 읽기 및 BeautifulSoup 파싱 ---



# 1. "URL 연결 및 응답 객체 확인" (URL Connection and Response Object)

# 네이버 홈페이지의 URL을 'url' 변수에 저장합니다.
url = 'http://www.naver.com'

# "urlopen(url)" 함수를 사용하여 해당 URL로 연결을 시도하고,
# 서버로부터 받은 "HTTPResponse 객체"를 'html' 변수에 저장합니다.
# 이 객체는 웹 서버와의 "활성 연결"을 나타냅니다.
# 주의: 'urlopen'은 urllib.request 모듈에 속합니다.
html = urlopen(url)

# "HTTPResponse 객체"인 'html' 변수의 정보를 출력합니다.
# 출력 결과는 <http.client.HTTPResponse object at 0x...> 형태이며, 
# 이는 서버와의 연결이 "성공적"이었음을 의미합니다.
print(html)


# 2. "BeautifulSoup 객체 생성 및 타입 확인" (BeautifulSoup Object Creation and Type Check)

# "bs4.BeautifulSoup()" 생성자를 사용하여 HTML 파싱 객체를 만듭니다.
# 첫 번째 인수인 'html' (HTTPResponse 객체)에서 HTML 데이터를 읽어옵니다.
# 두 번째 인수인 'html.parser'는 파이썬 표준 라이브러리에 포함된 "HTML 파서"를 사용하도록 지정합니다.
# 파싱된 구조화된 객체는 'bs_obj' 변수에 저장됩니다.
bs_obj = bs4.BeautifulSoup(html,'html.parser')

# 'bs_obj' 변수의 "타입"을 출력합니다.
# 출력 결과는 "<class 'bs4.BeautifulSoup'>"이며, 이는 데이터가 
# 웹 스크래핑에 용이한 "BeautifulSoup 객체"로 변환되었음을 나타냅니다.
print(type(bs_obj))


# 3. "HTML 구조 출력" (Pretty HTML Output)

# 'bs_obj' 객체의 ".prettify()" 메서드를 호출합니다.
# 이 메서드는 파싱된 HTML 구조를 "보기 좋게 들여쓰기"하고 정렬된 문자열로 반환합니다.
# 반환된 문자열의 "앞에서 2468자"까지만 잘라내어 출력합니다.
# 이 출력은 웹페이지의 "구조화된 소스 코드"를 보여주며, 태그와 계층 구조를 쉽게 파악할 수 있게 해줍니다.
print(bs_obj.prettify()[:2468])








# 문자열 HTML 파싱 및 BeautifulSoup 객체 확인

# 1. "HTML 문자열 정의" (HTML String Definition)
html_str = "<!DOCTYPE html><html><div>hello</div></html>"


# 2. "BeautifulSoup 객체 생성 및 타입 확인" (BeautifulSoup Object Creation and Type Check)

# bs4.BeautifulSoup() 생성자를 사용하여 파싱 객체를 만듭니다.
# 첫 번째 인수인 'html_str'은 분석할 HTML 문자열입니다.
# 두 번째 인수인 'html.parser'는 Python 표준 라이브러리에 내장된 "HTML 파서"를 사용하도록 지정합니다.
# 파싱된 구조화된 객체는 'bs_obj' 변수에 저장됩니다.
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

# 'bs_obj' 변수의 "타입"을 출력합니다.
# 출력 결과는 "<class 'bs4.BeautifulSoup'>"이며, 이는 HTML 문자열이 
# 성공적으로 "BeautifulSoup 객체"로 변환되어 데이터 추출 준비가 완료되었음을 나타냅니다.
print(type(bs_obj))

# 생성된 'bs_obj' 객체의 내용 전체를 출력합니다.
# BeautifulSoup이 <html> 태그를 인식하고 내부 구조를 포함하여 출력하는 것을 볼 수 있습니다.
print(bs_obj)


# 3. "데이터 검색 및 텍스트 추출" (Data Search and Text Extraction)

# 'bs_obj' 객체의 ".find('div')" 메서드를 호출합니다.
# 이는 BeautifulSoup 트리 구조에서 "첫 번째로 발견되는 'div' 태그 요소"를 찾아 반환합니다.
# 출력 결과는 <div>hello</div> 형태의 태그 객체입니다.
print(bs_obj.find('div'))

# ".find('div')"로 찾은 'div' 태그 객체 뒤에 ".text" 속성을 붙입니다.
# ".text" 속성은 해당 태그 객체가 포함하고 있는 "순수한 텍스트 내용"만을 추출합니다.
# 출력 결과는 'hello' 문자열입니다.
print(bs_obj.find('div').text)



# --- BeautifulSoup을 이용한 데이터 목록(List) 추출 ---


# 1. "HTML 문자열 정의 및 객체 생성" (HTML Definition and Object Creation)

# 여러 개의 목록 항목(<li>)을 포함하는 HTML 문자열을 정의합니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""

# BeautifulSoup 객체를 생성합니다.
# 'html_str' 문자열을 'html.parser'를 사용하여 분석하고, 그 결과를 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str,'html.parser')



# 2. "최상위 목록 태그 검색" (Finding the Top-Level List Tag)

# "bs_obj.find('ul')" 메서드를 사용하여 문서에서 "첫 번째로 발견되는 'ul' 태그 요소" 전체를 찾습니다.
# 'ul_t' 변수는 <ul>...</ul> 전체를 포함하는 BeautifulSoup 태그 객체가 됩니다.
ul_t = bs_obj.find('ul')
# 찾은 'ul' 태그 객체의 전체 내용을 출력합니다.
print(ul_t)

# 'ul_t' 객체 내에서 ".find('li')" 메서드를 사용하여 "첫 번째로 발견되는 'li' 태그 요소"를 찾습니다.
# 출력 없이 실행되었지만, 결과는 '<li>hello</li>' 객체가 됩니다.
ul_t.find('li')



# 3. "모든 목록 항목 추출" (Extracting All List Items)

# 'ul_t' 객체 내에서 ".findAll('li')" 메서드를 사용하여 "모든 'li' 태그 요소"를 검색합니다.
# 찾은 모든 요소는 리스트 형태로 'uls' 변수에 저장됩니다.
uls = ul_t.findAll('li')
# 'uls' 리스트의 내용을 출력합니다. (각 <li> 태그 객체들이 리스트의 요소로 포함됨)
print(uls)


# 'uls' 리스트의 "세 번째 요소" (인덱스 2)의 "타입"을 출력합니다.
# 출력 결과는 "<class 'bs4.element.Tag'>"로, 리스트 요소가 태그 객체임을 보여줍니다.
print(type(uls[2]))
# 세 번째 'li' 태그 객체에서 ".text" 속성을 사용하여 "순수한 텍스트"('welcome')만 추출하여 출력합니다.
print(uls[2].text)


# 'uls' 리스트의 각 'li' 태그 객체에 대해 반복문(for loop)을 실행합니다.
for li in uls :
    # 각 'li' 객체에서 ".text"를 사용하여 텍스트 내용을 추출하고 출력합니다.
    # 이 과정으로 'hello', 'bye', 'welcome'이 각각 한 줄씩 출력됩니다.
    print(li.text)
    
    
    
    
# 4. "전체 텍스트 추출 및 정제" (Full Text Extraction and Cleaning)     

# 'ul_t' 객체 전체에서 ".text" 속성을 사용하여 "모든 하위 태그의 텍스트"를 한 번에 추출합니다.
# 이 과정에서 HTML의 공백(개행 문자, 탭 등)도 텍스트에 포함되어 추출됩니다.
print(ul_t.text)

# 'ul_t.text'의 결과 문자열을 Python의 ".split('\n')" 메서드를 사용하여 "개행 문자('\n') 기준"으로 나눕니다.
# 결과는 불필요한 공백 문자열이 포함된 리스트가 됩니다.
print(ul_t.text.split('\n'))







# --- BeautifulSoup 클래스 및 복합 조건 검색 ---



# 1. "HTML 문자열 정의 및 객체 생성" (HTML Definition and Object Creation)



# 'greet'과 'reply' 두 개의 다른 클래스를 가진 <ul> 목록을 포함하는 HTML 문자열을 정의합니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <ul class="greet">
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
        <ul class="reply">
            <li>ok</li>
            <li>no</li>
            <li>sure</li>
        </ul>
    </body>
</html>
"""
# BeautifulSoup 객체를 생성합니다. 'html_str'을 'html.parser'로 분석하고 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str,'html.parser')



# 2. "단일 요소 검색 (find)" (Single Element Search)

# bs_obj.find('ul')
# 문서에서 "첫 번째로 발견되는" 'ul' 태그 요소를 찾습니다.
# 결과는 클래스가 'greet'인 <ul> 요소입니다.
bs_obj.find('ul')

# bs_obj.find('ul',{'class':'greet'})
# 'ul' 태그 중에서, 속성 딕셔너리 {'class':'greet'}와 "일치하는" 첫 번째 요소를 찾습니다.
# 이는 'greet' 클래스를 가진 <ul> 요소를 정확하게 지정하여 찾습니다.
bs_obj.find('ul',{'class':'greet'})




# 3. "모든 요소 검색 (findAll)" (Multiple Element Search)

# bs_obj.findAll('ul')[1]
# 문서에서 "모든" 'ul' 태그 요소를 리스트로 찾은 후, 그 리스트의 "두 번째 요소" (인덱스 1)를 선택합니다.
# 결과는 클래스가 'reply'인 <ul> 요소입니다.
bs_obj.findAll('ul')[1]

# bs_obj.find('ul',{'class':'reply'}) 
# 'ul' 태그 중에서, 클래스가 'reply'인 "첫 번째" 요소를 찾습니다.
# 'reply' 클래스를 가진 <ul> 요소가 하나밖에 없으므로, 이를 정확히 반환합니다.
bs_obj.find('ul',{'class':'reply'}) 

# bs_obj.findAll('ul',{'class':'reply'})
# 'ul' 태그 중에서, 클래스가 'reply'인 "모든" 요소를 찾아 리스트로 반환합니다.
# 이 경우, 요소가 하나이므로, 그 하나를 담은 리스트가 반환됩니다.
bs_obj.findAll('ul',{'class':'reply'})



# 4. "일반 태그 검색 및 별칭 사용" (General Tag Search and Aliases)


# bs_obj.find_all('li')
# 문서 전체에서 "모든" 'li' 태그 요소를 찾아 리스트로 반환합니다. (hello, bye, welcome, ok, no, sure 모두 포함)
bs_obj.find_all('li')

# bs_obj.findAll('li')
# 'findAll'은 'find_all'의 "별칭(alias)"입니다. 기능은 완전히 동일하며, 문서의 모든 'li' 태그를 반환합니다.
bs_obj.findAll('li')


# bs_obj.find_all('ul')
# 문서 전체에서 "모든" 'ul' 태그 요소를 찾아 리스트로 반환합니다. ('greet'과 'reply' 두 개 모두 포함)
bs_obj.find_all('ul')





# 5. "계층적 검색 (Method Chaining)" (Hierarchical Search)


# bs_obj.find('ul').find_all('li')
# 1단계: "첫 번째 'ul'" 태그('greet' 클래스)를 찾습니다.
# 2단계: 그 찾은 'ul' 태그 내부에서 "모든 'li'" 태그를 찾습니다. (hello, bye, welcome)
# 이는 특정 부모 태그 내부의 자식 요소들을 추출하는 "대표적인 방식"입니다.
bs_obj.find('ul').find_all('li')

# bs_obj.find_all('ul')[0].find_all('li')
# 1단계: "모든 'ul'" 태그를 리스트로 찾고, 그 리스트의 "첫 번째 요소" (인덱스 0, 'greet' 클래스)를 선택합니다.
# 2단계: 그 'ul' 태그 내부에서 "모든 'li'" 태그를 찾습니다. (hello, bye, welcome)
bs_obj.find_all('ul')[0].find_all('li')

# bs_obj.find('ul',{'class':'greet'}).find_all('li')
# 1단계: 클래스가 'greet'인 'ul' 태그를 "정확하게 지정"하여 찾습니다.
# 2단계: 그 'ul' 태그 내부에서 "모든 'li'" 태그를 찾습니다. (hello, bye, welcome)
bs_obj.find('ul',{'class':'greet'}).find_all('li')

# bs_obj.find_all('ul',{'class':'greet'})[0].find_all('li')
# 1단계: 클래스가 'greet'인 'ul' 태그를 모두 찾아 리스트로 얻고, "첫 번째 요소"를 선택합니다.
# 2단계: 그 'ul' 태그 내부에서 "모든 'li'" 태그를 찾습니다. (hello, bye, welcome)
bs_obj.find_all('ul',{'class':'greet'})[0].find_all('li')


# "핵심 요약"
# 가장 중요한 패턴은 **find('parent_tag', {...})**를 사용하여 원하는 부모 요소를 정확히 찾아낸 후, 
# **.find_all('child_tag')**를 체인 형태로 연결하여 그 하위의 모든 데이터를 효율적으로 추출하는 "계층적 검색" 방식입니다.







# --- BeautifulSoup ID 속성 기반 검색 ---



# 1. "HTML 문자열 정의 및 객체 생성" (HTML Definition and Object Creation)

# 'id' 속성(title, crawling, parsing)을 가진 여러 태그를 포함하는 HTML 문자열을 정의합니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <h1 id='title'>Hello Python</h1>
        <p id="crawling">웹 크롤링</p>
        <p id="parsing">파싱</p>
    </body>
</html>
"""

# BeautifulSoup 객체를 생성합니다.
# 'html_str' 문자열을 'html.parser'를 사용하여 분석하고, 그 결과를 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str, 'html.parser')



# 2. "ID 속성을 사용한 단일 요소 검색" (Single Element Search using ID)

# bs_obj.find('h1',{'id':'title'})
# 1단계: 검색할 태그 이름('h1')을 지정합니다.
# 2단계: "딕셔너리 형태"의 속성 조건 {'id':'title'}을 지정하여 해당 조건을 만족하는 요소를 찾습니다.
# 결과는 "id가 'title'인 첫 번째 'h1' 태그" (<h1>Hello Python</h1>)가 됩니다.
bs_obj.find('h1',{'id':'title'})

# bs_obj.find('p',{'id':'parsing'})
# 1단계: 검색할 태그 이름('p')을 지정합니다.
# 2단계: 속성 조건 {'id':'parsing'}을 지정하여 해당 조건을 만족하는 요소를 찾습니다.
# 결과는 "id가 'parsing'인 첫 번째 'p' 태그" (<p id="parsing">파싱</p>)가 됩니다.
bs_obj.find('p',{'id':'parsing'})



# "핵심 요약"
# HTML에서 **id**는 일반적으로 문서 내에서 **"유일성"**을 보장하는 식별자입니다. 
# 따라서 find(tag, {'id': 'id_value'}) 형태는 특정 태그 중에서 "가장 정확하고 빠르게" 
# 원하는 하나의 요소를 찾아내는 데 매우 효과적인 방법입니다.







# --- BeautifulSoup 형제 요소 탐색 ---


# 1. "HTML 문자열 정의 및 객체 생성" (HTML Definition and Object Creation) 

# 여러 개의 연속된 <p> 태그를 포함하는 HTML 문자열을 정의합니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <h1>파이썬 프로그래밍</h1>
        <p>웹 페이지 분석</p><p>크롤링</p><p>파싱</p>        
    </body>
</html>
"""

# BeautifulSoup 객체를 생성합니다.
# 'html_str' 문자열을 'html.parser'를 사용하여 분석하고, 그 결과를 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str, 'html.parser')





# 2. "태그 검색" (Tag Search)

# bs_obj.find('p')
# 문서에서 "첫 번째로 발견되는" '<p>' 태그 요소를 찾습니다.
# 결과는 <p>웹 페이지 분석</p> 태그 객체가 됩니다.
bs_obj.find('p')

# bs_obj.find_all('p')
# 문서 전체에서 "모든" '<p>' 태그 요소를 찾아 리스트 형태로 반환합니다.
# 결과는 [<p>웹 페이지 분석</p>, <p>크롤링</p>, <p>파싱</p>] 리스트가 됩니다.
bs_obj.find_all('p')




# 3. "형제 요소 탐색 (next_sibling)" (Sibling Element Navigation)

# "첫 번째 '<p>' 태그" (<p>웹 페이지 분석</p>)를 찾아서 'p1' 변수에 저장합니다.
p1 = bs_obj.find('p')

# print(p1.next_sibling)
# 'p1' (첫 번째 <p> 태그)의 "바로 다음 형제 요소"를 출력합니다.
# HTML 소스에서 첫 번째 <p> 바로 뒤에는 두 번째 <p> 태그가 붙어 있습니다.
# 따라서, "다음 형제 요소"는 <p>크롤링</p> 태그 객체가 됩니다.
print(p1.next_sibling)

# print(p1.next_sibling.next_sibling)
# 1단계: 'p1'의 "다음 형제" (<p>크롤링</p>)를 찾습니다.
# 2단계: 그 "다음 형제" (<p>크롤링</p>)의 "또 다음 형제"를 찾습니다.
# 결과는 세 번째 <p> 태그인 <p>파싱</p> 태그 객체가 됩니다.
# 이는 동일한 부모('body') 아래에 있는 요소를 "순차적으로 이동"하며 탐색하는 방법입니다.
print(p1.next_sibling.next_sibling)


# "핵심 요약"

# **next_sibling**은 BeautifulSoup에서 **"DOM 트리 구조상 같은 부모 아래에 있는 다음 요소"**로 이동할 때 사용됩니다. 
# 만약 HTML 소스에서 태그 사이에 공백이나 개행 문자(줄 바꿈)가 있다면, 
# **next_sibling**은 태그 객체가 아닌 "NavigableString(문자열)" 객체를 반환할 수 있으므로 주의해야 합니다. 
# 이 예시에서는 <p> 태그들이 공백 없이 붙어있어 바로 다음 <p> 태그를 반환했습니다.











# --- BeautifulSoup을 이용한 하이퍼링크 데이터 추출 및 DataFrame 생성 ---



# 1. "HTML 정의 및 BeautifulSoup 객체 생성" (HTML Definition and Parsing)

# 클래스가 'ko'와 'sns'인 두 개의 <ul> 목록에 여러 개의 하이퍼링크(<a> 태그)를 포함하는 HTML 문자열을 정의합니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <ul class="ko">
            <li><a href="https://www.naver.com/">네이버</a></li>
            <li><a href="https://www.daum.net/">다음</a></li>
        </ul>
        <ul class="sns">
            <li><a href="https://www.goole.com/">구글</a></li>
            <li><a href="https://www.facebook.net/">페이스북</a></li>
        </ul>
    </body>
</html>
"""

# BeautifulSoup 객체를 생성합니다. 'html_str'을 'html.parser'로 분석하고 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str,'html.parser')




# 2. "태그 검색 및 기본 속성 추출" (Tag Search and Basic Attribute Extraction)


# bs_obj.find_all('li')
# 문서 전체에서 "모든 'li' 태그 요소"를 찾아 리스트로 반환합니다. (총 4개)
bs_obj.find_all('li')

# bs_obj.find_all('a')
# 문서 전체에서 "모든 'a' 태그 요소" (하이퍼링크)를 찾아 리스트로 반환합니다. (총 4개)
bs_obj.find_all('a')


# bs_obj.find_all('a')[0]['href']
# 1단계: 모든 <a> 태그를 찾습니다.
# 2단계: 리스트의 "첫 번째 요소" (인덱스 0, 네이버 링크)를 선택합니다.
# 3단계: 태그 객체에 "딕셔너리처럼 접근"하여 'href' 속성 값(URL 문자열)을 추출합니다.
bs_obj.find_all('a')[0]['href']

# bs_obj.find_all('a')[0].text
# 1단계: 첫 번째 <a> 태그 요소를 선택합니다.
# 2단계: ".text" 속성을 사용하여 태그 안의 "순수한 텍스트"('네이버')를 추출합니다.
bs_obj.find_all('a')[0].text




# 3. "반복문을 이용한 URL 추출" (Extracting URLs via Loop)

hrefs=[] # 추출한 URL을 저장할 빈 리스트를 초기화합니다.
# bs_obj.find_all('a')를 사용하여 찾은 모든 <a> 태그 요소에 대해 반복합니다.
for a in bs_obj.find_all('a') :
    # 현재 <a> 태그의 'href' 속성 값을 추출하여 출력합니다.
    print(a['href'])
    # 추출한 URL을 'hrefs' 리스트에 추가합니다.
    hrefs.append(a['href'])


# 이전 리스트를 재사용하기 위해 초기화하고, 이름 저장을 위한 'name' 리스트도 초기화합니다.
hrefs=[]
name = []
# 모든 <a> 태그에 대해 다시 반복합니다.
for a in bs_obj.find_all('a') :
    # 현재 <a> 태그의 텍스트(사이트 이름)를 'name' 리스트에 추가합니다.
    name.append(a.text)
    # 현재 <a> 태그의 'href' 속성(URL)을 'hrefs' 리스트에 추가합니다.
    hrefs.append(a['href'])


# 최종적으로 추출된 두 리스트 ('hrefs'와 'name')의 내용을 출력합니다.
print(f"hrefs : {hrefs}, name : {name}")




# pd.DataFrame() 생성자를 사용하여 최종 데이터 프레임을 생성합니다.
# 딕셔너리를 인수로 전달하며, 딕셔너리의 "키"는 DataFrame의 "컬럼 이름"이 되고,
# "값"은 추출된 리스트('name', 'hrefs')가 됩니다.
pd.DataFrame(
    {
        'site명' : name, 
        'siteURL' : hrefs
    }
)
# 결과는 사이트 이름과 URL이 깔끔하게 정리된 표 형태의 데이터 프레임입니다.


# "핵심 요약"
# 이 코드는 웹 스크래핑의 실용적인 최종 단계를 보여줍니다. 
# **find_all('a')**를 통해 반복되는 데이터를 추출하고, 
# 반복문을 사용하여 **"텍스트 내용 (.text)"**과 **"속성 값 (['속성명'])"**을 동시에 리스트에 저장한 후, 
# Pandas를 이용해 이 데이터를 구조화된 테이블 형태로 변환합니다.








# --- BeautifulSoup CSS 선택자(Selector)를 이용한 데이터 추출 ---



# 1. "HTML 정의 및 BeautifulSoup 객체 생성" (HTML Definition and Object Creation)

# 여러 <div>, <ul>, <table>, <a>, <img> 태그와 ID 및 클래스 속성을 포함하는 복잡한 HTML 구조입니다.
html_str = """
<!DOCTYPE html>
<html>
    <body>
        <div id="wrap">
            <div id="mainMenuBox">                  
                <ul> 
                    <li><a href="#">패션잡화</a></li>    
                    <li><a href="#">주방용품</a></li>                      
                    <li><a href="#">생활건강</a></li>
                    <li><a href="#">DIY가구</a></li>
                </ul>
            </div>
            <div>
                <table>
                    <tr>
                        <td><img src="shoes1.jpg"></td>
                        <td><img src="shoes2.jpg"></td>
                        <td><img src="shoes3.jpg"></td>
                    </tr>
                    <tr id="prdName">
                        <td>솔로이스트<br>걸리쉬 리본단화</td>
                        <td>맥컬린<br>그레이가보시스트랩 펌프스</td>
                        <td>맥컬린<br>섹슈얼인사이드펌프스</td>
                    </tr>
                    <tr id="price">
                        <td>100,000원</td>
                        <td>200,000원</td>
                        <td>120,000원</td>
                    </tr>
                </table>
            </div>
            <div id="out_box">
                <div class="box">
                    <h4>공지사항</h4>
                    <hr>
                    <a href="#">[배송] : 무표배송 변경 안내 18.10.20</a><br>
                    <a href="#">[전시] : DIY 가구 전시 안내 18.10.31</a><br>
                    <a href="#">[판매] : 11월 특가 상품 안내 18.11.05</a>                      
                </div>
                <div class="box">
                    <h4>커뮤니티</h4>
                    <hr>
                    <a href="#">[레시피] : 살 안찌는 야식 만들기</a><br>
                    <a href="#">[가구] : 헌집 새집 베스트 가구</a><br>
                    <a href="#">[후기] : 배송이 잘못 됐어요 ㅠㅠ</a><br>
                </div>
            </div>          
        </div>
    </body>
</html>
"""

# BeautifulSoup 객체를 생성합니다. HTML 문자열을 'html.parser'로 분석하고 'bs_obj'에 저장합니다.
bs_obj = bs4.BeautifulSoup(html_str,'html.parser')



# 2. "기본 검색 및 선택자 활용" (Basic Search and Selector Usage)

# bs_obj.findAll("a")
# find_all() 메서드를 사용하여 문서 전체의 "모든 <a> 태그"를 찾아 리스트로 반환합니다. (총 10개)
bs_obj.findAll("a")

# bs_obj.select('a')
# select() 메서드를 사용하여 CSS 선택자 'a'와 일치하는 "모든 <a> 태그"를 찾아 리스트로 반환합니다. (findAll과 동일 결과)
bs_obj.select('a')

# bs_obj.select('div')
# select() 메서드를 사용하여 문서 전체의 "모든 <div> 태그"를 찾아 리스트로 반환합니다. (총 5개: wrap, mainMenuBox, unnamed div, out_box, 2개의 box 클래스)
bs_obj.select('div')



# 3. "ID 및 계층 선택자" (ID and Hierarchical Selectors)

# bs_obj.select('div #mainMenuBox')
# 'div' 태그의 후손(descendant) 중에서 "ID가 mainMenuBox인 요소"를 찾습니다. (공백은 후손 선택자)
bs_obj.select('div #mainMenuBox')

# bs_obj.select('#mainMenuBox')
# "ID가 mainMenuBox인 요소"를 바로 찾습니다. (ID 선택자 #을 사용)
bs_obj.select('#mainMenuBox')

# bs_obj.select('#mainMenuBox ul')
# ID가 mainMenuBox인 요소의 "후손" 중에서 "모든 <ul> 태그"를 찾습니다.
bs_obj.select('#mainMenuBox ul')

# bs_obj.select('#mainMenuBox > ul')
# ID가 mainMenuBox인 요소의 "직계 자식" 중에서 "모든 <ul> 태그"를 찾습니다. (>는 자식 선택자)
bs_obj.select('#mainMenuBox > ul')

# print(bs_obj.select('#mainMenuBox li'))
# ID가 mainMenuBox인 요소의 후손 중에서 "모든 <li> 태그"를 찾아 출력합니다. (4개 항목)
print(bs_obj.select('#mainMenuBox li'))

# bs_obj.select('#mainMenuBox > li')
# ID가 mainMenuBox인 요소의 "직계 자식" 중에서 'li' 태그를 찾습니다.
# mainMenuBox의 직계 자식은 <ul>이므로 <li>는 찾지 못하여 "빈 리스트"가 반환됩니다.
bs_obj.select('#mainMenuBox > li')

# bs_obj.select("#wrap > div")
# ID가 wrap인 요소의 "직계 자식" 중에서 "모든 <div> 태그"를 찾습니다. (총 3개의 <div>)
bs_obj.select("#wrap > div")

# len(bs_obj.select("#wrap > div"))
# 직계 자식인 <div> 요소의 개수를 출력합니다. (3)
len(bs_obj.select("#wrap > div"))

# bs_obj.select("#wrap  div")
# ID가 wrap인 요소의 "모든 후손" 중에서 "모든 <div> 태그"를 찾습니다. (공백은 후손 선택자)
bs_obj.select("#wrap  div")

# len(bs_obj.select("#wrap  div"))
# 모든 후손 <div> 요소의 개수를 출력합니다. (총 4개: mainMenuBox, unnamed div, out_box, 2개의 box 클래스 -> 5개)
len(bs_obj.select("#wrap  div"))




# 4. "클래스 선택자 및 데이터 추출" (Class Selector and Data Extraction)

# bs_obj.select('.box')
# "클래스 이름이 'box'인 모든 요소"를 찾아 리스트로 반환합니다. (.은 클래스 선택자) (공지사항, 커뮤니티 2개)
bs_obj.select('.box')

# len(bs_obj.select('.box'))
# 클래스가 'box'인 요소의 개수를 출력합니다. (2)
len(bs_obj.select('.box'))

# bs_obj.select('.box')[1].select('a')
# 1단계: 모든 '.box' 클래스를 찾아 리스트로 얻습니다.
# 2단계: 그 리스트의 "두 번째 요소" (인덱스 1, 커뮤니티 박스)를 선택합니다.
# 3단계: 선택된 요소 내부에서 "모든 <a> 태그"를 찾습니다. (커뮤니티 내 3개의 링크)
bs_obj.select('.box')[1].select('a')

# bs_obj.select('.box')[1].select('a')[0]
# 커뮤니티 박스 내부에서 찾은 <a> 태그 리스트의 "첫 번째 요소"를 선택합니다. (<a href="#">[레시피] : 살 안찌는 야식 만들기</a>)
bs_obj.select('.box')[1].select('a')[0]

# bs_obj.select('.box')[0].select('a')[0].text
# 1단계: 첫 번째 '.box' (공지사항)를 선택합니다.
# 2단계: 그 내부의 첫 번째 'a' 태그를 선택합니다.
# 3단계: ".text" 속성을 사용하여 그 태그의 "순수한 텍스트"를 추출합니다. ('[배송] : 무표배송 변경 안내 18.10.20')
bs_obj.select('.box')[0].select('a')[0].text

# bs_obj.select('.box')[0].select('a')[0]['href']
# 1단계: 첫 번째 '.box' (공지사항) 내부의 첫 번째 'a' 태그를 선택합니다.
# 2단계: "딕셔너리 접근" 방식(['href'])을 사용하여 'href' "속성 값"('#')을 추출합니다.
bs_obj.select('.box')[0].select('a')[0]['href']


# "핵심 요약"
# select() 메서드는 CSS 선택자의 강력한 문법(ID: #, Class: ., Descendant: Space, Child: >)을 사용하여 
# find()/findAll() 보다 훨씬 명확하고 간결하게 HTML 요소를 검색할 수 있게 해줍니다. 
# 이 예시는 특정 박스(box 클래스) 내부의 링크만 추출하는 등 **"정밀한 영역 지정"**에 select()가 얼마나 유용한지를 보여줍니다.


