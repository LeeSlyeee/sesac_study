import webbrowser
import os
import requests
import bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen # 사이트에 요청 신호를 보내는 함수
from urllib.parse import urljoin # URL을 조합하는 데 유용한 함수




BASE_URL = 'http://daekwangdoor.com/'

target_url = BASE_URL
target = requests.get(target_url)
target.encoding = 'UTF-8'
html_target = target.text


target_image = BeautifulSoup(html_target, "lxml")
target_image_elements = target_image.select('img')

target_image_elements





def get_image_url(url):
    html_image_url = requests.get(url).text
    soup_image_url = BeautifulSoup(html_image_url, "lxml")
    image_elements = soup_image_url.select('img')

    if(image_elements): # 리스트가 비어있지 않은지 확인
        image_urls = []

        for image_element in image_elements:
            # 'src' 속성을 가져옴
            relative_url = image_element.get('src')

            if relative_url:
                # 'urljoin'을 사용하여 상대 경로를 절대 경로로 변환합니다.
                # BASE_URL과 relative_url을 안전하게 조합하여 완전한 URL을 만듭니다.
                full_url = urljoin(BASE_URL, relative_url)
                image_urls.append(full_url)

        return image_urls

    else:
        return None
    
    
    
    
    
def download_image(img_folder, img_url):
    # 폴더가 없으면 생성
    if not os.path.exists(img_folder):
        os.makedirs(img_folder)

    if(img_url):
        try:
            # 스트림을 활성화하여 큰 파일 다운로드에 효율적으로 만듭니다.
            html_image = requests.get(img_url, stream=True)
            html_image.raise_for_status() # HTTP 오류가 발생하면 예외를 발생시킵니다.

            # 파일명을 URL의 기본 이름으로 사용
            image_filename = os.path.basename(img_url)

            # URL의 마지막 부분이 너무 일반적이거나 '/'로 끝나는 경우 (예: base_url 자체가 이미지 url로 잘못 추출된 경우)를 대비해 필터링
            if not image_filename or '.' not in image_filename:
                print(f"경고: 유효하지 않은 파일명 '{image_filename}'으로 인해 다운로드 건너뜀.")
                return

            imageFile = open(os.path.join(img_folder, image_filename), 'wb')

            chunk_size = 1024 * 10 # 10KB 청크 (메모리 효율성을 위해 작은 단위로 변경)

            for chunk in html_image.iter_content(chunk_size):
                if chunk: # chunk가 유효한 데이터인지 확인
                    imageFile.write(chunk)

            imageFile.close()

            print(f"이미지 파일명: '{image_filename}'. 내려받기 완료!")

        except requests.exceptions.RequestException as e:
            print(f"오류: {img_url} 다운로드 실패: {e}")
        except Exception as e:
            print(f"파일 쓰기 오류: {e}")
            
            
daekwang_url = BASE_URL # 이미 위에서 정의된 BASE_URL 사용
figure_folder = "C:/Myexam/download" # **주의: 이 경로는 실행 환경에 따라 접근 권한이 필요할 수 있습니다.**







print("--- 이미지 URL 추출 시작 ---")
image_urls = get_image_url(daekwang_url)

if image_urls:
    num_of_download_image = len(image_urls)
    print(f"총 {num_of_download_image}개의 이미지 URL 추출 완료.")

    # 추출된 전체 URL 목록 출력 (확인용)
    # print(image_urls)

    print("\n--- 이미지 다운로드 시작 ---")
    for k in range(num_of_download_image):
        download_image(figure_folder, image_urls[k])

    print("================================")
    print("선택한 모든 이미지 내려받기 완료!")

else:
    print("================================")
    print("추출된 이미지 URL이 없습니다.")