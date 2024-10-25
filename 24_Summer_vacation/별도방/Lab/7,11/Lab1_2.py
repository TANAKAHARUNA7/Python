import csv

file_path = r"Lab\7,11\2024_std_num_high_school.csv"

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    total_male_students = 0
    total_female_students = 0
    
    for row in csv_reader:
        total_male_students += int( row['계(남)']) if row['계(남)'].isdigit() else 0  # isdigit →　資料型が数字かどうか確認する
        total_female_students += int( row['계(여)']) if row['계(여)'].isdigit() else 0
        
        total_student = total_male_students + total_female_students
        male_percentage = total_male_students / total_student * 100
        female_percentage = total_female_students / total_student * 100
        
        
print(f"{total_student:,} 명")
print(f"{total_male_students:,} 명")
print(f"{total_female_students:,} 명")
print(f"{male_percentage:.2f} %")        
print(f"{female_percentage:.2f} %")       


bar = "2134"

if bar.isdigit():
    print("True")
else:
    print("False")
