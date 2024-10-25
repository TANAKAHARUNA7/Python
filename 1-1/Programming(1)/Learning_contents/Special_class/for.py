# 양의 정수 5개를 입력 받아 합과 평균을 출력하라
sum = 0
for i in range(1,6):
     num = int(input(f"{i}번째 값 입력"))
     if num >= 0 :
         sum += num
     else:
       a = int(input("에러 다시입력"))
print("합계",sum,"평균",float(sum/5))


# input_num = 5
# sum = 0
# avg = 0.0

# for trial_count in range(1, input_num+1):
#     while True:        
#         msg = str(trial_count) + "번째 입력"
#         input_value = int(input(msg))
    
#         sum = sum + input_value
#         avg = sum / input_num

# print(sum,avg)


# 다음과 같이  출력하는 프로그램을 작성
# 1,3,5,7,9,11,13,15,17,19
# 조건 for 문 사용
# for i in range(1,20):
#     if i % 2 != 0:
#         print(i,end=" ")
