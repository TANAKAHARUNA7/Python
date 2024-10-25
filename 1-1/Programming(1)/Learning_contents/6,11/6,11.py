# def 함수이름(매개 변수):
#      함수 호출 시 실행 고드

# 함수 호출 시 입력 값을 전달 할 수 있다 
# -> 1) Argument (인자 값)
# -> 2) Parameter (매개변수)

# def get_sum(arg_a, arg_b, arg_c): 
    
#     sum = arg_a + arg_b + arg_c
    
#     return sum
    
# print(get_sum(1,2,3))
# print(get_sum(4,5,6))

# print("------------")

# print(get_sum(7,8,9))


bar = [2, 3, 5]

def foo(arg_list): # 매모리 주소 값을 복사
    copied_list = arg_list[:]
    # print(copied_list)
    
    copied_list[0] = 100
 
    
foo(bar)

print(bar) # 2, 100, 5


