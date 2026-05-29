import pandas as pd
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

df = pd.read_excel('결과.xlsx')

print("=== 결과.xlsx 검증 ===")
print(f"총 행 수: {len(df)}")
print(f"세특 작성 완료 학생 수: {df['세특'].notna().sum()}")
print(f"세특 미작성 학생 수: {df['세특'].isna().sum()}")

print("\n=== 글자수 검증 ===")
for idx, row in df.iterrows():
    if pd.notna(row['세특']):
        length = len(str(row['세특']))
        status = "✓" if 250 <= length <= 800 else "⚠ 글자수 이상"
        print(f"{row['학번']} {row['이름']}: {length}자 {status}")
