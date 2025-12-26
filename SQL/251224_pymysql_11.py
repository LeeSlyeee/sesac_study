from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import pymysql
import emoji
from tqdm import tqdm

# =========================================================
# 함수 정의: MySQL 데이터베이스 연결 함수
# =========================================================
def conn(d_name) :
    # DB 접속 정보 설정
    host_name = '127.0.0.1'  # 로컬호스트 IP
    host_port = 3306         # MySQL 기본 포트
    username = 'root'        # MySQL 계정 아이디
    password = '1q2w3e4r!!'  # MySQL 계정 비밀번호
    database_name = d_name   # 접속할 데이터베이스 이름 (함수 인자로 받음)
    
    # pymysql을 사용하여 DB 연결 객체 생성
    db = pymysql.connect(
        host=host_name, 
        port=host_port, 
        user=username, 
        password=password, 
        database=database_name, 
        charset='utf8'
    )
    return db

# =========================================================
# 메인 로직 시작
# =========================================================

# 1. DB 연결 ('beauty_shop' 데이터베이스에 접속)
# 주의: 'beauty_shop' DB가 미리 생성되어 있어야 합니다. 없다면 에러 발생.
db = conn('beauty_shop')

# 2. 커서 생성 (쿼리 실행을 위한 객체)
cursor = db.cursor()

# 3. 현재 존재하는 데이터베이스 목록 확인 (테스트용)
sql = "SHOW DATABASES"
cursor.execute(sql)
result = cursor.fetchall()
print(f"Databases List: {result}")


# 4. 'beauty_shop' DB 사용 선언 (conn 함수에서 이미 지정했지만 명시적으로 한번 더 확인)
sql = "USE beauty_shop"
cursor.execute(sql)

# 5. 현재 DB의 테이블 목록 확인
sql = "SHOW TABLES"
cursor.execute(sql)
result = cursor.fetchone() # 하나만 가져오기 (테스트)
print(f"Current Tables: {result}")

# 6. 상품 정보를 저장할 'product' 테이블 생성
# IF NOT EXISTS: 테이블이 없을 때만 생성
# PRODUCT_CODE: 자동 증가(AUTO_INCREMENT)하는 PK
# TITLE: 상품명
# ORI_PRICE: 원래 가격
# DISCOUNT_PRICE: 할인 가격
# link: 상품 상세 페이지 링크
sql = '''
CREATE TABLE IF NOT EXISTS product (
    PRODUCT_CODE int AUTO_INCREMENT NOT NULL,
    TITLE VARCHAR(200) NOT NULL,
    ORI_PRICE VARCHAR(100),
    DISCOUNT_PRICE VARCHAR(100),
    link VARCHAR(200),
    PRIMARY KEY(PRODUCT_CODE)
);
'''
cursor.execute(sql)
db.commit() # 테이블 생성 확정


# 7. 테이블 생성 후 확인
sql = "SHOW TABLES"
cursor.execute(sql)
result = cursor.fetchall()
print(f"Tables after create: {result}")


# 8. product 테이블 구조(스키마) 확인
sql = "DESC product"
cursor.execute(sql)
result = cursor.fetchall()
print(f"Table Schema: {result}")



# =========================================================
# 웹 크롤링 및 데이터 수집 함수 정의
# =========================================================

# 크롤링 테스트용 URL
url="http://jolse.com/category/toners-mists/1019/"
html = urlopen(url)
htmls = html.read()
bs_obj = BeautifulSoup(htmls,"html.parser")


# 함수: 하나의 상품 박스(HTML 요소)에서 정보 추출
def get_product_info(box) :
    # 상품명 태그 찾기
    strong_tag = box.find("strong",{"class":"name"})
    
    # 상품명(TITLE) 추출 ('상품명 : 실제이름' 형식이어서 split으로 분리)
    span =strong_tag.text.split(':',1)[1]
    
    # 상세 페이지 링크 추출
    a = strong_tag.find("a")
    sub_link = 'https://jolse.com' + a["href"]
    # 링크에 포함된 이모지 제거 (DB 저장 시 인코딩 문제 방지)
    sub_link = emoji.replace_emoji(sub_link,'')
    
    # 가격 정보 추출 (ul 태그 안에 li로 가격들이 나열됨)
    price_ul = box.find("ul")
    
    # 원래 가격 (첫 번째 li)
    old_price = price_ul.select("li")[0]
    old_price = old_price.select("span")[1].text
    old_price = old_price.split(" ")[1] # '$ 20.00' 형식에서 숫자만 추출
    
    # 할인 가격 (두 번째 li)
    dis_price = price_ul.select("li")[1]
    dis_price = dis_price.select("span")[1].text
    dis_price = dis_price.split(" ")[1] # '$ 15.00' 형식에서 숫자만 추출
    
    # 데이터 전처리
    # SQL 쿼리에서 작은따옴표(')는 문자열 구분자이므로, 데이터 내의 '를 ''로 치환(Escape)
    title = span.replace("'","''") 
    title = emoji.replace_emoji(title,'') # 이모지 제거
    
    # 할인 가격이 비어있으면 0.0으로 처리
    if dis_price =='' :
        dis_price = '0.0'
        
    # 추출된 데이터를 딕셔너리로 반환
    return {"prd_name":title, "price":old_price, "sale_price":dis_price, "sub_link":sub_link}


# 함수: 추출된 상품 정보를 DB에 저장 (INSERT)
def save_data(prd_info) :
    # print(prd_info) # 디버깅용 출력
    
    # INSERT 쿼리문 생성 (f-string 대신 문자열 결합 방식 사용됨)
    # 문자열 값 앞뒤로 작은따옴표(')를 붙여줘야 함에 유의
    sql = "INSERT INTO product (title, ori_price, discount_price, link) values('" \
    + prd_info["prd_name"] \
    +"'," \
    + prd_info['price']\
    +"," \
    + prd_info['sale_price']\
    +",'"\
    + prd_info['sub_link']\
    + "');"
    
    # 완성된 쿼리문 확인용 출력 (필요 시 주석 해제)
    # print(sql)
    
    # 쿼리 실행
    cursor.execute(sql)


# 함수: 특정 페이지 URL의 모든 상품 정보를 가져와서 DB에 저장
def get_page_products(url) :
    url=url
    html = urlopen(url)
    htmls = html.read()
    bs_obj = BeautifulSoup(htmls,"html.parser")
    
    # 상품 리스트가 있는 ul 태그 찾기
    ul=bs_obj.find("ul",{"class":"prdList grid5"})
    
    # 각 상품 정보를 담고 있는 div 박스들 찾기
    prd_boxes = ul.findAll("div", {"class":"description"}) 
    
    # 각 상품 박스를 순회하며 정보 추출 및 DB 저장
    for box in prd_boxes :
        prd = get_product_info(box) # 정보 추출 함수 호출
        # print(prd) # 디버깅용
        save_data(prd) # DB 저장 함수 호출


# =========================================================
# 실제 크롤링 실행부 (페이지 순회)
# =========================================================

# 크롤링 대상 기본 URL
url = "http://jolse.com/category/toners-mists/1019/?page="

# 마지막 페이지 번호를 자동으로 찾으려면 아래 주석 해제하여 사용
# last = int(bs_obj.find("a",{"class":"last"})['href'].split("=")[1])

# 실습을 위해 2페이지까지만 크롤링하도록 설정
last = 2

# 1페이지부터 last 페이지까지 반복 (tqdm으로 진행상황 표시)
for i in tqdm(range(1,last+1)):
    urlfin =url + str(i) # 페이지 번호를 붙여 최종 URL 생성
    get_page_products(urlfin) # 해당 페이지 크롤링 및 DB 저장

# 모든 데이터 입력 후 변경사항 확정 (Commit)
db.commit()


# ---------------------------------------------------------
# 저장된 데이터 확인
# ---------------------------------------------------------
print("=== 저장된 데이터 확인 (상위 5개) ===")
sql = "SELECT * FROM product"
cursor.execute(sql)
result = cursor.fetchall()

# 상위 5개만 출력해서 확인
for row in result[:5]:
    print(row)

# DB 연결 종료
db.close()