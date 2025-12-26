import pymongo
from pymongo import MongoClient
import datetime

# 1. MongoDB 클라이언트 연결
# 기본적으로 localhost:27017에 연결합니다.
# 만약 다른 주소나 포트를 사용한다면 MongoClient('mongodb://user:password@host:port/') 형식으로 변경하세요.
client = MongoClient('mongodb://localhost:27017/')

# 2. 데이터베이스 선택 (없으면 자동으로 생성됩니다)
db = client['example_database']

# 3. 컬렉션 선택 (SQL의 Table과 유사, 없으면 자동 생성)
collection = db['users']

# ==========================================
# 예시 1: 단일 문서 삽입 (Insert One)
# ==========================================

# 삽입할 데이터 딕셔너리 생성
user_data = {
    "name": "홍길동",
    "age": 30,
    "email": "hong@example.com",
    "joined_at": datetime.datetime.now(),
    "skills": ["Python", "MongoDB"]
}

try:
    # insert_one() 메서드를 사용하여 데이터 하나를 저장합니다.
    result_one = collection.insert_one(user_data)
    
    # insert_one은 InsertOneResult 객체를 반환합니다.
    # inserted_id 속성을 통해 생성된 _id 값을 확인할 수 있습니다.
    print(f"단일 문서 삽입 성공! ID: {result_one.inserted_id}")

except Exception as e:
    print(f"단일 삽입 중 오류 발생: {e}")


# ==========================================
# 예시 2: 다중 문서 삽입 (Insert Many)
# ==========================================

# 여러 개의 데이터를 리스트로 준비합니다.
users_list = [
    {
        "name": "김철수",
        "age": 25,
        "email": "kim@example.com",
        "skills": ["Java", "Spring"]
    },
    {
        "name": "이영희",
        "age": 28,
        "email": "lee@example.com",
        "skills": ["JavaScript", "React", "Node.js"]
    },
    {
        "name": "박민수",
        "age": 35,
        "email": "park@example.com",
        "skills": ["Docker", "Kubernetes"]
    }
]

try:
    # insert_many() 메서드를 사용하여 여러 데이터를 한 번에 저장합니다.
    result_many = collection.insert_many(users_list)
    
    # insert_many는 InsertManyResult 객체를 반환합니다.
    # inserted_ids 속성을 통해 생성된 모든 _id 값들의 리스트를 확인할 수 있습니다.
    print(f"다중 문서 삽입 성공! {len(result_many.inserted_ids)}개 문 서가 추가되었습니다.")
    print(f"생성된 ID 목록: {result_many.inserted_ids}")

except Exception as e:
    print(f"다중 삽입 중 오류 발생: {e}")

# ==========================================
# 결과 확인 (데이터 조회)
# ==========================================

print("\n[현재 컬렉션에 저장된 모든 문서 출력]")
# find() 메서드로 모든 문서를 가져옵니다.
for doc in collection.find():
    print(doc)

# 연결 종료 (선택사항, 스크립트가 끝나면 자동 종료됨)
client.close()
