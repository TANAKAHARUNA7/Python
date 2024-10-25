import csv

file_path = r"Lab\7,11\2024_std_num_high_school.csv"

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    male_students_1 = 0
    female_students_1 = 0
    
    male_students_2 = 0
    female_students_2 = 0
    
    male_students_3 = 0
    female_students_3 = 0
    
    for row in csv_reader:
        
        male_students_1 += int( row['1학년(남)'] if row['1학년(남)'].isdigit() else 0)
        female_students_1 += int( row['1학년(여)'] if row['1학년(여)'].isdigit() else 0)
        
        male_students_2 += int( row['2학년(남)'] if row['2학년(남)'].isdigit() else 0)
        female_students_2 += int( row['2학년(여)'] if row['2학년(여)'].isdigit() else 0)
        
        male_students_3 += int( row['3학년(남)'] if row['3학년(남)'].isdigit() else 0)
        female_students_3 += int( row['3학년(여)'] if row['3학년(여)'].isdigit() else 0)
        
        total_student = male_students_1 + male_students_2 + male_students_3 + female_students_1 + female_students_2 + female_students_3
        
        male_1_percentage = male_students_1 / (male_students_1 + female_students_1) * 100
        female_1_percentage = female_students_1 / (male_students_1 + female_students_1) * 100 
        
        male_2_percentage = male_students_2 / (male_students_2 + female_students_2) * 100
        female_2_percentage = female_students_2 / (male_students_2 + female_students_2) * 100
        
        male_3_percentage = male_students_3 / (male_students_3 + female_students_2) * 100
        female_3_percentage = female_students_3 / (male_students_3 + female_students_2) * 100
        
        

print(f"전체 고등학생 수: {total_student:,}")
print(f"1학년 - 남학생 수: {male_students_1:,}, 여학생 수: {female_students_1:,}, 남학생 비율: {male_1_percentage:.2f}%, 여힉생 비율: {female_1_percentage:.2f}%")
print(f"2학년 - 남학생 수: {male_students_2:,}, 여학생 수: {female_students_2:,}, 남학생 비율: {male_2_percentage:.2f}%, 여힉생 비율: {female_2_percentage:.2f}%")
print(f"3학년 - 남학생 수: {male_students_3:,}, 여학생 수: {female_students_3:,}, 남학생 비율: {male_3_percentage:.2f}%, 여힉생 비율: {female_3_percentage:.2f}%")
