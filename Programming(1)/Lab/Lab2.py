rows = int(input("Enter the number of rows: "))

col = int(input("Enter the number of columns: "))

list = [[]* col for i in range(rows)]

for j in range(rows):
    for i in range(col):
        num = int(input(f"Enter value for [{j}][{i}]: "))
        list[j].append(num)
    print(list)
    
for row in list:
    for item in row:
        print(item , "\t", end="")
    print()