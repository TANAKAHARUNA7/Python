import csv

with open("output.csv", mode = "w", newline='', encoding="utf-8") as f_handler:
    writer = csv.writer(f_handler)
    
    writer.writerow(['Name', 'Age', 'Email'])
    
    writer.writerows([['Alice', 30, 'alice@example.com', ['Bob', 25, 'bob@example.com']]])


    
    
    
    
    
    