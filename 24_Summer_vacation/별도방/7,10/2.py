# 파일의 작업 모드는 : Write / Read
# r+ : Read(파일 오픈 모드) + Write
# w+ : Write(파일 오픈 모드) + Read
# a+ : Append(파일 오픈 모드) + Read

# csv モデュールインポート
# このモデュールはCSVファイルを読んで書く機能を提供
import csv

# "grade.csv" ファイルを読んですべて
 

with open('grade.csv', 'r', newline='', encoding='utf-8') as f_handler:
    reader = csv.reader(f_handler)
    
    header = next(reader)
    header = next(reader)
    
    
    for row in reader:
        print(row)
        
    for row in reader:
        for item in row:
            print(item, "\t", end="")
        print()