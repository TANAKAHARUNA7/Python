
def get_check_digit(arg_ssid):
    weight = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
    weight = [(value % 8) + 2 for value in range(12)]
    
    ssid = [int(value) for value in arg_ssid]
    
    sum_value = sum([ssid[index] * weight[index] for index in range(12)])
    
    return (11 - sum_value % 11) % 10

# 유호한 주민번호 -> True else False

def is_valid_ssid(arg_ssid):
    
    arg_ssid = arg_ssid.replace("-","")

    if len(arg_ssid) != 13:
        return False
    
    # 
    check_digit = 0
    
    if check_digit == arg_ssid[-1]:
        return True
    else:
        return False
    
is_valid_ssid("650212-2871727")



# input_num = [input("입력")]
# # input_num = [7,9,0,6,0,8,"-",2,5,5,2,4,1,6]
# input_num.remove("-")
# print(input_num)

# # 주민번호의 앞 12자리를 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5로 곱하고 그 결과를 모두 더한다
# list = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]

# sum = 0
# for index in range(12):
#     sum += input_num[index] * list[index]
# print(sum)

# # 더한 결과를 11로 나눈 나머지를 구합니다.
# div = sum % 11
 
# # 11에서 이 나머지를 뺍니다.
# minus = 11 - div

# # 결과가 두 자리 숫자일 경우, 10의 자리는 버리고 1의 자리만 사용합니다.
# if minus >= 10:
#     result = minus % 10 
# else:
#     result = minus
# # 최종 결과가 주민번호의 마지막 숫자(검증번호)와 일치하면 유효한 주민번호입니다
# if input_num[-1] == result:
#     print("유효한 주민번호")
# else:
#     print("유효하지않은 주민번호")