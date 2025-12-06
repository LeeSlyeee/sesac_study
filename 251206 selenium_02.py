from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import threading
import pandas as pd






# 기사 제목들을 저장할 전역 리스트를 초기화합니다.
article_list = []


# 특정 페이지의 기사 제목을 크롤링하는 함수를 정의합니다.
def get_article(page):
    # 각 호출마다 새로운 Chrome WebDriver 인스턴스를 생성합니다.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 네이버 뉴스 '섹션' 페이지로 이동합니다. (예: 100=정치, 101=경제 등)
    # page 변수를 10 뒤에 붙여 URL을 완성합니다. (예: page=0이면 100, page=1이면 101)
    driver.get("https://news.naver.com/section/10" + str(page))
    
    # CSS 선택자 '#newsct li'를 사용하여 뉴스 리스트 내의 각 기사 항목들을 모두 찾습니다.
    articles = driver.find_elements(By.CSS_SELECTOR,'#newsct li')
    
    # 찾은 각 기사 항목(article)을 순회하며 제목을 추출합니다.
    for article in articles:
        try:
            # 1. 일반적인 기사 제목을 포함하는 요소를 찾습니다.
            tmp_elements = article.find_elements(By.CSS_SELECTOR, '.sa_text strong')
            
            # 만약 요소가 존재하면 (일반 기사 레이아웃)
            if tmp_elements:
                # 첫 번째 요소의 텍스트를 제목으로 저장합니다.
                title = tmp_elements[0].text
            # 요소가 존재하지 않으면 (다른 레이아웃, 예: 포토/영상 기사)
            else:
                # 2. 다른 레이아웃의 기사 제목을 포함하는 요소를 찾습니다.
                tmp_elements2 = article.find_elements(By.CSS_SELECTOR, '.ss_text a')
                
                # 만약 이 요소가 존재하면
                if tmp_elements2:
                    # 첫 번째 요소의 텍스트를 제목으로 저장합니다.
                    title = tmp_elements2[0].text
                # 두 가지 모두 찾지 못했다면
                else:
                    title = "해당 정보 없음"
            
            # 추출한 제목을 전역 리스트 article_list에 추가합니다.
            article_list.append(title)
        except:
            # 요소 찾기 또는 텍스트 추출 중 오류가 발생하면 출력합니다.
            print("에러 발생!")
            
    # 해당 페이지의 크롤링이 완료되었음을 알립니다.
    print("end :", page)
    # WebDriver를 종료하여 브라우저 창을 닫습니다.
    driver.quit()
    
    
# for 루프를 사용하여 get_article 함수를 순차적으로 5번 호출합니다. (page=0부터 4까지)
# 참고: 이 호출은 순차적(Sequential)으로 실행되며, 멀티스레딩은 사용되지 않았습니다.
for page in range(0, 5):
    get_article(page)
    
    
    
    
# "category"와 "title" 컬럼을 가진 빈 Pandas DataFrame을 생성합니다.
df = pd.DataFrame(columns=["category","title"])


# 기사 제목과 카테고리를 크롤링하여 DataFrame에 저장하는 함수를 재정의합니다.
# 참고: 위에서 정의된 get_article 함수를 덮어씁니다.
def get_article(page):
    # 새로운 Chrome WebDriver 인스턴스를 생성합니다.
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    
    # 네이버 뉴스 섹션 페이지로 이동합니다. (예: 100=정치, 101=경제 등)
    driver.get(
        "https://news.naver.com/section/10" + str(page))
        
    # CSS 선택자 '.ct_snb_h2_a'를 사용하여 현재 페이지의 카테고리 이름(예: "정치", "경제")을 가져옵니다.
    # .get_attribute("innerText")를 사용하여 텍스트 내용을 추출합니다.
    category = driver.find_element(By.CSS_SELECTOR, '.ct_snb_h2_a').get_attribute("innerText")
    
    # CSS 선택자 '#newsct li'를 사용하여 뉴스 리스트 내의 각 기사 항목들을 모두 찾습니다.
    articles = driver.find_elements(By.CSS_SELECTOR,'#newsct li')
    
    # 찾은 각 기사 항목(article)을 순회하며 제목을 추출하고 DataFrame에 저장합니다.
    for article in articles:
        try:
            # 제목 추출 로직은 첫 번째 섹션과 동일합니다.
            tmp_elements = article.find_elements(By.CSS_SELECTOR, '.sa_text strong')
            if tmp_elements:
                title = tmp_elements[0].text
            else:
                tmp_elements2 = article.find_elements(By.CSS_SELECTOR, '.ss_text a')
                if tmp_elements2:
                    title = tmp_elements2[0].text
                else:
                    title = "해당 정보 없음"
        except:
            print("에러 발생!")
            
        
        # 추출한 카테고리와 제목 정보를 DataFrame의 새로운 행으로 추가합니다.
        # df.loc[len(df)]을 사용하여 현재 DataFrame의 마지막 행 다음에 데이터를 추가합니다.
        df.loc[len(df)] = {
            "category": category,
            "title": title,
        }
        
    # 해당 페이지의 크롤링이 완료되었음을 알립니다. (여기서는 page+1로 출력하여 페이지 번호를 1부터 시작하는 것처럼 보입니다.)
    print("end :", page+1)
    # WebDriver를 종료하여 브라우저 창을 닫습니다.
    driver.quit()
    
    
# for 루프를 사용하여 get_article 함수를 순차적으로 6번 호출합니다. (page=0부터 5까지)
# 참고: 이 호출 역시 순차적(Sequential)으로 실행됩니다.
for page in range(0, 6):
    get_article(page)
    
# 최종적으로 크롤링된 데이터가 담긴 DataFrame 전체를 출력합니다.
print(df)
    
# 크롤링된 데이터에서 'category' 컬럼의 값별 개수를 세어 출력합니다.
# 이를 통해 각 카테고리별로 몇 개의 기사가 수집되었는지 확인할 수 있습니다.
print(df['category'].value_counts())


df.to_excel('test.xlsx')