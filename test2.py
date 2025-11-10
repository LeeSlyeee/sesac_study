chulsu = {"국어": 90, "수학": 95, "영어": 78, "과학": 55, "기술": 94}
grade = {"A": 90, "B": 80, "C": 70, "D": 60} # 등급 기준은 if/elif 문에서 사용됩니다.

"""
딕셔너리의 key와 value를 동시에 순회합니다.
chulsu.items()값은 [('국어', 90), ("수학", 95)]과 같이 튜플을 요소값으로 가진 리스트형태로 출력됨
따라서 튜플 언패킹을 사용할 수 있다. 

튜플의 첫 번째 요소 (키, 즉 과목 이름)는 변수 subject에 할당.
튜플의 두 번째 요소 (값, 즉 점수)는 변수 score에 할당.
""" 
for subject, score in chulsu.items(): 
    if score >= 90:
        result_grade = "A"
    elif score >= 80:
        result_grade = "B"
    elif score >= 70:
        result_grade = "C"
    elif score >= 60:
        result_grade = "D"
    else:
        result_grade = "F" # D 미만은 F로 처리

    print(f"{subject} 점수는 {score}점이고, 등급은 {result_grade}입니다.")




"""
chulsu = {"국어": 90, "수학": 95, "영어": 78, "과학": 55, "기술": 87}

# 등급 기준: 딕셔너리의 키는 등급, 값은 최소 점수를 의미
grade_criteria = {"A": 90, "B": 80, "C": 70, "D": 60, "A+": 85} 

# 튜플의 두 번째 요소(점수)를 반환하는 사용자 정의 함수
def get_score(item):
    '''(등급, 점수) 튜플에서 점수(인덱스 1)를 반환합니다.'''
    return item[1]

# sorted_grades = sorted(grade_criteria.items(), key=get_score, reverse=True)
# print(sorted_grades)


for subject, score in chulsu.items(): 
    result_grade = "F"  # 기본 등급은 F로 설정

    # get_score 함수를 사용하여 튜플의 두 번째 요소(점수)를 기준으로 정렬합니다.
    # reverse=True로 내림차순 정렬하여 높은 점수 기준부터 확인합니다.
    # sorted_grades는 [('A', 90), ('B', 80), ...] 순서가 됩니다.
    sorted_grades = sorted(grade_criteria.items(), key=get_score, reverse=True)    
    for grade, min_score in sorted_grades:
        if score >= min_score:
            result_grade = grade
            break  # 기준을 만족하는 가장 높은 등급을 찾았으므로 루프를 즉시 종료합니다.

    print(f"{subject}점수는 {score}점이고, 등급은 {result_grade}입니다.")

    """






total_price = 72500
menu1 = 12000
menu2 = 9000
beer = 2500

member = {'a': 3, 'b': 3, 'c': 5}

menu_avg = menu1 + menu2 / len(member.keys())


beer_total_price = total_price - (menu1 + menu2)

# print("병일형님의 가격은 ", int(beer * member['a'] + menu_avg), "원 입니다.")
# print("가연씨의 가격은 ", int(beer * member['b'] + menu_avg), "원 입니다.")
# print("성희의 가격은 ", int(beer * member['c'] + menu_avg), "원 입니다.")

tmp_total = int((beer * member['a'] + menu_avg) + (beer * member['b'] + menu_avg) + (beer * member['c'] + menu_avg))

print(tmp_total)

if total_price == int((beer * member['a'] + menu_avg) + (beer * member['b'] + menu_avg) + (beer * member['c'] + menu_avg)):
    print("정산이 정상적으로 완료 됨")

else:
    print("정산 실패")