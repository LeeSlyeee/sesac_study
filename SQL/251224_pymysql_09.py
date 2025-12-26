import pymysql
import pandas as pd

# MySQL 접속 설정 정보
host_name = '127.0.0.1'  # localhost
host_port = 3306         # MySQL 기본 포트
username = 'root'        # 사용자 이름
password = '1q2w3e4r!!'  # 비밀번호

# 데이터베이스 연결
db = pymysql.connect(
    host=host_name, 
    port=host_port,
    user=username,
    password=password,
    charset="utf8"
)

# 커서 생성 (SQL 실행을 위한 객체)
cursor = db.cursor()

# 현재 실행 중인 파일의 경로를 기반으로 'sqlDB.sql' 파일 경로 생성
file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "sqlDB.sql")

# 여러 쿼리문이 들어있는 sqlDB.sql 파일을 읽어서 데이터베이스 초기화
# sqlDB.sql 파일 내용: DB 생성, 테이블 생성, 초기 데이터 INSERT 등
with open(load_file, 'r', encoding='utf-8') as f:
    sql_file = f.read()
    
# 세미콜론(;)을 기준으로 쿼리문 분리
sql_querys = sql_file.split(";")

# 분리된 쿼리문을 순차적으로 실행
for query in sql_querys:
    query = query.strip()  # 앞뒤 공백 제거
    if query:              # 빈 문자열이 아닌 경우 실행
        cursor.execute(query)
        
# 변경사항(초기화 작업)을 데이터베이스에 반영
db.commit()


# usertbl(회원 테이블) 조회 및 데이터프레임으로 출력
print("=== usertbl 조회 ===")
sql = "SELECT * FROM usertbl"
df = pd.read_sql(sql, db)
print(df)

# buytbl(구매 테이블) 조회 및 데이터프레임으로 출력
print("\n=== buytbl 조회 ===")
sql = "SELECT * FROM buytbl"
df = pd.read_sql(sql, db)
print(df)


# ---------------------------------------------------------
# [에러 발생 구간 분석]
# 아래 코드에서 IntegrityError (Foreign Key Constraint Violation)가 발생합니다.
# 
# 에러 메시지 예시: 
# Cannot add or update a child row: a foreign key constraint fails ...
#
# 원인:
# buytbl의 'userID' 컬럼은 usertbl의 'userID'를 참조하는 외래키(Foreign Key)입니다.
# 즉, buytbl에 데이터를 넣으려면, 해당 userID가 반드시 usertbl에 먼저 존재해야 합니다.
# 현재 usertbl에는 'STJ'라는 아이디를 가진 회원이 없습니다.
# 따라서 존재하지 않는 회원이 구매 내역을 남기려고 하므로 DB 무결성 원칙에 의해 에러가 발생합니다.
# ---------------------------------------------------------

# 커서 다시 생성 (필수는 아니지만 명시적으로 생성)
cursor = db.cursor()

try:
    sql = "INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('STJ', '운동화', '의류', 30, 2);"
    cursor.execute(sql) # 여기서 에러 발생! ('STJ' 유저 없음)
    db.commit()
except Exception as e:
    print(f"\n[에러 발생]: {e}")
    print("설명: 'STJ'라는 userID가 usertbl에 존재하지 않기 때문에 외래키 제약 조건을 위반하여 입력에 실패했습니다.")


# ---------------------------------------------------------
# 아래 코드는 정상 실행되어야 하는 코드입니다.
# 'BBK' (바비킴)은 usertbl에 이미 존재하는 회원입니다.
# 하지만 위에서 에러가 발생하여 프로그램이 멈추면 이 코드는 실행되지 않습니다.
# ---------------------------------------------------------

cursor = db.cursor()
sql = "INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('BBK', '운동화', '의류', 30, 2);"
try:
    cursor.execute(sql)
    db.commit()
    print("\n'BBK' 구매 내역 정상 입력 완료")
except Exception as e:
    print(f"에러 발생: {e}")

# 연결 종료
db.close()