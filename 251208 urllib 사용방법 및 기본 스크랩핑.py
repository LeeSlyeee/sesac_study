# urllib.request 모듈을 가져오고, 'req'라는 별칭으로 사용합니다.
# 이 모듈은 URL을 열고 읽는 함수와 클래스를 제공합니다.
import urllib.request as req


# 다운로드할 이미지 파일의 URL을 변수에 저장합니다.
img_url = "https://sesac.seoul.kr/static/common/images/www/common/img_ssac_intro.png"
# 다운로드할 HTML 페이지의 URL을 변수에 저장합니다.
html_url = "http://google.com"


# 다운로드한 파일을 저장할 로컬 경로와 파일 이름을 변수에 저장합니다.
save_path1 = "C:/Myexam/test1.jpg"
# 다운로드한 HTML을 저장할 로컬 경로와 파일 이름을 변수에 저장합니다.
save_path2 = "C:/Myexam/index.html"


# 다운로드 과정 중 발생할 수 있는 오류를 처리하기 위해 try-except 블록을 사용합니다.
try:
    # req.urlretrieve() 함수를 사용하여 이미지 URL에서 파일을 다운로드하고 지정된 경로에 저장합니다.
    # 함수는 저장된 파일 경로(file1)와 응답 헤더 정보(header1)를 반환합니다.
    file1, header1 = req.urlretrieve(img_url, save_path1)
    
    # req.urlretrieve() 함수를 사용하여 HTML URL에서 파일을 다운로드하고 지정된 경로에 저장합니다.
    # 함수는 저장된 파일 경로(file2)와 응답 헤더 정보(header2)를 반환합니다.
    file2, header2 = req.urlretrieve(html_url, save_path2)
    
# 다운로드 중 예외(오류)가 발생하면 이 블록이 실행됩니다.
except Exception as e:
    # 다운로드 실패 메시지를 출력합니다.
    print("Download failed.")
    # 발생한 예외(오류) 내용을 출력합니다.
    print(e)
    
# 예외 없이 try 블록이 성공적으로 완료되면 이 블록이 실행됩니다.
else:
    # 다운로드된 이미지 파일의 응답 헤더 정보를 출력합니다.
    print(header1)
    # 다운로드된 HTML 파일의 응답 헤더 정보를 출력합니다.
    print(header2)
    
    
# 다운로드가 성공했는지 여부와 관계없이(try/except/else 블록 이후) 실행됩니다.
# 저장된 파일 경로(file1)를 출력합니다.
print(f"Filename1 {file1}")
# 저장된 파일 경로(file2)를 출력합니다.
print(f"Filename2 {file2}")

# 다운로드 성공 메시지를 출력합니다. (실제 다운로드 성공 여부는 try/except 블록에서 확인)
print("Download Succeed.")