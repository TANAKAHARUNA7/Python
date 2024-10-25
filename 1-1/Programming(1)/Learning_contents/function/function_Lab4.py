
def max_of_three(num1,num2,num3):
    maxNum = num1
    if num1 < num2:
        maxNum = num2
    else:
        maxNum = num3
    return maxNum

print(max_of_three(10,20,15))