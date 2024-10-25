# 사용자로부터 섭씨 온도를 입력받아 화씨 온도로 변환하는 함수를작성하고, 변환된 화씨 온도를 출력하는 프로그램을 작성하세요.
# 사용자에게 섭씨 온도를 입력받는다.
input_celsius = int(input("섭씨 온도를 입력하세요: "))

# 섭씨를 화씨로 변환하는 함수를 작성한다.
# 회씨 온도는 섭씨 온도에 9/5를 곱한 후 32를 더해 계산한다.
def convert_celsius_to_fahrenheit(celsius):
    Fahrenheit = (celsius * 9 / 5 ) + 32
    return Fahrenheit


# 변환된 화씨 온도를 출력한다.
Fahrenheit = convert_celsius_to_fahrenheit(input_celsius)

print("화씨 온도는 ", Fahrenheit,"입니다.")





