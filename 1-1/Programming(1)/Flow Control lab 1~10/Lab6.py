# for 문과 continue 문을 사용하여 1~20까지의 숫자 중 짝수의 계를 계산한다.
sum = 0

for num in range(1, 21):
    if num % 2 != 0:
        continue
    else:
        sum += num 
print("1부터 20까지의 짝수 합계 (홀수 건너뜀): ", sum)
