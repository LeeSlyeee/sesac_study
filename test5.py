# f = open("test.py", 'r', encoding="utf-8") # 파일 열기
# while True: # 무한 루프
#     line = f.readline() # 한 줄씩 읽기
#     if not line: break # 더 이상 읽을 줄이 없으면 종료
#     print(line) # 한 줄씩 출력 
# f.close() # 파일 닫기

# f = open('myFile.txt', 'w') # 파일 쓰기 모드로 열기
# f.write('This is my first file.') # 문자열 쓰기
# f.close() # 파일 닫기


# w = open('myFile.txt', 'r') # 파일 읽기 모드로 열기 
# file_txt = w.read() # 파일 내용 읽기
# w.close() # 파일 닫기
# print(file_txt) # 파일 내용 출력

# f = open('two_times_table.txt', 'w') # 파일 쓰기 모드로 열기
# for num in range(1,6): # 1부터 5까지 반복
#     format_string = f"2 x {num} = {2*num}\n" # 포맷 문자열 생성
#     f.write(format_string) # 파일에 문자열 쓰기
# f.close() # 파일 닫기


# w = open('two_times_table.txt', 'r') # 파일 읽기 모드로 열기
# file_txt = w.read() # 파일 내용 읽기
# w.close() # 파일 닫기
# print(file_txt) # 파일 내용 출력

# f = open('two_times_table.txt', 'r') # 파일 읽기 모드로 열기
# line1 = f.readline() # 한 줄 읽기
# line2 = f.readline() # 한 줄 읽기
# f.close() # 파일 닫기
# print(line1, end="") # 한 줄 출력
# print(line2, end="") # 한 줄 출력


# f = open('two_times_table.txt') # 파일 읽기 모드로 열기
# line = f.readline() # 한 줄 읽기
# while line: # 읽은 줄이 있으면 반복
#     print(line, end="") # 한 줄 출력
#     line = f.readline() # 다음 줄 읽기
# f.close() # 파일 닫기



# f = open('two_times_table.txt') # 파일 읽기 모드로 열기
# lines = f.readlines() # 모든 줄을 리스트로 읽기
# f.close() # 파일 닫기

# for line in lines: # 리스트의 각 줄에 대해 반복  
#     print(line, end="") # 한 줄 출력


# f = open('two_times_table.txt') # 파일 읽기 모드로 열기
# for line in f.readlines(): # 파일의 각 줄에 대해 반복
#     print(line, end="") # 한 줄 출력
# f.close() # 파일 닫기


f = open('two_times_table.txt') # 파일 읽기 모드로 열기
for line in f: # 파일의 각 줄에 대해 반복
    print(line, end="") # 한 줄 출력
f.close() # 파일 닫기


with open('three_times_table.txt', "w") as f: # 파일 쓰기 모드로 열기
    for num in range(1,6): # 1부터 5까지 반복
        format_str = f"3 x {num} = {num*3}\n" # 포맷 문자열 생성
        f.write(format_str) # 파일에 문자열 쓰기