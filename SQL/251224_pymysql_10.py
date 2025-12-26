import pymysql
import pandas as pd

# ---------------------------------------------------------
# [수정 사항]
# 기존 코드에서 pymysql.connect()에 database 설정이 누락되어 있었습니다.
# 이로 인해 쿼리 실행 시 "No database selected" 에러가 발생합니다.
# database='sqldb'를 추가하여 접속 시 'sqldb'를 사용하도록 수정했습니다.
# ---------------------------------------------------------

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
    database='sqldb',    # [수정] 사용할 데이터베이스 명시
    charset="utf8"
)

# 커서 생성 (SQL 실행 객체)
cursor = db.cursor()

# ---------------------------------------------------------
# 1. userTbl에 데이터 입력 (INSERT)
# ---------------------------------------------------------
# 'STJ' (서태지) 회원 정보를 userTbl에 입력합니다.
# 이 데이터가 있어야 buyTbl(구매테이블)에서 'STJ'가 물건을 구매할 수 있습니다. (외래키 제약조건 위배 방지)
sql = "INSERT INTO userTbl VALUES('STJ', '서태지', 1975, '경기', '011', 'toortoor', 171, '2014-4-4');"
cursor.execute(sql)
db.commit() # 입력 확정 (Commit)


# ---------------------------------------------------------
# 2. buyTbl에 데이터 입력 (INSERT)
# ---------------------------------------------------------
# 위에서 입력한 'STJ' 회원이 '운동화'를 구매한 내역을 buyTbl에 입력합니다.
# userID 'STJ'가 userTbl에 존재하므로 정상적으로 입력됩니다.
sql = "INSERT INTO buyTbl (userID, prodName, groupName, price, amount) VALUES('STJ', '운동화', '의류', 30, 2);"
cursor.execute(sql)
db.commit() # 입력 확정 (Commit)


# ---------------------------------------------------------
# 3. userTbl에서 데이터 삭제 (DELETE) [에러 주의]
# ---------------------------------------------------------
# 'STJ' 회원을 userTbl에서 삭제하려고 시도합니다.
# 하지만 방금 buyTbl에 'STJ'의 구매 내역을 입력했습니다.
# userTbl의 userID는 buyTbl의 userID가 참조하고 있는 부모 키(Foreign Key)입니다.
# 자식 테이블(buyTbl)에 참조하는 데이터가 남아있는 상태에서 부모 데이터('STJ')를 삭제하려고 하면,
# "Foreign Key Constraint Violation" (외래키 제약조건 위배) 에러가 발생하여 삭제되지 않습니다.
# (만약 삭제하려면 buyTbl의 내역을 먼저 지워야 합니다.)

try:
    sql = "DELETE FROM userTbl WHERE userID='STJ'"
    cursor.execute(sql)
    db.commit()
    print("삭제 성공 (참조 데이터가 없을 경우)")
except Exception as e:
    print(f"\n[삭제 에러 발생]: {e}")
    print("설명: buyTbl에서 'STJ'를 참조하고 있기 때문에 userTbl에서 삭제할 수 없습니다.")

# 연결 종료
db.close()