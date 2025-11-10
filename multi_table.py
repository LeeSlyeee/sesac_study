#
# 개요 : 이중 반복문으로 만든 구구단 출력 기능 
#

# range()함수를 통해서 2~9까지 반복 실행
for target in range(2,10):
    print(f"---{target}단---")
    
    # 아직 상위 반복문을 진행하고 있는 상태임.
    # 해당 반복문은 1~9까지 반복문을 진행함
    for number in range(1,10):
        # taget x number 의 값을 result에 할당함
        result = target * number
        print(target, "x", number, "=", result, sep="\t")
print("진짜 감사합니다.")
