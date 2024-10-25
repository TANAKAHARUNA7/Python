# # 다섯 개의 정수의 입력을 받고 합게와 평균을 출력한다.
number = []

for i in range(5):
    num = int(input(f"{i+1}번째 값 입력: "))
    number.append(num)

total_sum = sum(number)  
average = total_sum / len(number)

print("합계: ",total_sum)
print("평균: ",average)

# sum = 0

# for i in range(5):
#      num1 = int(input("1번째 값 입력"))
#      sum += num1
#      num2 = int(input("2번째 값 입력"))
#      sum += num2
#      num3 = int(input("3번째 값 입력"))
#      sum += num3
#      num4 = int(input("4번째 값 입력"))
#      sum += num4
#      num5 = int(input("5번째 값 입력"))
#      sum += num5   
#      print("합계: ",sum)
#      print("평균: ",sum/5)
#      break



