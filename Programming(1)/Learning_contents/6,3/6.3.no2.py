# while

# while 조건식:
#     참 일때 실행되는 문장

# 키보도로부터 정수를 입력 받고, 양수일 경우 출력
# 음수 또는 0인 경우 재입력 -> 양수 입력 될때까지

# while True:
#     num = int(input("입력"))
    
#     if num > 0:
#         print(num)
#         break
       
# while 문을 이용해서 1에서 10까지 출력하는 프로그램을 작성
# count = 1
# while count <= 10:
#     print(count)
#     count += 1
    
bar = ["hello", "world", "Richard"]
# found_word = False # Flag 변수 -> 깃발 : Boolean

for word in bar:
    
    if word == "world":    
        print("단어를 찾았음")
        # found_word = True
        break
else:
    print("단어를 찾지 못했음. 나~~빠~~또~~" )
    
# if not found_word:    
#     print("단어를 찾지 못했음. 나~~빠~~또~~" )
    
    
    
    
    