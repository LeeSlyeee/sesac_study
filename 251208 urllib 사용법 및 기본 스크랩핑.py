# urllib.request 모듈을 가져와 'req'라는 별칭으로 사용합니다.
import urllib.request as req
# urllib.error 모듈에서 URLError와 HTTPError 클래스를 가져옵니다.
# 이는 웹 요청 중 발생할 수 있는 다양한 종류의 오류를 처리하는 데 사용됩니다.
from urllib.error import URLError, HTTPError


# 다운로드한 파일을 저장할 로컬 경로 리스트입니다.
path_list = ["c:\\MyExam\\test2.jpg", "c:\\MyExam\\index2.html"]

# 다운로드할 웹 리소스의 URL 리스트입니다.
target_url = ["https://i.pinimg.com/736x/13/77/b6/1377b6c567a937484e1ce227337ba8bd.jpg", "https://www.google.com/"]

# target_url 리스트를 순회하며 각 URL(url)과 인덱스(i)에 대해 반복합니다.
for i, url in enumerate(target_url):
    # 예외 처리(try...except...else) 블록을 시작하여 네트워크 오류를 대비합니다.
    try:
        # req.urlopen() 함수를 사용하여 URL에 연결하고 응답 객체(response)를 얻습니다.
        # 이 객체를 통해 서버 응답 정보를 읽을 수 있습니다.
        response = req.urlopen(url)
        
        # response.read() 메서드를 사용하여 응답 본문(컨텐츠) 전체를 읽어와 contents 변수에 저장합니다.
        # 이미지나 HTML 페이지의 실제 데이터가 여기에 담깁니다.
        contents = response.read()
        print('---------------------------------------------------')
        # 상태 정보 중간 출력: 서버 응답의 헤더 정보를 출력합니다 (Content-Type, Date 등).
        print('Header Info-{} : {}'.format(i, response.info()))
        # HTTP Status Code (예: 200 OK, 404 Not Found 등)를 출력합니다.
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('---------------------------------------------------')
        
        # 파일 쓰기: 'with open(...) as c:' 구문을 사용하여 파일을 엽니다.
        # 'wb' 모드는 이진(Binary) 쓰기 모드로, 이미지나 인코딩된 HTML 등을 저장할 때 적합합니다.
        with open(path_list[i], 'wb') as c:
            # contents 변수에 저장된 데이터를 파일에 씁니다.
            c.write(contents)
            
        # HTTP 에러(예: 404, 500 등 서버 관련 에러) 발생 시 이 블록이 실행됩니다.
    except HTTPError as e:
        print("Download failed.")
        # 발생한 HTTP 에러의 상태 코드를 출력합니다.
        print('HTTPError Code : ', e.code)
        
        # URL 에러(예: 잘못된 URL 형식, 네트워크 연결 실패 등) 발생 시 이 블록이 실행됩니다.
    except URLError as e:
        print("Download failed.")
        # 발생한 URL 에러의 이유(원인)를 출력합니다.
        print('URL Error Reason : ', e.reason)
        
        # try 블록이 예외 없이 성공적으로 완료되었을 때만 이 블록이 실행됩니다.
    else:
        print()
        print("Download Succeed.")