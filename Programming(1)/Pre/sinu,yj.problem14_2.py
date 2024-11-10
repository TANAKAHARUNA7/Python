# 사용자로부터 여러 개의 숫자를 문자열로 입력 받는다.
# 문자열을 개별 숫자로 분리하고 각 숫자를 정수로 변환한 후, 모든 숫자의 합을 계산한다.
# 숫자의 총합이 100을 초과하면해당 순간의 입력 값들과 총합을 출력하고 프로그램을 종료
# 숫자의 총합이 100을 초과하지 않은 경우 최종 총합과 입력된 숫자들을 출력

num_sum = 0
num_list = []
# 사용자로부터 숫자를 문자열로 입력 받기
while True:
    num_str = input("숫자들을 쉼표로 구분하여 입력하세요: ")
    
# 입력된 문자열을 쉼표 기준으로 숫자 리스트로 변환
    nums = num_str.split(',')

# 정수로 변환한 후 숫자의 합을 계산
    for num in nums:
        num_sum += int(num)
        num_list.append(int(num))

# 총합이 100을 초과하면 입력 값들이랑 총합 출력하고 종료
        if num_sum > 100:
            print("총합이 100을 초과했습니다.")
            print(f"현재까지의 입력값들: {num_list}")
            print(f"현재까지의 총합: {num_sum}")
            break
# 총합이 100이하면 최종 총합과 입력된 숫자들을 입력
    if num_sum <= 100:
        print("총합이 100을 초과하지 않았습니다.")
        print(f"입력된 모든 숫자들: {num_list}")
        print(f"최종 총합: {num_sum}")
    else:
        break