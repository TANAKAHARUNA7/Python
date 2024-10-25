def print_matrix(arg_list):
    for row in arg_list:
        for col in row:
            print(col,"\t",end="")
        print()
    print("-" * 17)

def del_col(arg_list,col_num):
    for index in range(len(arg_list)):
        del arg_list[index][col_num]


# def pulas_col(arg_list,pulas):
#     for index in range(len(arg_list)):
#         arg_list[pulas][2].append(100)


matrix = [[1, 2, 3],[4, 5],[6, 7]]

print_matrix(matrix)
del_col(matrix,1)
# pulas_col(matrix,2)
# del matrix[0][1]
matrix[2].append(100) # 2番目のリストに100を追加
matrix.append([8, 9, 10, 11]) # 最後の行にリストを新しく追加
matrix.insert(2,[1,2,3,4]) # 指定の位置にリストを新しく挿入

print_matrix(matrix)
