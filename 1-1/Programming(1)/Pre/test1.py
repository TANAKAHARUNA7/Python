# 두 개의 실수를 입력받고 사용자가 원하는 연산자,자료형에 맞고 결과를 출력하기
# 첫 번째 값을 입력받는다.
num1 = (input("첫 번째 값을 입력 하세요:\n"))

# 두 번째 값을 입력받는다.
num2 = (input("두 번째 값을 입력 하세요:\n")) 

# 연산자를 입력받는다.(+,-,*,/ 중 하나 입력)
calculation = input("연산자를 입력하세요(+,-,*,/ 중 하나):\n")

value = 0

if calculation == "+":
    value = float(num1) + float(num2)
elif calculation == "-":
    value = float(num1) - float(num2) 
elif calculation == "*":
    value = float(num1) * float(num2)
elif calculation == "/":
    value = float(num1) / float(num2)
    
# 결과 값 자료형을 입력받는다. (integer,float,string, 중 하나 입력)
document = input("결과 값 자료형을 입력하세요(integer,float,string 중 하나):\n")

# 결과 값을 출력   
if document == "integer":
    print(f"결과 값은 아래와 같습니다.\n{num1} {calculation} {num2} = {int(value)}" )   
elif document == "float":
    print(f"결과 값은 아래와 같습니다.\n{num1} {calculation} {num2} = {value}" ) 
else:
    print(f"결과 값은 아래와 같습니다.\n{num1} {calculation} {num2} = {str(value)}" )


    