# 성적 입력칸
name = "철수"
score_dict = {"Korean":90, "Math": 95, "English": 78, "Science" : 55}
#등급 조건
level_dict = {"A":90, "B":80, "C":70, "D":60, "F":50}
#쓰기 편하게 하기
s_k = list(score_dict.keys())
s_v = list(score_dict.values())
l_k = list(level_dict.keys())
l_v = list(level_dict.values())
#코드
for i in range (len(s_k)):     #검사해야할 성적의 갯수만큼 반복
    for b in range (len(l_k)):  #등급 조건의 갯수만큼 반복
        if(s_v[i] >= l_v[b]):    #몇등급인지 확인 코드
            print(f"{name}의 {s_k[i]} 등급은 {l_k[b]}입니다.")
            break   #등급확인이 되면 반복 종료