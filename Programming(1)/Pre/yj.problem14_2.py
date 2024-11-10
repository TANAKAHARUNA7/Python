# 사용자로부터 여러 개의 숫자르르 문자열로 입력 받는다.
numbers_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
# 문자열을 개별 숫자로 분리하고 각 숫자를 정수로 변환한후 , 모든 숫자의 합을 계산한다.

numbers = numbers_str.split(',')

sum = 0
list = []
for i in numbers:
    num = int(numbers)
    sum += num
    list.append(i)
    if sum > 100:
        print("총합이 100을 초과하였습니다.")
        print("입력된 모든 숫자들: ",list)
        print("최종 총합: ",sum)
        break
    else:
        print("총합이 100을 초과하지 않았습니다.")
        print("현재까지의 입력값들: ",numbers)
        print("현재까지의 총합: ",sum)
        break
# 숫자의 총합이 100을 초과하면 해당 순간의 입력 값들과 총합을 출력하고 프로그램을 종료

# 숫자의 총합이 100을 초과하지 않은 경우 최종 총합과 입력된 숫자들을 출력
