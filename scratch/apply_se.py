import pandas as pd
import json
import os
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 파일 경로 정의
excel_file = '심국.xlsx'
output_file = '결과.xlsx'
scratch_dir = 'scratch'

# JSON 조각들을 읽어서 하나의 딕셔너리로 합침
all_se = {}
parts = ['se_part1.json', 'se_part2.json', 'se_part3.json']

for part in parts:
    path = os.path.join(scratch_dir, part)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            # data는 학번(str 또는 int)을 key로 하고 세특 문장을 value로 하는 딕셔너리
            for k, v in data.items():
                all_se[int(k)] = v

print(f"로드된 세특 데이터 개수: {len(all_se)}")

# 엑셀 로드 및 형변환
df = pd.read_excel(excel_file)
df['세특'] = df['세특'].astype(object)

# 세특 입력
updated_count = 0
for idx, row in df.iterrows():
    s_id = int(row['학번'])
    if s_id in all_se:
        df.at[idx, '세특'] = all_se[s_id]
        updated_count += 1
    else:
        print(f"경고: 학번 {s_id} ({row['이름']})의 세특 데이터가 없습니다.")

# 결과 저장
df.to_excel(output_file, index=False)
print(f"성공적으로 {updated_count}명의 세특을 업데이트하여 '{output_file}'에 저장했습니다.")
