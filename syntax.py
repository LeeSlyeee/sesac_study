answer_age = input("나이를 적어주세요") # 사용자에게 나이를 입력받음

if not answer_age.isalpha(): # 입력값이 숫자로만 이루어져 있는지 확인
    int_age = int(answer_age) # 문자열을 정수로 변환  
    status = "성인" if int_age >= 18 else "미성년" # 삼항 연산자를 사용하여 성인/미성년자 구분
    print(status) # 결과 출력
        
else: # 입력값이 숫자가 아닐 경우
    print("숫자로만 적어주세요") # 경고 메시지 출력
    