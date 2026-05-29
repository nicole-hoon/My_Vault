import pandas as pd
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 엑셀 파일 로드
df = pd.read_excel('심국.xlsx')

# 결측치를 None으로 변환
df_filled = df.where(pd.notnull(df), None)

students = []
for idx, row in df_filled.iterrows():
    student = {
        "학번": int(row["학번"]),
        "이름": row["이름"],
        "제목": row["제목"],
        "주요내용": row["주요내용"],
        "쟁점1": row["쟁점1"],
        "쟁점2": row["쟁점2"],
        "쟁점3": row["쟁점3"],
        "특기사항": row["특기사항"]
    }
    students.append(student)

# JSON 파일로 저장
with open('scratch/student_data.json', 'w', encoding='utf-8') as f:
    json.dump(students, f, ensure_ascii=False, indent=2)

print(f"성공적으로 {len(students)}명의 학생 데이터를 scratch/student_data.json에 저장했습니다.")
