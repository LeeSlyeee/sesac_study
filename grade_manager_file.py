"""
# 학생성적 관리 시스템

1. 학생 5명의 학생이름, 국어, 수학, 영어, 과학 점수를 입력받아
 - 학생에 따른 점수의 평균 과 전체 평균
 - 각 과목별 최대, 최소 점수

 
2-1 학생 5명에 학생이름 국어, 수학, 영어, 과학 점수를 입력받아
    파일(Student_Score.txt)

2-2. 파일(Student_Score.txt)읽어 각 학생에 따른 점수의 평균 및 전체 평균 
     각 과목평 최대,최소 점수를 result.txt을 작성하시오.
"""


# 필요한 함수 목록 
#  - 성적입력 함수 // func_input_score()
#  - 학생에 따른 점수 평균을 구하는 함수 // func_std_avg()
#  - 전체학생의 평균을 구하는 함수 // func_total_avg()
#  - 과목별 최대 점수를 구하는 함수  // find_max_score
#  - 과목별 최소 점수를 구하는 함수  // find_min_score


# func_sub_score()에서 리턴한 값을 student_dict에 추가,
# student_dict의 키값을 이용해 func_std_avg()에서 평균값을 구한다.
# 


# 파이썬 표준 라이브러리의 ast(Abstract Syntax Tree) 모듈을 
# 사용하기 위해 ast를 가져옴
import ast



# 이름과 성적을 빈 딕셔너리에 추가하는 방식으로 진행.
student_dict = {}

# 과목은 미리 정해져 있으니, 과목의 목록을 튜플로 미리 만들어 전제 조건 설정. 
subject_list = ("국어", "수학", "영어", "과학")



# tmp_data = {"이성희": [95,90,85,70], "개발자": [90,94,80,92]}



def func_input_score(name): 
    temp_dic = {}
    temp_score = []
    # 각 과목의 갯수만큼 반복문 진행
    for sub_index in range(len(subject_list)): 
        temp_score.append(int(input(f"{subject_list[sub_index]}과목의 점수는?")))

    temp_dic[name] = temp_score
    student_dict[name] = temp_score
    print(temp_dic)
# func_sub_score(name)




def func_std_avg(stdt_data, key_str): 
    tmp_score = 0
    for score_idx in range(len(subject_list)): 
        tmp_score += stdt_data[key_str][score_idx]

    print(f"{key_str}의 평균점수는 {tmp_score / len(subject_list)}점 입니다.")

    with open(f"Result_avg[{key_str}].txt", "w", encoding="utf-8") as result_avg:
        result_avg.write(f"{key_str}의 평균점수는 {tmp_score / len(subject_list)}점 입니다.")
# func_std_avg(tmp_data,'개발자')





def func_total_avg(student_dict):
    acc_score = 0
    for stdt_name, scores in student_dict.items():
        for tmp_total in student_dict[stdt_name]:
            acc_score += tmp_total
    
    print(acc_score / (len(student_dict[stdt_name]) * len(student_dict.keys())))

    with open("Result_total_avg.txt", "w", encoding="utf-8") as result_total_avg:
        result_total_avg.write(f"학생들 전체 평균점수는 {acc_score / (len(student_dict[stdt_name]) * len(student_dict.keys()))}점 입니다.")
# func_total_avg(tmp_data)





def find_max_score(subject_list, student_dict):
    max_scores = {}
    all_scores = student_dict.values()

    # subject_list의 길이를 사용하여 0부터 시작하는 인덱스(subject_idx)를 생성.
    for subject_idx in range(len(subject_list)):
        # 현재 인덱스(subject_idx)에 해당하는 과목 이름을 가져오기.
        subject = subject_list[subject_idx]
        current_subject_scores = []  # 결과를 저장할 빈 리스트 초기화

        # 모든 학생의 점수 목록을 순회.
        for scores in all_scores:
            # 각 점수 목록(scores)에서 특정 과목 인덱스(subject_idx)에 해당하는 점수 추출.
            score_for_subject = scores[subject_idx]
            current_subject_scores.append(score_for_subject)

        max_score = max(current_subject_scores)
        max_scores[subject] = max_score

    print(max_scores) 

    with open("Result_max_scores.txt", "w", encoding="utf-8") as result_max:
        result_max.write(f"과목별 최고점수는 {max_scores} 입니다.")

# find_max_score(subject_list, tmp_data)




def find_min_score(subject_list, student_dict):
    min_scores = {}
    all_scores = student_dict.values()
    
    for subject_idx in range(len(subject_list)):
        # 현재 인덱스(subject_idx)에 해당하는 과목 이름을 가져오기.
        subject = subject_list[subject_idx]      
        current_subject_scores = []  # 결과를 저장할 빈 리스트 초기화
        
        # 모든 학생의 점수 목록을 순회.
        for scores in all_scores:
            # 각 점수 목록(scores)에서 특정 과목 인덱스(subject_idx)에 해당하는 점수 추출.
            score_for_subject = scores[subject_idx]
            current_subject_scores.append(score_for_subject)
            
        min_score = min(current_subject_scores)
        min_scores[subject] = min_score

    print(min_scores)

    with open("Result_min_scores.txt", "w", encoding="utf-8") as result_min:
        result_min.write(f"과목별 최소점수는 {min_scores} 입니다.")
# find_min_score(subject_list, tmp_data)



#######################################################################################

def score_manager_program():
    while len(student_dict.keys()) < 2:
        # 각 학생의 성적을 입력받는다. 
        name_str = input("학생의 이름은?")
        # 성적입력 함수 실행
        func_input_score(name_str)

    with open("Student_Score.txt", "w", encoding="utf-8") as st_sc_w:
        st_sc_w.write(str(student_dict))

    with open("Student_Score.txt", "r", encoding="utf-8") as st_sc_r:
        # 파이썬 리터럴(문자열, 숫자, 튜플, 리스트, 딕셔너리, 불리언 등)만 안전하게 평가하여
        # 텍스트를 딕셔너리로 변환함
        student_dict_file = ast.literal_eval(st_sc_r.read()) 

    command = input(
    """
    ---------------------------------------------------
        작업내용을 입력해주세요
                    
        - 학생 별 평균값을 구하려는 경우 "1"을 입력
        - 전체 학생의 평균값을 구하려는 경우 "2"를 입력
        - 각 과목별 최고 점수를 구하려는 경우 "3"을 입력
        - 각 과목별 최소 점수를 구하려는 경우 "4"를 입력
    ---------------------------------------------------
                    
    """)
    if command == "1":
        print("---------- 학생평균 ----------")
        for stdt_name, scores in student_dict.items():
            func_std_avg(student_dict_file, stdt_name)

    if command == "2":
        print("---------- 전체평균 ----------")
        func_total_avg(student_dict_file)

    if command == "3":
        print("---------- 과목최고 ----------")
        find_max_score(subject_list, student_dict_file)
    
    if command == "4":
        print("---------- 과목최소 ----------")
        find_min_score(subject_list, student_dict_file)

score_manager_program()




