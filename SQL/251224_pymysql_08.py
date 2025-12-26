import pymysql
import pandas as pd

# ---------------------------------------------------------
# [에러 발생 예상 구간]
# pymysql.connect() 함수에서 database="ecommerce" 옵션을 사용하고 있습니다.
# 이 옵션은 접속하자마자 사용할 데이터베이스를 지정하는 것입니다.
# 만약 MySQL 서버에 'ecommerce'라는 이름의 데이터베이스가 미리 생성되어 있지 않다면
# OperationalError (1049, "Unknown database 'ecommerce'") 에러가 발생하여 접속에 실패합니다.
# 
# [해결 방법]
# 1. MySQL 워크벤치나 콘솔에서 'CREATE DATABASE ecommerce;' 명령어로 미리 DB를 생성해 두거나,
# 2. database="ecommerce" 옵션을 제거하고 접속한 후, 코드 내에서 DB를 생성하거나 선택해야 합니다.
# ---------------------------------------------------------

try:
    # MySQL 데이터베이스에 연결
    db = pymysql.connect(
        host="127.0.0.1",       # 접속할 호스트 주소 (로컬)
        port=3306,              # 포트 번호
        user="root",            # 사용자 이름
        password='1q2w3e4r!!',  # 비밀번호
        charset="utf8"          # 문자 인코딩
    )
    print("DB 접속 성공:", db)
except Exception as e:
    # 접속 실패 시 에러 메시지 출력
    print(f"\n[DB 접속 에러 발생]: {e}")
    print("설명: 'ecommerce' 데이터베이스가 존재하지 않아서 접속에 실패했을 가능성이 높습니다.")
    # 실제로는 여기서 프로그램을 종료하거나, DB 생성 로직을 추가하는 등의 처리가 필요합니다.
    # 예제 진행을 위해 여기서 멈추도록 exit()을 호출합니다.
    exit()

# 커서 생성 (SQL 쿼리를 실행하기 위한 객체)
cursor = db.cursor()

# ---------------------------------------------------------
# SQL 쿼리문 정의
# 데이터베이스 생성 -> 사용 -> 테이블 삭제 -> 테이블 생성 순으로 쿼리가 준비되어 있습니다.
# IF NOT EXISTS / IF EXISTS를 사용하여 쿼리 실행 시 에러를 방지합니다.
# ---------------------------------------------------------

# 1. DB 생성 쿼리 ('student_mgmt'라는 DB를 새로 만듭니다)
create_db_query = """CREATE DATABASE IF NOT EXISTS student_mgmt;"""

# 2. DB 사용 쿼리 (방금 만든 'student_mgmt' DB를 사용하겠다고 선언)
# 이후 실행되는 쿼리는 student_mgmt DB에 적용됩니다.
use_db_query = """USE student_mgmt;"""

# 3. 테이블 삭제 쿼리 (만약 'students' 테이블이 이미 있다면 삭제해서 초기화)
drop_table_query = """DROP TABLE IF EXISTS students;"""

# 4. 테이블 생성 쿼리
# students 테이블 스키마 정의
# - id: 자동 증가하는 정수형 PK
# - name: 이름 (문자열)
# - gender: 성별 (ENUM 타입, 'man' 또는 'woman'만 허용)
# - birth: 생일 (DATE 타입)
# - english, math, korean: 성적 (TINYINT, 작은 정수)
create_table_query = """
CREATE TABLE students (
    id TINYINT NOT NULL AUTO_INCREMENT,
    name VARCHAR(10) NOT NULL,
    gender ENUM('man','woman') NOT NULL,
    birth DATE NOT NULL,
    english TINYINT NOT NULL,
    math TINYINT NOT NULL,
    korean TINYINT NOT NULL,
    PRIMARY KEY (id)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;
"""

# 여러 개의 INSERT 문이 세미콜론(;)으로 구분되어 있는 하나의 긴 문자열입니다.
# 아래에서 split(';')을 사용하여 각 INSERT 문을 분리하여 실행할 것입니다.
inserte_data_query = """INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('dave', 'man', '1983-07-16', 90, 80, 71);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('minsun', 'woman', '1982-10-16', 30, 88, 60);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('david', 'man', '1982-12-10', 78, 77, 30);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('jade', 'man', '1979-11-1', 45, 66, 20);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('jane', 'man', '1990-11-12', 65, 32, 90);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('wage', 'woman', '1982-1-13', 76, 30, 80);INSERT INTO students (name, gender, birth, english, math, korean) VALUES ('tina', 'woman', '1982-12-3', 87, 62, 71);"""


# ---------------------------------------------------------
# 쿼리 실행 부
# 준비된 쿼리들을 순차적으로 실행하여 DB 구조를 잡습니다.
# ---------------------------------------------------------

# DB 생성 -> 사용 -> 테이블 삭제 -> 테이블 생성
cursor.execute(create_db_query)
cursor.execute(use_db_query)
cursor.execute(drop_table_query)
cursor.execute(create_table_query)


# 데이터 입력 (INSERT)
# 세미콜론으로 구분된 쿼리들을 하나씩 실행합니다.
for query in inserte_data_query.split(';'):
    query = query.strip() # 앞뒤 공백 제거
    if query:             # 빈 문자열이 아닌 경우에만 실행
        cursor.execute(query)
        
# 변경사항(INSERT)을 실제 DB에 반영 (Commit)
db.commit()


# ---------------------------------------------------------
# 데이터 확인 (Pandas 활용)
# Pandas의 read_sql 함수를 사용하면 쿼리 결과를 바로 DataFrame으로 가져올 수 있어 편리합니다.
# ---------------------------------------------------------

# 1. DB의 테이블 목록 확인
sql = "SHOW TABLES"
df = pd.read_sql(sql, db)
print(f"showdatatable >>> \n{df}") # DB 내 테이블 리스트 출력

# 2. students 테이블의 모든 데이터 조회
sql = "SELECT * FROM students"
df = pd.read_sql(sql,db)
print(f"select >>> \n{df}") # students 테이블 내용 출력

# 3. 데이터 타입 확인 
# DataFrame의 특정 컬럼(math)의 첫 번째 값(0번 인덱스)의 타입을 확인합니다.
# read_sql로 가져온 데이터는 알맞은 파이썬/판다스 타입으로 변환되어 있습니다.
print(f"type >>> {type(df['math'][0])}")

    
# 4. 조회된 데이터를 CSV 파일로 저장
# sep=',': 콤마로 구분
# index=False: DataFrame의 인덱스 번호는 저장하지 않음
# encoding='utf-8-sig': 한글 깨짐 방지를 위한 인코딩 설정
df.to_csv('students.csv', sep=',', index=False, encoding='utf-8-sig')
print("students.csv 파일 저장 완료.")


# DB 연결 종료
db.close()