import pandas as pd
import sys
import io

# 한글 출력을 위한 표준 출력 인코딩 설정
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 엑셀 파일 로드
df = pd.read_excel('심국.xlsx')

print("=== 엑셀 컬럼 정보 ===")
print(df.columns.tolist())

print("\n=== 데이터 정보 ===")
print(f"전체 행 개수: {len(df)}")
print(f"특기사항이 있는 학생 수: {df['특기사항'].notna().sum()}")
print(f"특기사항이 없는 학생 수: {df['특기사항'].isna().sum()}")

print("\n=== 특기사항이 있는 학생 예시 ===")
sample_with = df[df['특기사항'].notna()].head(2)
for idx, row in sample_with.iterrows():
    print(f"학번: {row['학번']}, 이름: {row['이름']}")
    print(f"제목: {row['제목']}")
    print(f"주요내용: {row['주요내용']}")
    print(f"쟁점1: {row['쟁점1']}, 쟁점2: {row['쟁점2']}, 쟁점3: {row['쟁점3']}")
    print(f"특기사항: {row['특기사항']}")
    print("-" * 50)

print("\n=== 특기사항이 없는 학생 예시 ===")
sample_without = df[df['특기사항'].isna()].head(2)
for idx, row in sample_without.iterrows():
    print(f"학번: {row['학번']}, 이름: {row['이름']}")
    print(f"제목: {row['제목']}")
    print(f"주요내용: {row['주요내용']}")
    print("-" * 50)
