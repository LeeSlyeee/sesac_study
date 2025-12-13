import pandas as pd


file_list = __file__.split("\\") 
load_file = __file__.replace(file_list[-1], "노원구 범죄 뉴스.csv")


df = pd.DataFrame(pd.read_csv(load_file))

condition_date = df['기사날짜'] != '해당 정보 없음'

condition_title = df['기사제목'] != '해당 정보 없음'

df_filtered = df[condition_date & condition_title]

df_filtered = df_filtered.reset_index(drop=True)


output_file_name = __file__.replace(file_list[-1], "노원구 범죄 뉴스_filterd.csv")
df_filtered.to_csv(output_file_name, encoding='utf-8-sig') # 한글 깨짐 방지를 위해 'utf-8-sig' 사용

print(f"\n✅ 처리가 완료되었습니다.")
print(f"   '기사날짜'와 '기사제목'이 모두 '해당 정보 없음'인 행이 제거된 데이터가")
print(f"   **'{output_file_name}'** 파일로 저장되었습니다.")




# df = pd.read_csv(output_file_name, sep='\s{2,}', engine='python')

# def filter_and_sort_articles(df):
#     NOW = pd.to_datetime('2025-01-30')

#     def clean_date(date_str):
#         if '일 전' in date_str:
#             days = int(date_str.replace('일 전', '').strip())
#             return NOW - pd.Timedelta(days=days)
#         elif '주 전' in date_str:
#             weeks = int(date_str.replace('주 전', '').strip())
#             return NOW - pd.Timedelta(weeks=weeks)
#         elif '면' in date_str or '단' in date_str or 'tv' in date_str or date_str == '':
#             return pd.NaT
#         else:
#             try:
#                 return pd.to_datetime(date_str.replace('.', '-', 2).strip(), format='%Y-%m-%d', errors='coerce')
#             except:
#                 return pd.NaT
            
#     print('>>>>>>>>>>>>>>>>', clean_date)


#     df['변환된 날짜'] = df['기사날짜'].apply(clean_date)

#     start_date = pd.to_datetime('2023-01-01')
#     df_filtered = df[df['변환된 날짜'] >= start_date].copy()

#     df_filtered.sort_values(by='변환된 날짜', ascending=True, inplace=True)

#     df_result = df_filtered[['기사날짜', '기사제목']].reset_index(drop=True)

#     return df_result

# df_sorted = filter_and_sort_articles(df)

# print("✅ 2023년 1월 1일 이후 기사 (날짜 순 정렬) 결과:")
# print("--------------------------------------------------")
# print(df_sorted.to_string())

# # 5. (선택) 새로운 CSV 파일로 저장

# df_sorted.to_csv('2023이후 노원구 범죄 뉴스.csv', encoding='utf-8-sig', index=False)
# print(f"\n파일 저장이 완료되었습니다: '{'2023이후 노원구 범죄 뉴스.csv''2023이후 도봉구 범죄 뉴스.csv'}'")
