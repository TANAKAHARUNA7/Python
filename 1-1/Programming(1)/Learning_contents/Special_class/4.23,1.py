# # 　정수 3개를 입력받아서 제일 큰 값을 출력하기
# num1 = int(input("첫 번째  정수를 입력하세요"))
# num2 = int(input("두 번째 정수를 입력하세요"))
# num3 = int(input("세 번째 정수를 입력하세요"))

# max_num = num1

# if max_num < num2:
#     max_num = num2
# elif max_num < num3:
#     max_num = num3
# print(max_num)


max_num = -1
for i in range(1,4):
    msg = str(i) + "번"
    input_value = int(input(msg))
  
    if max_num < input_value:
        max_num = input_value

print(max_num)
   
    
    