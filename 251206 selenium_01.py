# webdriver: Selenium의 핵심 클래스로, 브라우저를 제어하는 데 사용됩니다.
from selenium import webdriver
# ChromeService: Chrome 드라이버를 서비스로 설정하는 데 사용됩니다.
from selenium.webdriver.chrome.service import Service as ChromeService
# ChromeDriverManager: Chrome 드라이버를 자동으로 다운로드 및 설치하여 관리해 줍니다.
from webdriver_manager.chrome import ChromeDriverManager
# By: 요소를 찾을 때 사용되는 기준(ID, CSS_SELECTOR, XPATH 등)을 제공합니다.
from selenium.webdriver.common.by import By


# 1. WebDriver 초기화 및 설정
# Chrome 브라우저의 WebDriver 인스턴스를 생성합니다.
# ChromeService(ChromeDriverManager().install()):
#   - ChromeDriverManager().install()로 최신 Chrome 드라이버를 자동으로 설치/가져오고,
#   - 이를 ChromeService를 통해 WebDriver에 서비스로 연결하여 사용합니다.
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# 2. 웹페이지 접속
# 지정된 URL(네이버 메인 페이지)로 이동합니다.
driver.get("https://www.naver.com/")

# 3. 브라우저 창 크기 설정
# 브라우저 창 크기를 가로 1024 픽셀, 세로 768 픽셀로 설정합니다.
driver.set_window_size(1024, 768)

# 4. JavaScript 실행 (스크롤 이동)
# JavaScript 코드를 실행하여 현재 창을 가로 200, 세로 300 픽셀 위치로 스크롤합니다.
driver.execute_script("window.scrollTo(200, 300);")

# 5. JavaScript 실행 (경고창 띄우기)
# JavaScript 코드를 실행하여 "selenium test" 메시지를 가진 경고(alert) 팝업창을 띄웁니다.
driver.execute_script("alert('selenium test');")

# 6. 경고창(Alert) 처리
try:
    # driver.switch_to.alert: 브라우저의 제어권을 경고창(Alert)으로 전환합니다.
    alert = driver.switch_to.alert
    # alert.text: 경고창에 표시된 텍스트를 출력합니다.
    print(alert.text)
except:
    # 경고창이 존재하지 않을 경우(예외 발생 시) 이 메시지를 출력합니다.
    print('alert 없음')

# 경고창 닫기 (확인 버튼 클릭)
# 경고창(Alert) 객체에서 .accept() 메서드를 호출하여 "확인" 버튼을 눌러 경고창을 닫습니다.
# 참고: 이 코드가 실행되기 위해서는 경고창이 이전에 성공적으로 잡혀서 'alert' 변수에 할당되어 있어야 합니다.
alert.accept()


# 7. 요소 찾기 및 클릭
# driver.find_element(): 웹페이지에서 요소를 찾습니다.
# By.CSS_SELECTOR: CSS 선택자(Selector)를 사용하여 요소를 찾습니다.
# ".MyView-module__link_login___HpHMW": 네이버 로그인 링크(또는 유사한 요소)의 CSS 클래스 이름입니다.
# .click(): 찾은 요소를 클릭합니다 (로그인 페이지로 이동 시도).
driver.find_element(By.CSS_SELECTOR,".MyView-module__link_login___HpHMW").click()


# 8. WebDriver 종료
# 브라우저를 닫고 WebDriver 세션을 종료합니다. (스크립트 실행 완료)
driver.quit()