# 10 ~ 20 정수 중 짝수의 합을 계산한다.

sum = 0
for i in range(10,21):
    if i % 2 == 0:
        sum = sum + i 
print(sum)
    
# for value in range(10,21,2):
#     sum += value
# print(sum)


# 구구단 2~9

for i in range(2,10): # 세로 
    if i == 5 or i == 7:
        continue 
    
    for j in range(1,10): # 가로
        print(f"{i} X {j} = {i * j}")
    print("----------")