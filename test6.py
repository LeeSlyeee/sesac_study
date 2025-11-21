'''
첫줄은 날짜 에스프레소 아메리카노 카페라테 카푸치노 의 구분이므로
딕셔너리 형태로 키는 날짜 / 값은 튜플의 형태로 저장해야한다. 
커피의 종류는 순서대로 지정되야 하므로 튜플로 저장해둔다

예시) 
coffee_type = ("에스프레소","아메리카노","카페라테","카푸치노")
date_by_sales_data = {"10.15": (10,50,45,20), ... }

이후 키에 해당하는 날짜의 튜플데이터를 이용하여 날짜별 총 판매량 및 전체 판매량을 구한다.
날짜 별 총 판매량은 날짜에 해당하는 튜플데이터를 모두 합산하고
전체판매량은 for문으로 키값에 해당하는 값을 순회하면서 모두 합산한 값이다.

'''


f = open("coffee.txt", "r", encoding="utf-8") # 파일 읽기 모드로 열기
header = f.readline() # 첫번째 줄 읽기
header_list = header.split() # 공백 기준으로 분리하여 리스트로 저장

# print(header_list) # 헤더 리스트 출력

date_by_sales_data = {} # 날짜별 판매량을 저장할 딕셔너리
for line in f: # 파일의 각 줄을 순회
    data_list = line.split() # 공백 기준으로 분리하여 리스트로 저장
    date = data_list[0] # 첫번째 요소는 날짜
    sales_tuple = tuple(map(int, data_list[1:])) # 나머지 요소들은 판매량, 정수형으로 변환 후 튜플로 저장
    date_by_sales_data[date] = sales_tuple # 딕셔너리에 날짜와 판매량 튜플 저장



# f = open("coffee.txt", "r", encoding="utf-8")
# header = f.readline()
# header_list = header.split()

# # print(header_list)

# for line in f:
#     data_list = line.split()
#     # print(data_list)
    
#     date_key_list = []
#     dete_date_list = []


#     for date_data in data_list:
#         if data_list[0]:
#             date_key_list.append(data_list[::-4])
#         else:
#             pass


#     print(date_key_list)



