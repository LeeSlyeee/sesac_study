"""
while문 - 구구단 출력 프로그램 
"""

# while문을 사용하기 위한 초기변수를 dan으로 설정 값은 2로 설정함(구구단은 2단부터 시작하므로)
dan = 2

# while문의 조건을 9이하로 설정함
while dan <= 9: 
    # print문으로 현재 구구단 수를 화면에 출력
    print(f"------- {dan}단 -------")

    # 이중 while문을 사용해야 하므로 변수 설정 기본값 0
    multi = 0 
    
    # while문 조건을 9이하로 설정 이유는 while문 내 변수 multi를 증가시켜주므로.
    while multi < 9:
        # 곱셈값을 1씩 증가 시킴
        multi += 1
        # 구구단을 만들기 위한 기본 수식을 result에 할당
        result = dan * multi
        # 해당 구구단을 화면에 출력 
        print(f" {dan} x {multi} = {result}")

        
    
    # 해당 단이 끝났으므로 현재 구구단 수를 1증가 시킴 
    dan += 1
    print()

    # 현재 단수가 상위 while문의 조건을 만족하면 반복 실행. 사실상 필요없는 구문
    continue
