# bar = [[10, 20, 30], [40, 50], [60, 70, 80, 90]]

# rows = int(input("Enter the number of rows: "))
# col = int(input("Enter the number of columns: "))

# list = [[]]

# # 'bar' Matrixの全ての元素を巡回
# for row in range(rows):
#     for item in range(col):
#         print(f"Enter value for [{row}][{item}]: ", end="")
#         a = input()
#         print(item, end = " ")
#     print()


# ####################################################

rows = int(input("Enter the number of rows: "))
col = int(input("Enter the number of columns: "))

matrix = [[] for _ in range(rows)]

for i in range(rows): # 
    for j in range(col):
        print(f"Enter value for [{i}][{j}]: ", end="")
        a = input()
        matrix[i].append(a)
    
for row in matrix:
    for item in row:
        print(item, "\t",end=" ")
    print()
    

        
        
#######################################################
        