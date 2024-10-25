numbers_str = input("숫자들을 쉼표로 구분하여 입력: ")

numbers = numbers_str.split(',')

sum = 0
list = []
over_100 = False

for i in numbers:
    num = int(i)
    sum += num
    list.append(i)
    
    if sum > 100 :
        over_100 = True
        break

if over_100 :
    print("총합이 100을 초과하였습니다.")
    print("현재까지의 입력값들: ",list)
    print("현재까지의 총합: ",sum)