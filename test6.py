a = 5

def func1():
    a = 1
    print("[func1] 지역 변수 = a ", a)

def func2():
    a = 2
    print("[func2] 지역 변수 = a ", a)

def func3():
    print("[func3] 전역 변수 = a ", a)

def func4():
    global a 
    a = 4
    print("[func4] 전역 변수 = a ", a)



func1()
func2()
func3()
func4()