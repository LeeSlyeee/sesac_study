PI = 3.14

def square_area(a):
    return a ** 2

def circle_area(r):
    return PI * r ** 2

def func(a):
    print(f"입력숫자 {a}")

if __name__ == "__main__":
    print("모듈을 직접 실행")
    square_area(8)
    circle_area(5)

else:
    func(9)