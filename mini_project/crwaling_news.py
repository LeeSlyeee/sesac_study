import os
import re
from datetime import timedelta
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
gangdong_crime_url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EA%B0%95%EB%8F%99%EA%B5%AC+%EB%B2%94%EC%A3%84"
sungbuk_crime_url = "https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query=%EC%84%B1%EB%B6%81%EA%B5%AC+%EB%B2%94%EC%A3%84"



nowon_crime_date = []
nowon_crime_title = []

def get_nowon_crime():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(nowon_crime_url)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        import time
        time.sleep(0.3) 
        
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


nowon_crime_df = pd.DataFrame(nowon_crime_news)

file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스.csv")

nowon_crime_df.to_csv(load_file, encoding='utf-8-sig')





df = pd.DataFrame(pd.read_csv(load_file))

condition_date = df['기사날짜'] != '해당 정보 없음'

condition_title = df['기사제목'] != '해당 정보 없음'

df_filtered = df[condition_date & condition_title]

df_filtered = df_filtered.reset_index(drop=True)


output_file_name = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_filterd.csv")
df_filtered.to_csv(output_file_name, encoding='utf-8-sig') # 한글 깨짐 방지를 위해 'utf-8-sig' 사용


print(f"\n✅ 처리가 완료되었습니다.")
print(f"   '기사날짜'와 '기사제목'이 모두 '해당 정보 없음'인 행이 제거된 데이터가")
print(f"   **'{output_file_name}'** 파일로 저장되었습니다.")




file_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_filterd.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df.drop_duplicates(subset=['기사제목'], keep='first')

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} duplicate rows.")

    output_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_result.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")





file_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_result.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df[df['기사제목'].str.contains("범죄|성폭행|성범죄|폭행|구타|살인|절도|강도", na=False) & df['기사제목'].str.contains("노원구", na=False)]

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows that did not satisfy the condition.")

    output_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_final.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")







file_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_final.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    current_date = pd.Timestamp("2025-12-14")

    def parse_date(date_str):
        try:
            date_str = str(date_str).strip()
            if re.match(r'^\d{4}\.\d{2}\.\d{2}\.?$', date_str):
                return pd.to_datetime(date_str.rstrip('.'), format='%Y.%m.%d')
            
            if '시간 전' in date_str or '분 전' in date_str:
                return current_date
            if '일 전' in date_str:
                days = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=days)
            if '주 전' in date_str:
                weeks = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(weeks=weeks)
            if '달 전' in date_str or '개월 전' in date_str: # Rough estimate
                months = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=months*30)
            
            return pd.NaT
        except:
            return pd.NaT

    df['parsed_date'] = df['기사날짜'].apply(parse_date)

    df_filtered = df.dropna(subset=['parsed_date'])
    df_filtered = df_filtered[
        (df_filtered['parsed_date'].dt.year >= 2022) & 
        (df_filtered['parsed_date'].dt.year <= 2025)
    ]

    df_filtered = df_filtered.sort_values(by='parsed_date', ascending=False)

    print(f"Filtered row count (2022-2025): {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows.")

    df_filtered = df_filtered.drop(columns=['parsed_date'])

    output_path = __file__.replace(file_list[-1], "\노원구\노원구 범죄 뉴스_final_sorted.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")





#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







sungbuk_crime_date = []
sungbuk_crime_title = []

def get_sungbuk_crime():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(sungbuk_crime_url)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        import time
        time.sleep(0.3) 
        
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
            sungbuk_crime_date.append(crime_date[0].text.strip())
        else:
            sungbuk_crime_date.append("해당 정보 없음")
        
    
        crime_title = row.find_elements(By.CSS_SELECTOR, '.sds-comps-base-layout a .sds-comps-text-type-headline1')
        if crime_title:
            sungbuk_crime_title.append(crime_title[0].text.strip())
        else:
            sungbuk_crime_title.append("해당 정보 없음")
    
    
    
    
    driver.quit()
    

get_sungbuk_crime()



sungbuk_crime_news = {
    "기사날짜" : sungbuk_crime_date,
    "기사제목" : sungbuk_crime_title
}


sungbuk_crime_df = pd.DataFrame(sungbuk_crime_news)

file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스.csv")

sungbuk_crime_df.to_csv(load_file, encoding='utf-8-sig')





df = pd.DataFrame(pd.read_csv(load_file))

condition_date = df['기사날짜'] != '해당 정보 없음'

condition_title = df['기사제목'] != '해당 정보 없음'

df_filtered = df[condition_date & condition_title]

df_filtered = df_filtered.reset_index(drop=True)


output_file_name = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_filterd.csv")
df_filtered.to_csv(output_file_name, encoding='utf-8-sig') # 한글 깨짐 방지를 위해 'utf-8-sig' 사용


print(f"\n✅ 처리가 완료되었습니다.")
print(f"   '기사날짜'와 '기사제목'이 모두 '해당 정보 없음'인 행이 제거된 데이터가")
print(f"   **'{output_file_name}'** 파일로 저장되었습니다.")




file_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_filterd.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df.drop_duplicates(subset=['기사제목'], keep='first')

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} duplicate rows.")

    output_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_result.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")





file_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_result.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df[df['기사제목'].str.contains("범죄|성폭행|성범죄|폭행|구타|살인|절도|강도", na=False) & df['기사제목'].str.contains("성북구", na=False)]

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows that did not satisfy the condition.")

    output_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_final.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")







file_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_final.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    current_date = pd.Timestamp("2025-12-14")

    def parse_date(date_str):
        try:
            date_str = str(date_str).strip()
            if re.match(r'^\d{4}\.\d{2}\.\d{2}\.?$', date_str):
                return pd.to_datetime(date_str.rstrip('.'), format='%Y.%m.%d')
            
            if '시간 전' in date_str or '분 전' in date_str:
                return current_date
            if '일 전' in date_str:
                days = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=days)
            if '주 전' in date_str:
                weeks = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(weeks=weeks)
            if '달 전' in date_str or '개월 전' in date_str: # Rough estimate
                months = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=months*30)
            
            return pd.NaT
        except:
            return pd.NaT

    df['parsed_date'] = df['기사날짜'].apply(parse_date)

    df_filtered = df.dropna(subset=['parsed_date'])
    df_filtered = df_filtered[
        (df_filtered['parsed_date'].dt.year >= 2022) & 
        (df_filtered['parsed_date'].dt.year <= 2025)
    ]

    df_filtered = df_filtered.sort_values(by='parsed_date', ascending=False)

    print(f"Filtered row count (2022-2025): {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows.")

    df_filtered = df_filtered.drop(columns=['parsed_date'])

    output_path = __file__.replace(file_list[-1], "\성북구\성북구 범죄 뉴스_final_sorted.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")







#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++











gangdong_crime_date = []
gangdong_crime_title = []

def get_gangdong_crime():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(gangdong_crime_url)
    
    last_height = driver.execute_script("return document.body.scrollHeight")
    
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        import time
        time.sleep(0.3) 
        
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
            gangdong_crime_date.append(crime_date[0].text.strip())
        else:
            gangdong_crime_date.append("해당 정보 없음")
        
    
        crime_title = row.find_elements(By.CSS_SELECTOR, '.sds-comps-base-layout a .sds-comps-text-type-headline1')
        if crime_title:
            gangdong_crime_title.append(crime_title[0].text.strip())
        else:
            gangdong_crime_title.append("해당 정보 없음")
    
    
    
    
    driver.quit()
    

get_gangdong_crime()



gangdong_crime_news = {
    "기사날짜" : gangdong_crime_date,
    "기사제목" : gangdong_crime_title
}


gangdong_crime_df = pd.DataFrame(gangdong_crime_news)

file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스.csv")

gangdong_crime_df.to_csv(load_file, encoding='utf-8-sig')





df = pd.DataFrame(pd.read_csv(load_file))

condition_date = df['기사날짜'] != '해당 정보 없음'

condition_title = df['기사제목'] != '해당 정보 없음'

df_filtered = df[condition_date & condition_title]

df_filtered = df_filtered.reset_index(drop=True)


output_file_name = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_filterd.csv")
df_filtered.to_csv(output_file_name, encoding='utf-8-sig') # 한글 깨짐 방지를 위해 'utf-8-sig' 사용


print(f"\n✅ 처리가 완료되었습니다.")
print(f"   '기사날짜'와 '기사제목'이 모두 '해당 정보 없음'인 행이 제거된 데이터가")
print(f"   **'{output_file_name}'** 파일로 저장되었습니다.")




file_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_filterd.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df.drop_duplicates(subset=['기사제목'], keep='first')

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} duplicate rows.")

    output_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_result.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")





file_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_result.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    df_filtered = df[df['기사제목'].str.contains("범죄|성폭행|성범죄|폭행|구타|살인|절도|강도", na=False) & df['기사제목'].str.contains("강동구", na=False)]

    print(f"Filtered row count: {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows that did not satisfy the condition.")

    output_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_final.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")







file_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_final.csv")

if not os.path.exists(file_path):
    print(f"File not found: {file_path}")
else:
    try:
        df = pd.read_csv(file_path, encoding='utf-8-sig')
    except UnicodeDecodeError:
        df = pd.read_csv(file_path, encoding='cp949')

    print(f"Original row count: {len(df)}")

    current_date = pd.Timestamp("2025-12-14")

    def parse_date(date_str):
        try:
            date_str = str(date_str).strip()
            if re.match(r'^\d{4}\.\d{2}\.\d{2}\.?$', date_str):
                return pd.to_datetime(date_str.rstrip('.'), format='%Y.%m.%d')
            
            if '시간 전' in date_str or '분 전' in date_str:
                return current_date
            if '일 전' in date_str:
                days = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=days)
            if '주 전' in date_str:
                weeks = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(weeks=weeks)
            if '달 전' in date_str or '개월 전' in date_str: # Rough estimate
                months = int(re.search(r'(\d+)', date_str).group(1))
                return current_date - timedelta(days=months*30)
            
            return pd.NaT
        except:
            return pd.NaT

    df['parsed_date'] = df['기사날짜'].apply(parse_date)

    df_filtered = df.dropna(subset=['parsed_date'])
    df_filtered = df_filtered[
        (df_filtered['parsed_date'].dt.year >= 2022) & 
        (df_filtered['parsed_date'].dt.year <= 2025)
    ]

    df_filtered = df_filtered.sort_values(by='parsed_date', ascending=False)

    print(f"Filtered row count (2022-2025): {len(df_filtered)}")
    print(f"Removed {len(df) - len(df_filtered)} rows.")

    df_filtered = df_filtered.drop(columns=['parsed_date'])

    output_path = __file__.replace(file_list[-1], "\강동구\강동구 범죄 뉴스_final_sorted.csv")
    df_filtered.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"File saved successfully to {output_path}.")
