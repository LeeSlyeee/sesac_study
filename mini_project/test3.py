import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os

# Set Korean font
# Check for Windows default Korean font
font_path = 'C:/Windows/Fonts/malgun.ttf'
if os.path.exists(font_path):
    font_name = fm.FontProperties(fname=font_path).get_name()
    plt.rc('font', family=font_name)
else:
    # Fallback or standard setting
    plt.rc('font', family='Malgun Gothic')

plt.rcParams['axes.unicode_minus'] = False

# Load the data
file_path = 'mini_project/Data/구_동_기준_건물용도_가격.csv'
df = pd.read_csv(file_path, encoding='utf-8')

# Melt the DataFrame to long format for seaborn
# The CSV has '자치구명', '법정동명' as columns, and building types as other columns
value_vars = [col for col in df.columns if col not in ['자치구명', '법정동명']]
df_long = df.melt(id_vars=['자치구명', '법정동명'], value_vars=value_vars, 
                  var_name='건물용도', value_name='물건금액')

# Drop NaNs (some neighborhoods might not have certain building types)
df_long = df_long.dropna(subset=['물건금액'])

# Aggregate by District and Building Type (mean of neighborhoods)
df_agg = df_long.groupby(['자치구명', '건물용도'])['물건금액'].mean().reset_index()

# Pivot for Heatmap
df_pivot = df_agg.pivot(index='자치구명', columns='건물용도', values='물건금액')

# Create visualizations
fig, axes = plt.subplots(1, 2, figsize=(20, 10))

# 1. Heatmap
sns.heatmap(df_pivot, annot=True, fmt=".0f", cmap="YlGnBu", ax=axes[0])
axes[0].set_title('구별 건물용도별 평균 물건금액 (Heatmap)')
axes[0].set_xlabel('건물용도')
axes[0].set_ylabel('자치구명')

# 2. Bar Plot
sns.barplot(x='자치구명', y='물건금액', hue='건물용도', data=df_agg, ax=axes[1])
axes[1].set_title('구별 건물용도별 평균 물건금액 (Bar Plot)')
axes[1].set_xlabel('자치구명')
axes[1].set_ylabel('평균 물건금액')
axes[1].tick_params(axis='x', rotation=45)
axes[1].legend(title='건물용도')
axes[1].grid(True, axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()
