#  For 문을 사용하여 아래 문자열 내 ‘h’의 개수를 출력하는 프로그램
myString = "hello hyundai hoho"

# "h"의 개수를 count 한다
h_check_count = 0
 
for h in myString:
    if h == "h":
        h_check_count += 1
        
print("문자열 내 h 갯수 : ", h_check_count)