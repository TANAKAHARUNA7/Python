sum = 0
for i in range(1,6):
    while True:
        num = int(input(""))
        if num > 0 :
            sum += num
            break
        else:
          a = int(input("에러 다시입력\n"))
        break
print("평균","\t",sum/5)