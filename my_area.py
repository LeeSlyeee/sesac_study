PI = 3.14 # 원주율

def square_area(a): # 정사각형 넓이
    return a ** 2 # 한 변의 길이의 제곱

def circle_area(r): # 원 넓이
    return PI * r ** 2 # 반지름의 제곱에 원주율 곱하기

def func(a): # 테스트용 함수
    print(f"입력숫자 {a}") # 입력 숫자 출력

if __name__ == "__main__": # 이 파일이 메인 모듈로 실행될 때만 실행
    print("모듈을 직접 실행") # 메인 모듈로 실행되었음을 알림
    square_area(8) # 정사각형 넓이 함수 호출
    circle_area(5) # 원 넓이 함수 호출

else: # 이 파일이 임포트 되었을 때 실행
    func(9) # 테스트용 함수 호출