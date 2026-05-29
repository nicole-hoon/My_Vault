import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('scratch/student_data.json', 'r', encoding='utf-8') as f:
    students = json.load(f)

print(f"총 {len(students)}명의 학생 목록:")
for s in students:
    status = "특기사항 있음" if s["특기사항"] else "특기사항 없음"
    print(f"학번: {s['학번']} | 이름: {s['이름']} | 상태: {status} | 제목: {s['제목']}")
