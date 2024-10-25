# while - if - break
# 키보드로부터 양의 정수를 입력 받아 입력 값을 출력하고 프로그램을 종료
# 입력 값이 음의 정수 또는 0일 경우 재입력

while True:
    input_value = int(input("양의 정수를 입력하세요: "))
    if input_value > 0: #조건이 잠이면        
        break
    print("양의 정수를 입력하세요: ")
    
    
    
# 1~100 사이 정수 중, 3의 배수와 7의 배수를 출력하세요
for i in range(1,101):
    if i % 3 == 0 or i % 7 == 0:
       print(i,"\t",end=" ") 


# 1~100 사이 정수 중, 3의 배수이면서 7의 배수를 출력하세요
# for i in range(1,101):
#     if i % 3 == 0 and i % 7 == 0:
#       print(i,"\t",end="")



