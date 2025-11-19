# 프로젝트의 특성상 과목갯수와 점수는 일치하여야 함.
score = [90,95,78,55] # 국어, 수학, 영어, 과학 점수
course = ["국어", "수학", "영어", "과학"] # 과목명

def rating_system(index): # 등급 산출 함수
    scores = score[index] # 점수 변수
    courses = course[index] # 과목명 변수

    if scores >= 90: # 90점 이상 A등급
        print(f"{courses} 등급은 A등급입니다.")  #90점 이상 A등급
    elif scores >= 80: # 80점 이상 B등급
        print(f"{courses} 등급은 B등급입니다.")
    elif scores >= 70: # 70점 이상 C등급
        print(f"{courses} 등급은 C등급입니다.")
    elif scores >= 60: # 60점 이상 D등급
        print(f"{courses} 등급은 D등급입니다.")
    else: # 60점 미만 F등급
        print(f"{courses} 등급은 F등급입니다.")

for i in range(len(score)): # 점수 리스트 길이만큼 반복
    rating_system(i) # 등급 산출 함수 호출
    


    