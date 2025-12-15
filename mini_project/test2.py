import pandas as pd

# Load the data
file_path = 'mini_project/Data/서울시 부동산 실거래가 정보(2022~2025).csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Group by District ('자치구명'), Neighborhood ('법정동명'), and Building Type ('건물용도')
result = df.groupby(['자치구명', '법정동명', '건물용도'])['물건금액(만원)'].mean().reset_index()

print(result)

# Create a pivot table with District and Neighborhood as index
pivot_result = df.pivot_table(index=['자치구명', '법정동명'], columns='건물용도', values='물건금액(만원)', aggfunc='mean')
print("\n--- Pivot Table View ---")
print(pivot_result)

# Save the pivot table to a CSV file
output_path = 'mini_project/Data/구_동_기준_건물용도_가격.csv'
pivot_result.to_csv(output_path, encoding='utf-8-sig')
print(f"\nPivot table saved to {output_path}")
