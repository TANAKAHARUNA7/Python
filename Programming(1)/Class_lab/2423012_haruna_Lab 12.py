# 사용자로부터 소득 금액을 입력받아 소득세를 계산합니다. 
input_income = float(input("소득 금액을 입력하세요: "))


def calculate_tax(income):
    

#첫 1만 달러의 소득(income)에는 10%의 세율이 적용됩니다.
    if income <= 10000:
        tax = income * 0.1 
    

# 1만 이상 2만 이하는 15%의 세율을 적용하고, 첫 1만 달러의 세금인 1천 달러를 더합니다.

    elif 10000 < income <= 20000 :
         tax =( income - 10000 )* 0.15  + 1000  

# 2만 이상는 20%의 세율을 적용하고,앞선 구간의세금인 2천 5백 달러를 더합니다'''
     
    else:
        tax = (income - 20000) * 0.2 + 2500
    
    return tax
tax = calculate_tax(input_income) 
print("소득세는 ", tax , "달러 입니다.")
