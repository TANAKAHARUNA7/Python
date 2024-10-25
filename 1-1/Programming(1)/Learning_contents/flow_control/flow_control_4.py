# 영문 문자의 입력을 받는다.
input_str = input("회사명을 입력하세요")

# 규칙을 따라 한글로 변환한다.
msg = ""

if input_str == "SAMSUNG": 
    msg = "삼성"
    
elif input_str == "LG":
    msg = "엘쥐"
    
elif input_str == "KAKAO":
    msg = "카카오"    
    
elif input_str == "NAVER":
    msg = "네이버" 
    
elif input_str == "HYUNDAI":
    msg = "현대"    

elif input_str == "SK":
    msg = "에스케이"

# 규칙 이외의 영문 이름이 입력될 경우 “그외” 문자열 출력
else:
    msg = "그 외"

print(msg)    
    
    