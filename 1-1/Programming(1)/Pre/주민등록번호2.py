# 주민번호 입력을 받는다. 
# 유호하지 않은 번호 = 040425-2454578 , # 유호한 번호 = 790608-2552416

input_num = list(input("주민번호 입력"))
# input_num = "0404252-454578"
# input_num = "790608-2552416"
# input_num_list = list(input_num)
# input_num = list(0,4,0,4,2,5,2,4,5,4,5,7,8)

# 変数宣言 = 変数.replace("","")　‐≫　tuple型に対応。
# del_input_num = input_num_list.replace("-","") 
# input_num_list.remove("-")

# リスト型に対応
input_num.remove("-") 

# 주민번호의 앞 12자리를 각각 2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5로 곱합니다.
num = [2, 3, 4, 5, 6, 7, 8, 9, 2, 3, 4, 5]
sum = 0
for i in range(12):
    # 이 결과를 모두 더합니다.
    sum += int(input_num[i]) * num[i]

# 더한 결과를 11로 나눈 나머지를 구합니다.
div = sum % 11

# 11에서 이 나머지를 뺍니다
muinus = 11 - div

# 결과가 두 자리 숫자일 경우, 10의 자리는 버리고 1의 자리만 사용합니다
if muinus >= 10:
    result = muinus % 10 
else:
    result = muinus
    
if result == int(input_num[-1]):
    print("ok")
else:
    print("no")



