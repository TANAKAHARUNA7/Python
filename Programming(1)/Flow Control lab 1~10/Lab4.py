 # For 문을 사용하여 아래 문자열 내 단어 개수를 출력하는 프로그램
myString = "It is a great weather with you"

 # space를 제거한다.
s_n_space = myString.split()

word_count = 0 
 
for i in s_n_space:
     word_count += 1
    
print("문자열 단어 갯수 : ", word_count)
