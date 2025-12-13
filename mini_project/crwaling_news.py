import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False


nowon_crime_url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EB%85%B8%EC%9B%90%EA%B5%AC+%EB%B2%94%EC%A3%84"



nowon_crime_date = []
nowon_crime_title = []

def get_nowon_crime():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(nowon_crime_url)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        import time
        time.sleep(1) 
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        
        if new_height == last_height:
            print(">>> 페이지 맨 끝에 도달했습니다. 스크롤링 종료.")
            break
        
        last_height = new_height
        
    
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.group_news .sds-comps-vertical-layout'))
        )
    except Exception as e:
        print(f"최종 데이터 로드 대기 중 에러 발생: {e}")
        driver.quit()
        return

    crime_data_container = driver.find_elements(By.CSS_SELECTOR, '.group_news .sds-comps-vertical-layout')
    
    for row in crime_data_container:         
        crime_date = row.find_elements(By.CSS_SELECTOR, '.sds-comps-profile-source .sds-comps-profile-info-subtext')
        if crime_date:
            nowon_crime_date.append(crime_date[0].text.strip())
        else:
            nowon_crime_date.append("해당 정보 없음")
        
    
        crime_title = row.find_elements(By.CSS_SELECTOR, '.sds-comps-base-layout a .sds-comps-text-type-headline1')
        if crime_title:
            nowon_crime_title.append(crime_title[0].text.strip())
        else:
            nowon_crime_title.append("해당 정보 없음")
    
    
    
    
    driver.quit()
    

get_nowon_crime()



nowon_crime_news = {
    "기사날짜" : nowon_crime_date,
    "기사제목" : nowon_crime_title
}


dobong_crime_df = pd.DataFrame(nowon_crime_news)

file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "노원구 범죄 뉴스.csv")

dobong_crime_df.to_csv(load_file, encoding='utf-8-sig')





# 1. CSV 데이터를 데이터프레임으로 가져오기
# 첫 번째 열이 인덱스로 사용되고 있으므로, index_col=0을 사용합니다.
df = pd.DataFrame(pd.read_csv(load_file), index_col=0)

# 데이터프레임 확인 (선택 사항)
# print("--- 원본 데이터프레임 ---")
# print(df)

# 2. '기사날짜'와 '기사제목'이 둘 다 "해당 정보 없음"인 경우를 제외하기
# 논리적으로 NOT 연산자 (~) 와 AND 연산자 (&)를 사용합니다.
# (df['기사날짜'] == "해당 정보 없음") & (df['기사제목'] == "해당 정보 없음") 이 True인 행을 제외합니다.
df_filtered = df[~((df['기사날짜'] == "해당 정보 없음") & (df['기사제목'] == "해당 정보 없음"))]

# 필터링된 데이터프레임 확인 (선택 사항)
# print("\n--- 필터링된 데이터프레임 ---")
# print(df_filtered)

# 3. 새로운 CSV 파일로 저장하기
output_file_name = __file__.replace(file_list[-1], "노원구 범죄 뉴스_filterd.csv")
df_filtered.to_csv(output_file_name, encoding='utf-8-sig') # 한글 깨짐 방지를 위해 'utf-8-sig' 사용

print(f"\n✅ 처리가 완료되었습니다.")
print(f"   '기사날짜'와 '기사제목'이 모두 '해당 정보 없음'인 행이 제거된 데이터가")
print(f"   **'{output_file_name}'** 파일로 저장되었습니다.")