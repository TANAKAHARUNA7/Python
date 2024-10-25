import math

a_value = int(input("aの値を入力"))
b_value = int(input("bの値を入力"))
c_value = int(input("cの値を入力"))

answer_num = b_value**2 -4 * a_value*c_value

def x_mathematical_formula(a, b, c):
    formula1 = -b + (math.sqrt(answer_num)) / 2 * a
    formula2 = -b - (math.sqrt(answer_num)) / 2 * a
    return formula1, formula2

X1, X2 = x_mathematical_formula(a_value, b_value, c_value)

if answer_num > 0:
    print("서로 다른 두 실근을 가진다.")
elif answer_num == 0:
    print("한 개의 실근을 가진다")
else :
    print("서로 다른 두 허근을 가진다")
