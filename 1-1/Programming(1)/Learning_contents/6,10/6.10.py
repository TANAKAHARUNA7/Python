# import random

# random.randint(1,3)

# # 함수를 정의한다
# # 정의된 함수를 호출한다
# # 정수 3개를 입력받아 합계와 평균을 출력
# # def get_sum():
# #     input_value_1 = int(input("입력 값"))
# #     input_value_2 = int(input("입력 값"))
# #     input_value_3 = int(input("입력 값"))
    
# #     sum = input_value_1 + input_value_2 + input_value_3 
    
# #     print(sum)    


# # 함수 사용의 순서
# # 1) 함수를 정의한다
# # 2) 정의된 함수를 호출한다.


# # 정수 3개를 입력 받아 합계와 평균을 출력하는 프로그램을 작성하라.

# def get_int(arg_num):
#     input_values = []
#     for _ in range(arg_num):
#         input_values.append(int(input("입력값: ")))
        
#     return input_values

# def get_sum_avg(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     avg = sum / len(arg_list)
    
#     return sum, avg

# def get_sum(arg_list):
#     sum = 0
#     for value in arg_list:
#         sum += value
    
#     return sum
 

# input_list = get_int(13)

# sum, avg = get_sum_avg(input_list)

# print(sum, avg)


# def get_sum(num):
#     sum = 0
#     for i in range(num):
#         input_value = int(input("입력 값"))
#         sum += input_value 
#     print(sum)   

# get_sum(3) 




# def 함수명(매개변수):
# 함수 호출 시 실행 명령어

# 함수 정의 : -> 1번
# def print_name(name): # 'name' : Prumetor -> 매개변수
#     print(name,"님 안녕하세요")

# # 함수 호출 : -> 2번
# print_name("리자드") # '리자드' : Argument -> 인자값
# print_name("정영절")



# 함수 사용의 순서
# 1) 함수를 정의 한다
# 2) 정의된 함수를 호출한다

# def sum(arg_first , arg_second): 
#     sum = arg_first + arg_second 
    
#     if sum < 0: 
#         print("음수") # return의 두가지 role  # 1) 함수 종료 
#         return  # None -> 반환하는 값이 없으니까 'None'라고 출력 된다. 

#     return sum  # 2) 값 반환 , 호출된 것에 전달하는 약할
# # 함수 정의 시 return 있어도 되고 없어도 된다. 즉 Option 이다.

# result = sum(2, 3) 
# print(result)

# result = sum(-2, -3)
# print(result) 


# 함수 사용의 순서
# 1) 함수를 정의한다.
# 2) 정의된 함수를 호출한다.

# 한 개의 정수를 키보드로부터 입력을 받아 "짝수", "홀수"를 판별하여 화면에 출력
# 함수로 저장

# def num():
#     msg = "짝수" if input_num % 2 == 0 else "홀수"
    
#     return msg

# input_num = int(input("입력"))    
# print(num())


# 한수에 인자 값 4개를 입력 받아 함계와 편균을 반환하는 함수를 작성
# 그리고 반환된 함계와 편균을 출력

def input_num(num1,num2,num3,num4):
    sum = num1 + num2 + num3 + num4
    avg = sum / 4
    return sum , avg  # -> (sum, avg)
# 반환값이 두 개 이상이면 -> 자동으로 tuple로 변화 후 반환한다.

sum, avg = input_num(1,2,3,4)
print(sum, avg)  # 10 2.5

value = input_num(3,4,5,6)
print(value[0], value[1])  # 18 4.5
print(type(value))  # <class 'tuple'>




