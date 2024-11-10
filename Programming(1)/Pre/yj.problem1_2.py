
# 사용자로부터 세 변의 길이를 입력받는다.
triangular1 = int(input("첫 번째 변의 길이를 입력하세요: "))
triangular2 = int(input("두 번째 변의 길이를 입력하세요: "))
triangular3 = int(input("세 번째 변의 길이를 입력하세요: "))


# 세 변의 길이가 삼각형을 형성할 수 있는 조건은 만족하는지 검사한다. 
# 삼각형을 형성할 수 있다면, 삼각형의 유형을 출력한다.
if triangular1 + triangular2 > triangular3 and triangular2 + triangular3 > triangular1 and triangular1 + triangular3 > triangular2:
    
    # 세 번의 길이가 모두 같다면, '정삼각형을 만들 수 있습니다.'라고 출력한다.
    if triangular1 == triangular2 == triangular3 :
        print("입력하신 변의 길이로는 정삼각형을 만들 수 있습니다.")
        
    # 세 변 중 두 변의 길이가 깉다면 , '이등변삼각형을 만들 수 있습니다.'라고 출력한다.
    elif triangular1 == triangular2 or triangular1 == triangular3 or triangular2 == triangular3:
        print("입력하신 변의 길이로는  이등변삼각형을 만들 수 있습니다.")
        
    # 세 변 중 두 변의 길이가 깉다면 , '부등변삼각형을을 만들 수 있습니다.'라고 출력한다.
    else :
        print("입력하신 변의 길이로는 부등변삼각형을 만들 수 있습니다.")

 # 형성할 수 없는 경우에는 왜만들 수 없는지 이유를 포함한 메시지를 출력한다.
else :
    print("입력하신 변의 길이로는 삼각형을 만들 수 없습니다. n삼각형을 만들기 위해서는 어떤 두 변의 길이의 합이 다른 한 변의 길이보다 커야 합니다.")