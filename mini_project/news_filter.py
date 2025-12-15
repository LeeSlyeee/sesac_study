import pandas as pd


file_list = __file__.split("\\") 
input_file_path = __file__.replace(file_list[-1], "재개발뉴스 크롤링\재개발뉴스.csv")
output_file_path = __file__.replace(file_list[-1], "재개발뉴스 크롤링\재개발뉴스2.csv")



df1 = pd.read_csv(input_file_path, encoding='utf-8-sig')

df1.to_csv(output_file_path, encoding='utf-8-sig')


# import io

# file_list = __file__.split("\\") 
# input_file_path = __file__.replace(file_list[-1], "재개발뉴스 크롤링\재개발뉴스.csv")
# output_file_path = __file__.replace(file_list[-1], "재개발뉴스 크롤링\재개발뉴스2.csv")


# # 2. 파일 읽기 (UTF-8 인코딩 지정)
# try:
#     with io.open(input_file_path, 'r', encoding='utf-8') as infile:
#         content = infile.read()
    
#     print("✅ 파일 읽기 성공 (원본 인코딩: UTF-8)")

#     # 3. 파일 쓰기 (CP949 인코딩 지정)
#     # Windows 환경에서 구형 Excel 호환성을 위해 많이 사용됨
#     with io.open(output_file_path, 'w', encoding='cp949') as outfile:
#         outfile.write(content)
        
#     print(f"✅ 파일 쓰기 성공 (대상 인코딩: CP949). 파일 저장 위치: {output_file_path}")

# except FileNotFoundError:
#     print(f"❌ 오류: 파일을 찾을 수 없습니다. 경로를 확인해주세요: {input_file_path}")
# except UnicodeDecodeError as e:
#     print(f"❌ 오류: 파일 디코딩 실패. 원본 파일의 인코딩이 UTF-8이 아닐 수 있습니다. {e}")
# except Exception as e:
#     print(f"❌ 예상치 못한 오류 발생: {e}")