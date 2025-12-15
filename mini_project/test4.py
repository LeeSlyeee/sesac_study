import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set Korean font
font_path = 'C:/Windows/Fonts/malgun.ttf'
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    plt.rc('font', family='Malgun Gothic')

plt.rcParams['axes.unicode_minus'] = False

# Load the data
file_path = 'mini_project/Data/구_동_기준_건물용도_가격.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Filter for selected districts
target_districts = ['성북구', '노원구', '강동구']
df_selected = df[df['자치구명'].isin(target_districts)].copy()

print("Selected Data (First 5 rows):")
print(df_selected.head())

# Save filtered data to CSV
output_csv_path = 'mini_project/Data/3개구 건물용도별 가격.csv'
df_selected.to_csv(output_csv_path, index=False, encoding='utf-8-sig')
print(f"\nFiltered data saved to {output_csv_path}")

# Prepare data for visualization
# Melt to long format
value_vars = [col for col in df_selected.columns if col not in ['자치구명', '법정동명']]
df_long = df_selected.melt(id_vars=['자치구명', '법정동명'], value_vars=value_vars, 
                           var_name='건물용도', value_name='물건금액')
df_long = df_long.dropna(subset=['물건금액'])

# Aggregate by District and Building Type for Bar Plot
df_agg = df_long.groupby(['자치구명', '건물용도'])['물건금액'].mean().reset_index()

# Pivot for Heatmap (District vs Building Type)
df_pivot = df_agg.pivot(index='자치구명', columns='건물용도', values='물건금액')

# Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(18, 8))

# 1. Heatmap
sns.heatmap(df_pivot, annot=True, fmt=".0f", cmap="YlGnBu", ax=axes[0])
axes[0].set_title('3개구(성북, 노원, 강동) 건물용도별 평균 물건금액 (Heatmap)')
axes[0].set_xlabel('건물용도')
axes[0].set_ylabel('자치구명')

# 2. Bar Plot
sns.barplot(x='자치구명', y='물건금액', hue='건물용도', data=df_agg, ax=axes[1])
axes[1].set_title('3개구(성북, 노원, 강동) 건물용도별 평균 물건금액 (Bar Plot)')
axes[1].set_xlabel('자치구명')
axes[1].set_ylabel('평균 물건금액')
axes[1].legend(title='건물용도')
axes[1].grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
