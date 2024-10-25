import csv

def get_filed_by_int(row, filed_name):
    return int(row[filed_name]) if row [filed_name].isdigit() else 0


file_path = r"Lab\7,11\2024_std_num_high_school.csv"

std_list = [0] * 6


with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        std_list[0] +=  get_filed_by_int(row, '1학년(남)')
        std_list[1] += get_filed_by_int(row, '1학년(남)')
        
        std_list[2] += get_filed_by_int(row, '2학년(남)')
        std_list[3] += get_filed_by_int(row, '2학년(남)')
        
        std_list[4] += get_filed_by_int(row, '3학년(남)')
        std_list[5] += get_filed_by_int(row, '3학년(남)')
        
print(f"전체 고등학생 수: {sum(std_list):,}")

sum_list = sum(std_list[0:2])
print(f"1학년 - 남학생 수: {std_list[0]:,}, 여학생 수: {std_list[1]:,},\
    남학생 비율: {std_list[0]/sum_list *100:.2f}%, 여힉생 비율: {std_list[1]/sum_list*100:.2f}%")

sum_list = sum(std_list[0:2])
print(f"2학년 - 남학생 수: {std_list[0]:,}, 여학생 수: {std_list[1]:,},\
    남학생 비율: {std_list[0]/sum_list *100:.2f}%, 여힉생 비율: {std_list[1]/sum_list*100:.2f}%")

sum_list = sum(std_list[0:2])
print(f"3학년 - 남학생 수: {std_list[0]:,}, 여학생 수: {std_list[1]:,},\
    남학생 비율: {std_list[0]/sum_list *100:.2f}%, 여힉생 비율: {std_list[1]/sum_list*100:.2f}%")
