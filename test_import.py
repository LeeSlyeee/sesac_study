from my_area import PI, square_area, circle_area # my_area 모듈에서 PI, square_area, circle_area를 임포트

print("PI = ", PI) # PI 출력
print("square area = ", square_area(5)) # square_area 함수 호출
print("circle area = ", circle_area(2)) # circle_area 함수 호출



from module1 import * # module1의 모든 것을 임포트
from module2 import * # module2의 모든 것을 임포트

func2() # module2의 func2() 함수 호출


import my_area as area # my_area 모듈을 area라는 이름으로 임포트

print('PI = ', area.PI) # PI 출력
print('squeare area = ', area.square_area(5)) # square_area 함수 호출
print('circle area = ', area.circle_area(2)) # circle_area 함수 호출


import random # 랜덤 모듈 임포트
import datetime # 날짜/시간 모듈 임포트
import calendar # 달력 모듈 임포트


rand = random # random 모듈을 rand라는 이름으로 임포트

rotto_data = [] # 빈 리스트 생성
for i in range(6): # 6번 반복
    rotto_data.append(rand.randint(1,45)) # 1~45 사이의 임의의 정수를 리스트에 추가

date_obj = datetime.datetime.now()# 현재 날짜/시간 정보를 가져옴

print(f"발행 시간 {date_obj}\n로또 번호 {rotto_data}입니다.") # 발행 시간과 로또 번호 출력


print(calendar.setfirstweekday(6)) # 달력의 첫 요일을 일요일(6)로 설정
print(calendar.calendar(2025)) # 2025년 달력 출력


import my_area # my_area 모듈 임포트

print(random.random()) # 0.0 ~ 1.0 사이의 임의의 부동소수점 숫자 생성

dice1 = random.randint(1,6) # 1 ~ 6 사이의 임의의 정수 생성
dice2 = random.randint(1,6) # 1 ~ 6 사이의 임의의 정수 생성
print(f"주사위 두 개의 숫자: {dice1}, {dice2}") # 주사위 두 개의 숫자 출력


print(random.randrange(0,11,2)) # 0 ~ 10(11-1) 중 임의의 짝수 선택



num1 = random.randrange(1, 10, 2) # 1 ~ 9(10-1) 중 임의의 홀수 선택
num2 = random.randrange(0,100,10) # 0 ~ 99(100-1) 중 임의의10의 단위 숫자 선택
print(f"num1: {num1}, num2: {num2}") # num1과 num2 출력


menu = ('비빔밥', '된장찌개', '볶음밥', '불고기', '스파게티', '피자', '탕수육') # 메뉴 튜플 생성
print(random.choice(menu)) # 메뉴 중 임의의 하나 선택

# 모집단에서 두 개의 인자 선택
print(random.sample([1, 2, 3, 4, 5], 2)) # 리스트에서 임의의 두 개 요소 선택

date_obj = datetime.date(2025,5,24) # 2025년 5월 24일 날짜 객체 생성
time_obj = datetime.time(23, 14, 3) # 23시 14분 3초 시간 객체 생성
datetime_obj = datetime.datetime(2025, 11, 18, 11, 1, 0) # 2025년 11월 18일 11시 1분 0초 날짜/시간 객체 생성


print(f"{date_obj}, {time_obj}, \n{datetime_obj}") # 날짜, 시간, 날짜/시간 출력


set_day = datetime.date(2021, 8, 2) # 2021년 8월 2일 날짜 객체 생성
print(set_day) # 날짜 출력

print(f"{set_day.year}|{set_day.month}|{set_day.day}") # 연도, 월, 일 출력


day1 = datetime.date(2025, 4, 1) # 2025년 4월 1일 날짜 객체 생성
day2 = datetime.date(2025, 7, 10) # 2025년 7월 10일 날짜 객체 생성
diff_day = day2 - day1 # 두 날짜의 차이 계산
print(diff_day.days) # 날짜 차이 출력


today = datetime.date.today() # 오늘 날짜 객체 생성
special_day = datetime.date(2025, 12, 24) # 2025년 12월 24일 날짜 객체 생성
print(special_day - today) # 오늘부터 special_day까지의 남은 날짜 출력


set_time = datetime.time(15, 30, 45) # 15시 30분 45초 시간 객체 생성
print(set_time) # 시간 출력
print(f"{set_time.hour}.{set_time.minute}.{set_time.second}") # 시, 분, 초 출력