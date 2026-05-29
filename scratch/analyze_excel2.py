import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df = pd.read_excel('심국.xlsx')

print("=== 고유한 제목 목록 (특기사항이 있는 학생 대상) ===")
# NaN을 제외한 고유 제목과 해당 제목을 가진 학생 수
valid_df = df[df['제목'].notna()]
unique_titles = valid_df['제목'].value_counts()
print(unique_titles)

print("\n=== 고유한 제목 및 주요내용 조합 ===")
unique_combinations = valid_df.groupby(['제목', '주요내용']).size().reset_index(name='count')
for idx, row in unique_combinations.iterrows():
    print(f"[{idx+1}] 제목: {row['제목']}")
    print(f"주요내용: {row['주요내용'][:100]}...")
    print(f"학생 수: {row['count']}")
    print("-" * 50)
