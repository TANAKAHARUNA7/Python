# while 문과break 문을 사용하여 1부터100 사이의 숫자를 맞추는 게임작성
# 정답 숫자는 랜덤 함수를 이용하여 1에서100사이 임의 정수 선택
import random

input_randomNum = random.randint(1,100)

msg = ""

# 사용자가 숫자를 맞출 때까지 반복하고, 맞추면 반복을 종료
while True:
    # 사용자로부터 입력을 받는다.
    input_num = int(input("1부터 100 사이의 숫자를 맞춰보세요: "))
    # 결과를 출력
    if input_randomNum == input_num:
        msg = "정답입니다!"
        break
    elif input_randomNum < input_num:
        msg = "더 작은 숫자입니다."
    else:
        msg = "더 큰은 숫자입니다."
    print(msg)
print(msg)
