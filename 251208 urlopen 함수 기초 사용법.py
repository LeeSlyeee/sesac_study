import urllib.request as req
from urllib.error import URLError, HTTPError


path_list = ["c:\\MyExam\\test2.jpg", "c:\\MyExam\\index2.html"]

target_url = ["https://i.pinimg.com/736x/13/77/b6/1377b6c567a937484e1ce227337ba8bd.jpg", "https://www.google.com/"]

for i, url in enumerate(target_url):
    # 예외 처리
    try:
        # 웹 수신 정보 읽기
        response = req.urlopen(url)
        
        # 수신 내용
        contents = response.read()
        print('---------------------------------------------------')
        # 상태 정보 중간 출력
        print('Header Info-{} : {}'.format(i, response.info()))
        print('HTTP Status Code : {}'.format(response.getcode()))
        print()
        print('---------------------------------------------------')
        # 파일 쓰기
        with open(path_list[i], 'wb') as c:
            c.write(contents)
        # HTTP 에러 발생 시
    except HTTPError as e:
        print("Download failed.")
        print('HTTPError Code : ', e.code)
        # URL 에러 발생 시
    except URLError as e:
        print("Download failed.")
        print('URL Error Reason : ', e.reason)
        # 성공
    else:
        print()
        print("Download Succeed.")