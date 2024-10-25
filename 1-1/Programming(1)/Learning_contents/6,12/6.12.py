
# # # agument

# # # 1) positional(位置) argument　→　位置を合わせて

# # def foo(arg_a, arg_b, arg_c):
# #     print(arg_a, arg_b, arg_c)
        
# # foo(1,2,3)  # 指定した位置の媒介変数のところへ行く


# # # 2) keyword argument　→　媒介変数の名前を利用
# # def pos(arg_a, arg_b, arg_c):
# #     print(arg_a, arg_b, arg_c)

# # pos(arg_c= 1, arg_a= 2, arg_b= 3) # 媒介変数の名前を利用するため順序は関係ない
    
    
# # 3) defult argument
# # a) 全てのパラメーターに初期値を設定する
# # b) 初期値を持つパラメーターは一番後ろに位置しなければならない

# def kin(arg_a = 1, arg_b= 2, arg_c = 3,arg_d = 4): # 初期値 
#     print(arg_a, arg_b, arg_c, arg_d)    

# # 引数値を入力すると初期値を無視し引数値を代入する   
# kin() # 1, 2, 3, 4    
# kin(6, 7, 8, 9) # 6, 7, 8, 9  
# kin(6) # 6, 2, 3, 4
# kin(6, 7) # 6, 7, 3, 4
# kin(6, 7, arg_d = 10) # 6, 7, 3, 10


# 구구단을 출력 2~9
# 함수로 작성 : printMulTable()


# for i in range(2,10):
#     for j in range(1,10):
#         print(f"{i} X {j} = {i * j}")


# 1) printMulTable(2, 3)-> 2단과 3단을 출력
# 2) printMulTable(3)
                             # default parameter
def printMulTable(arg_start, arg_end = None):
    
    # 인자 값이 한 개가 입력 되었을 경우
    # arg_star 값만 출력한다.

    if arg_end == None:
        arg_end = arg_start
        
    for i in range(arg_start,arg_end + 2):
        if arg_start <= i <= arg_end:
            for j in range(1,10):
                print(f"{i} X {j} = {i * j}")
                
printMulTable(2,5)
printMulTable(3)





    