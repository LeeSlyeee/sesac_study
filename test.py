# 프로젝트의 특성상 과목갯수와 점수는 일치하여야 함.
score = [90,95,78,55]
course = ["국어", "수학", "영어", "과학"]

def rating_system(index):
    scores = score[index]
    courses = course[index]

    if scores >= 90:
        print(f"{courses} 등급은 A등급입니다.")
    elif scores >= 80:
        print(f"{courses} 등급은 B등급입니다.")
    elif scores >= 70:
        print(f"{courses} 등급은 C등급입니다.")
    elif scores >= 60:
        print(f"{courses} 등급은 D등급입니다.")
    else:
        print(f"{courses} 등급은 F등급입니다.")

for i in range(len(score)):
    rating_system(i)
    


    