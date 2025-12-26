from pymongo import MongoClient

# 1. MongoDB 클라이언트 연결 (기본 로컬 호스트 및 포트 사용)
# 'localhost'는 몽고DB가 설치된 컴퓨터를 의미하며, 27017은 기본 포트 번호입니다.
client = MongoClient('mongodb://localhost:27017/')

# 2. 데이터베이스 선택 (없으면 자동으로 생성됨)
# 'test_db'라는 이름의 데이터베이스를 사용합니다.
db = client['example_database']

# 3. 컬렉션 선택 (없으면 자동으로 생성됨 - RDBMS의 테이블과 비슷)
# 'users'라는 이름의 컬렉션을 사용합니다.
collection = db['users']

# ==========================================
# [참고] 방금 입력했을 것으로 가정하는 데이터 예시
# ==========================================
# insert_data = {
#     "name": "홍길동",
#     "age": 30,
#     "email": "hong@example.com",
#     "roles": ["admin", "editor"]
# }
# collection.insert_one(insert_data)
# ==========================================

print("--- 검색 결과 시작 ---")

# 4. 데이터 검색 (Find) 예제

# 4-1. 조건을 만족하는 문서 하나만 찾기 (find_one)
# 'name'이 '홍길동'인 데이터를 하나 찾아서 가져옵니다.
query = {"name": "홍길동"}
user = collection.find_one(query)

if user:
    print(f"[find_one] 찾은 사용자: {user}")
    print(f"이름: {user.get('name')}, 나이: {user.get('age')}")
else:
    print("[find_one] 해당 사용자를 찾을 수 없습니다.")

print("-" * 30)

# 4-2. 조건을 만족하는 모든 문서 찾기 (find)
# 예: 나이가 20세 이상인 모든 사용자 검색 ($gte: greater than or equal)
# 조건 연산자: $gt(초과), $gte(이상), $lt(미만), $lte(이하), $ne(같지 않음)
query_all = {"age": {"$gte": 20}}

# find()는 커서(Cursor)를 반환하므로 반복문(for)을 통해 데이터를 하나씩 꺼내야 합니다.
users_cursor = collection.find(query_all)

print(f"[find] 나이가 20세 이상인 사용자 목록:")
for doc in users_cursor:
    # '_id'는 몽고DB가 자동으로 생성하는 고유값입니다. 문자열로 변환하여 출력해봅니다.
    print(f"- ID: {str(doc['_id'])}, 이름: {doc['name']}, 이메일: {doc.get('email', '없음')}")

print("-" * 30)

# 4-3. 특정 필드만 가져오기 (Projection)
# 0은 제외, 1은 포함. (단, _id는 명시적으로 0을 주지 않으면 항상 포함됨)
# 여기서는 'name'과 'roles'만 가져오고, '_id'는 제외합니다.
projection = {"_id": 0, "name": 1, "roles": 1}
users_projected = collection.find(query, projection)

print("[find + projection] 이름과 역할만 조회:")
for doc in users_projected:
    print(doc)

# 5. 연결 종료 (권장)
client.close()
