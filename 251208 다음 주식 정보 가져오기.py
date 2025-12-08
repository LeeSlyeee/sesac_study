import json # JSON 데이터를 처리하기 위한 모듈을 가져옵니다.
import urllib.request as req # URL을 열고 요청을 보내기 위한 모듈을 가져옵니다.
from fake_useragent import UserAgent # 웹 요청 시 User-Agent 문자열을 무작위로 생성하여 봇 탐지를 우회하는 데 사용되는 모듈을 가져옵니다.



# UserAgent 객체를 생성합니다.
ua = UserAgent()



# HTTP 요청 헤더를 정의하는 딕셔너리입니다.
headers = {
    # 'User-Agent'는 요청을 보내는 클라이언트(브라우저) 정보를 서버에 알립니다.
    # ua.chrome은 무작위 Chrome 브라우저 User-Agent 문자열을 생성합니다.
    'User-Agent': ua.chrome,
    # 'referer'는 요청이 시작된 이전 페이지 주소를 서버에 알립니다.
    # 다음 금융 페이지에서 요청이 온 것처럼 위장하여 접근을 허용받기 위해 사용됩니다.
    'referer': 'https://finance.daum.net/'
}




# 다음 금융에서 실시간 인기 검색 순위 10개를 가져오는 API 엔드포인트 URL입니다.
url = "https://finance.daum.net/api/search/ranks?limit=10"




# 1. req.Request(url, headers=headers)로 요청 객체를 생성합니다. (URL과 정의된 헤더를 포함)
# 2. req.urlopen(...)로 요청을 보내고 응답 객체를 받습니다.
# 3. .read()로 응답 본문 전체(바이트 형태)를 읽어옵니다.
# 4. .decode('utf-8')로 바이트를 UTF-8 문자열로 디코딩합니다.
res = req.urlopen(req.Request(url, headers=headers)).read().decode('utf-8')

# 5. json.loads(res)를 사용하여 JSON 문자열(res)을 Python 딕셔너리/리스트로 변환합니다.
# 6. 결과 딕셔너리에서 실제 순위 데이터가 담긴 'data' 키의 값을 추출합니다.
rank_json = json.loads(res)['data']



# 추출된 순위 데이터 리스트를 중간 확인용으로 출력합니다.
print(f'중간 확인 : {rank_json} \n')



# 순위 데이터(리스트)를 순회하며 각 항목(elm, 딕셔너리)에 접근합니다.
for elm in rank_json:
    # print(type(elm)) # elm의 타입이 딕셔너리(dict)임을 확인하는 주석 처리된 코드입니다.
    # 각 종목의 순위, 현재 거래 금액, 회사명을 딕셔너리 키를 이용해 추출하여 출력합니다.
    print(f"순위 : {elm['rank']}, 금액 : {elm['tradePrice']}, 회사명 : {elm['name']}")