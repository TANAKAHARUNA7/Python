# 현재 연도와 사용자의 태어난 연도를 입력받아 나이 계산한다.
# 현재 연도를 입력받는다.
Current_year = int(input("현재 연도를 입력하세요: "))

# 사용자의 태어난 연도를 입력받는다.
Birth_year = int(input("태어난 연도를 입력하세요: "))

# 현재 연도에서 태어난 연도를 뺀다.
age = Current_year - Birth_year 

# 나이를 출력한다.
print("당신의 나이는", age , "살 입니다.")
