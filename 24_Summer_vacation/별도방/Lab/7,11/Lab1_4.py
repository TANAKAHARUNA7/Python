import csv
from myutil import get_filed_by_int as get_field

file_path = r"Lab\7,11\2024_std_num_high_school.csv"

std_num = ()

with open(file_path, "r", encoding="utf-8-sig") as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        
        if row ["시도교육청"] not in std_num:
            std_num[row["시도교육청"]] = [0] * 6\
                
        std_num[row["시도교육청"]][0] += get_field(row, "1학년(남)")
        std_num[row["시도교육청"]][1] += get_field(row, "1학년(여)")
        std_num[row["시도교육청"]][2] += get_field(row, "2학년(남)")
        std_num[row["시도교육청"]][3] += get_field(row, "2학년(여)")
        std_num[row["시도교육청"]][4] += get_field(row, "3학년(남)")
        std_num[row["시도교육청"]][5] += get_field(row, "3학년(여)")
        
        
print(std_num)
                
