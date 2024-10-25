numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
 # 문자열을 개별 숫자로 분리하고 각 숫자를 정수로 변환한후 , 모든 숫자의 합을 계산한다.

numbers = numbers_str.split(',')

sum = 0
list = []
over_100_flag = False

for i in numbers:
    num = int(i)
    sum += num
    list .append(num)
    
    if sum > 100:
        over_100_flag = True
        break
     
if over_100_flag:
    print("100초과",sum)    
    print(list)
else:
    print("100 이하",sum)    
    print(list)




