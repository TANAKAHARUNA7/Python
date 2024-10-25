import csv


file_path = r"Lab\7,11\2024_std_num_high_school.csv"

# 파일 열고
# 모든 레코드를 순희

# "시도교육청" -> 중복되지 않은 값을 출력
education_office = set()

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        # 중복되지 않은 "시도교육청" 필드를 리스트에 추가
        education_office.add(row['시도교육청'])
        
# 중복되지 않은 "시도교육청" 리스트 값 출력        
for index, item in enumerate(education_office, start=1):
    print(f"{index}번, {item}")