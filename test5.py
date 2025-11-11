# f = open("test.py", 'r', encoding="utf-8")
# while True:
#     line = f.readline()
#     if not line: break
#     print(line)
# f.close()

# f = open('myFile.txt', 'w')
# f.write('This is my first file.')
# f.close


# w = open('myFile.txt', 'r')
# file_txt = w.read()
# w.close()
# print(file_txt)

# f = open('two_times_table.txt', 'w')
# for num in range(1,6):
#     format_string = f"2 x {num} = {2*num}\n"
#     f.write(format_string)
# f.close()


# w = open('two_times_table.txt', 'r')
# file_txt = w.read()
# w.close()
# print(file_txt)

# f = open('two_times_table.txt', 'r')
# line1 = f.readline()
# line2 = f.readline()
# f.close()
# print(line1, end="")
# print(line2, end="")


# f = open('two_times_table.txt')
# line = f.readline()
# while line:
#     print(line, end="")
#     line = f.readline()
# f.close()



# f = open('two_times_table.txt')
# lines = f.readlines()
# f.close()

# for line in lines:
#     print(line, end="")


# f = open('two_times_table.txt')
# for line in f.readlines():
#     print(line, end="")
# f.close()


f = open('two_times_table.txt')
for line in f:
    print(line, end="")
f.close()


with open('three_times_table.txt', "w") as f: 
    for num in range(1,6):
        format_str = f"3 x {num} = {num*3}\n"
        f.write(format_str)