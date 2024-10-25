# args　値は1個または2個
#　args　値が1個なら、args X args マトリックスを生成して返還
#　args 値が２個なら、args[0] X args[1] マトリックスを生成して返還
# 初期の値は１～100の間のランダム値に設定（重複値）

import random

def get_matrix(*args):
    
    if not(1 <= len(args) <= 2):
        return None
    
    matrix_row = args[0]
    
    if len(args) == 1:
        matrix_col = args[0]
    else:
        matrix_col = args[1]
    
    data_frame = {
        "num_row" : matrix_row,
        "num_col" : matrix_col,
        "data" : [ [random.randint(1,100) for _ in range(matrix_col)]\
         for i in range(matrix_row)]}
    
    data_frame["sum"] = sum([sum(row) for row in data_frame["data"]])
    
    
    return data_frame
    # bar = [[random.randint(1,100) for _ in range(matrix_col)]\
    #      for i in range(matrix_row)]
    
    # return bar
    
foo = get_matrix(3,2)
print(foo["num_row"], "\t", foo["num_col"])
print(foo["data"])
print(foo["sum"()])
print(get_matrix(3))
print(get_matrix(3,2))
