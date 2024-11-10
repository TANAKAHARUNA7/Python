# 사용사로부터 토지의 면직을 제곱미터(㎡)단위로 입력받는다.
square_meters = float(input("토지의 면직을 제곱미터(㎡)단위로 입력하세요: "))

def convert_to_square_feet(square_meters):
    # 1제곱미터(㎡) = 10.7639 ft^2
    ft = 10.7639 * square_meters 
    return ft
def convert_to_acres(square_meters):
    at = square_meters / 4046.86  
    return at  

# 변환된 면적을 평방피트와 에이커 단위로 출력 
convert_to_square_feet(square_meters)
convert_to_acres(square_meters)
  
if square_meters < 0:
    print("잘못된 입력입니다.") 
else:
    print(square_meters,"제곱미터는",convert_to_square_feet(square_meters),"평방피트입니다.")
    print(square_meters,"제곱미터는",convert_to_acres(square_meters),"에이커입니다.")