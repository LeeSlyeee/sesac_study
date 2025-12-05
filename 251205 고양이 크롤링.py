# 'requests' 모듈: HTTP 요청을 보내 웹 서버의 데이터를 가져오는 데 사용됩니다.
import requests
# 'os' 모듈: 운영체제(파일 시스템) 관련 기능을 사용합니다. (폴더 생성, 경로 처리 등)
import os


# 웹 이미지 다운로드 전체 코드

# 다운로드할 이미지 파일의 전체 URL을 'url' 변수에 저장합니다.
url = 'https://i.pinimg.com/736x/d8/a6/cb/d8a6cbb02bc2c5c27ae238db2e89425d.jpg'

# "requests.get(url)" 함수를 사용하여 해당 URL로 HTTP GET 요청을 보냅니다.
# 이미지 파일의 "바이너리 데이터"를 포함하는 Response 객체를 'html_image'에 저장합니다.
html_image = requests.get(url)

# "os.path.basename(url)" 함수를 사용하여 URL 경로에서 "순수한 파일 이름"만을 추출하여 'image_file_name'에 저장합니다.
image_file_name = os.path.basename(url)




# 2. "저장 폴더 확인 및 경로 구성" (Folder Check and Path Construction)

# 이미지를 저장할 로컬 목표 폴더 경로를 'folder' 변수에 정의합니다.
folder = 'C:/Myexam/download'

# 'os.path.exists(folder)' 함수를 사용하여 해당 폴더가 존재하는지 확인합니다.
if not os.path.exists(folder):
    # 폴더가 존재하지 않는다면:
    
    # "os.makedirs(folder)" 함수를 사용하여 해당 폴더를 "생성"합니다.
    # 이 함수는 중간 경로도 함께 생성해줍니다. (파일 저장 전 필수 작업)
    os.makedirs(folder)
    
# "os.path.join(folder, image_file_name)" 함수를 사용하여 폴더 경로와 파일 이름을 결합합니다.
# 이로써 파일이 저장될 "최종 경로"('C:/Myexam/download/d8a6cbb02bc2c5c27ae238db2e89425d.jpg')가 'image_path'에 구성됩니다.
image_path = os.path.join(folder, image_file_name)

# 구성된 최종 파일 저장 경로를 출력하여 확인합니다.
print(image_path)



# 3. "스트리밍 파일 저장" (Streaming File Save)

# 'image_path'에 지정된 경로로 파일을 "쓰기 바이너리 모드('wb')"로 엽니다.
# 'wb' 모드는 이미지와 같은 "바이너리 데이터"를 디스크에 기록하는 데 필수적입니다.
imageFile = open(image_path, 'wb')

# 파일 저장 시 사용할 데이터 조각(청크)의 크기를 바이트 단위로 정의합니다. (1,000,000 바이트 = 1MB)
chunk_size = 1000000

# "html_image.iter_content(chunk_size)" 메서드를 사용하여 Response 객체의 이미지 데이터를 
# "chunk_size" 단위로 나누어 "반복적"으로 읽어옵니다.
# 이는 "큰 파일" 다운로드 시 메모리 부하를 줄이는 데 사용됩니다.
for chunk in html_image.iter_content(chunk_size):
    # 반복문에서 얻은 데이터 조각('chunk')을 'imageFile' 객체를 통해 디스크에 "쓰기"를 수행합니다.
    imageFile.write(chunk)
    
# 모든 데이터 청크가 파일에 기록된 후, 'imageFile.close()'를 호출하여 파일을 "닫고" 시스템 자원을 해제합니다.
# 이 단계는 데이터의 손실을 방지하고 파일 저장을 완료하는 데 중요합니다.
imageFile.close()