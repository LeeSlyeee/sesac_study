import mysql.connector

# ⚠️ [필수] 접속 정보 설정
config = {
    'user': 'root',         # 예: root
    'password': 'dltjdgml12qw!@',   # 사용자 DB 비밀번호
    'host': '127.0.0.1',           # 대부분의 경우 로컬호스트(localhost) 또는 127.0.0.1
    'database': 'myDataBase'       # 이전에 만드신 데이터베이스 이름 (예: mydatabase)
}

try:
    # 데이터베이스 연결 객체 생성
    mydb = mysql.connector.connect(**config)
    
    # 연결 확인
    if mydb.is_connected():
        print("✅ MySQL 데이터베이스 연결 성공!")
        
        # 커서 객체 생성 (SQL 명령어를 실행하는 데 사용됨)
        mycursor = mydb.cursor()
        
        # --- [다음 단계: SQL 명령어 실행] ---
        
        # 3-1. INSERT 명령어 실행 예시 (데이터 삽입)
        sql = "INSERT INTO user_table (user_name, email) VALUES ('test', 'test@example.com')"
        # val = ('slyeee', 'slyeee@example.com') # %s에 들어갈 데이터는 튜플 형태로 전달합니다.
        
        mycursor.execute(sql)
        
        # 변경 사항을 데이터베이스에 반영 (필수!)
        mydb.commit()
        
        print(f"✔️ {mycursor.rowcount} 개의 레코드가 삽입되었습니다.")
        
        # 3-2. SELECT 명령어 실행 예시 (데이터 조회)
        mycursor.execute("SELECT u_id, user_name, email FROM user_table")
        
        # 조회된 모든 결과를 가져옵니다.
        results = mycursor.fetchall()
        
        print("\n📝 현재 users 테이블의 데이터:")
        for row in results:
            print(row)
        
except mysql.connector.Error as err:
    print(f"❌ 데이터베이스 연결 오류: {err}")

finally:
    # 작업 완료 후 연결을 닫습니다. (오류가 나더라도 실행되도록 finally 블록에 위치)
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("🔗 데이터베이스 연결 종료.")
        
        