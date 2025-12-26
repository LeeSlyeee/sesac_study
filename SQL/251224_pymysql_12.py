import pymysql
import pandas as pd

# =========================================================
# 함수 정의: MySQL 데이터베이스 연결 함수
# =========================================================
def conn(d_name) :
    # 로컬 MySQL 서버 접속 정보 설정
    host_name = '127.0.0.1'
    host_port = 3306 
    username = 'root'
    password = '1q2w3e4r!!'
    database_name = d_name  # 함수 호출 시 전달받은 DB 이름 사용
    
    # pymysql.connect()를 사용하여 DB 연결 객체 생성 및 반환
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

# 1. DB 연결 ('beauty_shop' 데이터베이스 선택)
db = conn("beauty_shop")


# 2. 모든 데이터 조회 (SELECT *)
# pandas.read_sql() 함수 사용:
# - SQL 쿼리 결과(result set)를 곧바로 DataFrame 객체로 변환해줍니다.
# - 커서 생성(cursor), 실행(execute), 데이터 가져오기(fetchall), 컬럼명 매핑 등의 과정을 내부적으로 자동 처리하므로 매우 편리합니다.
sql = "SELECT * FROM product"
df = pd.read_sql(sql,db)

# 조회 결과 출력 (DataFrame 형태)
print("=== 전체 데이터 조회 ===")
print(df)


# 3. 특정 컬럼만 조회
# 필요한 컬럼(title, ori_price, discount_price)만 지정하여 가져옵니다.
sql = "SELECT title,ori_price,discount_price FROM product"
df = pd.read_sql(sql,db)

# 조회 결과 출력
print("\n=== 특정 컬럼(상품명, 가격, 할인가) 조회 ===")
print(df)


# 4. DB 연결 종료
# 작업이 끝났으므로 연결 자원을 해제합니다.
db.close()