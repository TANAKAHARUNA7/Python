#  While문을 사용하여 1~1000까지의 정수중 3의 배수의 총합을 구한다
num_count = 1
sum = 0

while 1 <= num_count <= 1000:
    if num_count % 3 == 0: 
        sum += num_count
    num_count += 1
print(sum)