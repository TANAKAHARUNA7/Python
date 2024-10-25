# 두 개의 실수를 입력받고 원하는 연산,자료형을 선택받고 출력하기 
# 첫 번째 수를 받는다.
num1 = float(input("첫 번째 수를 입력하세요: "))
# 두 번째 수를 받는다. 
num2 = float(input("두 번째 수를 입력하세요: "))

# 연산자를 선택받는다.(+,-,*,/ 중 하나 입력)
calculation = input("연산자를 입력하세요(+,-,*,/ 중 하나): ")

# 결과 값 자료형(integer,float,string 중 하나 입력)
document = input("결과 값 자료형을 입력하세요(integer,float,string 중 하나): ")

# 결과 값 자료형 integer를 선택한 경우
if  calculation == "+" and document == "integer":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"+",num2 ,"=",int(num1 + num2))
elif  calculation == "-" and document == "integer":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"-",num2 ,"=",int(num1 - num2))
elif  calculation == "*" and document == "integer":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"*",num2 ,"=",int(num1 * num2))
elif  calculation == "/" and document == "integer":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"/",num2 ,"=",int(num1 / num2))
    
# 결과 값 자료형 float를 선택한 경우    
if  calculation == "+" and document == "float":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"+",num2 ,"=",float(num1 + num2))   
elif calculation == "-" and document == "float":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"-",num2 ,"=",float(num1 - num2))
elif calculation == "*" and document == "float":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"*",num2 ,"=",float(num1 * num2))    
elif calculation == "/" and document == "float":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"/",num2 ,"=",float(num1 / num2)) 
    
# 결과 값 자료형 string를 선택한 경우       
if  calculation == "+" and document == "string":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"+",num2 ,"=",str(num1 + num2))   
elif calculation == "-" and document == "string":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"-",num2 ,"=",str(num1 - num2))
elif calculation == "*" and document == "string":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"*",num2 ,"=",str(num1 * num2))    
elif calculation == "/" and document == "string":
    print("결과 값은 아래와 같습니다.")
    print(num1 ,"/",num2 ,"=",str(num1 / num2))      
    
    
    
    