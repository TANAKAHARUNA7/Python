msg = """pos foo foo pos test pos
foo kin pos kin
dk test pos"""

find_word = "pos"
find_word_index = 0
find_word_len = len(find_word)
count_found_word = 0
find_word_pos = []


count = 0
count_lines = 1
count_char = 0
count_word = 0
prev = ""


for cur in msg:

    if find_word[find_word_index] == cur :
        find_word_index += 1
        if find_word_index == find_word_len: # 글자를 찾았다!!!!
            count_found_word += 1
            find_word_index = 0
            find_word_pos.append(count - find_word_len + 1)
            
    else:
        find_word_index = 0
    
    if cur == " " or cur == "\n":
        if prev != " " and prev != "\n":
            count_word += 1
    elif count == len(msg) - 1:
        if prev != " " and prev != "\n":
            count_word += 1        
             
    if cur != " " and cur != "\n":
        count_char += 1
        
    if cur == "\n":
        count_lines += 1

    count += 1
    
    prev = cur # 현재 글자를 이전 글자로 업데이트

    
   
print(f"총 글자수: {count_char}")        
print(f"총 줄수: {count_lines}") 
print(f"총 단어수: {count_word}")   
print(f"검색된 단어수: {count_found_word}")     
print(f"검색된 단어 위치: {find_word_pos}")  



############################################################
# 미리 입력된 문장
# sentence = """pos pos hello  bar
# foo bar foo pos kin pos
# test test pos"""

# # space,line 모둔 것을 list화
# list_sentence = []
# list_sentence += sentence
# print(list_sentence)

# # 단어 한 개씩 list화
# list_word = sentence.split()
# print(list_word)

# # line개수를 출력
# line = 0
# for i in list_sentence:
#     if i == "\n":
#         line += 1

# # value = input("문자를 입력하세요: ")

# # list_value = []
# # list_value += value
# # print(list_value)


# # n_location = 0
# # list_location = []
# # for y in list_sentence:
# #     if list_value[0] == y:
# #         list_location.append(n_location)
# #     n_location += 1
# # print(list_location)        

# # 문자열의 개행을 제외
# del_line = sentence.replace("\n","")

# # 문자열의 공백을 제외
# del_space = del_line.replace(" ", "")

# # 전체 문자 수
# sentence_length = len(del_line)

# # length_list_num = [value for value in range(len(length_list))]
# # print(length_list_num)

# # 모둔 단어의 개수를 count
# all_word_count = 0
# for value in range(len(list_word)): 
#     all_word_count += 1

# # 입력된 문자열이 있을 경우 검색 결과를 출력한 후 프로그램을 종료
# while True:
    
#     choice_word_count = 0
#     input_word = input("문자를 입력하세요: ")
#     if input_word in list_word:
    
#         list_value = []
#         list_value += input_word

#         # a. 검색된 문자열의 개수    
#         for word in list_word:
#             if input_word == word:
#                 choice_word_count += 1
        
#         n_location = 0
#         list_location = []
#         for y in sentence:
#             if y == " " and y == "\n":
#                 continue
            
#             list_location.append(n_location)
#             n_location += 1
#         break
#     #검색된 결과가 없을 경우 검색 문자를 재입력 받는다
#     else:
#         print("해당 문자열이 없읍니다. 다시 입력하세요.")
        
# print(f"검색된 문자열의 개수: {choice_word_count}")    
# print(f"검색된 문자열의 위치 {list_location}")    
# print(f"단어의 개수: {all_word_count}")    
# print(f"전체 문자 수: {sentence_length}")  
# print(f"줄 수: {line + 1}")  
    
# #     # 선텍된 단어의 개수를 count
# #     choice_word_count = 0

# #     # 검색 문자열을 입력 받는다.
# #     input_word = input("검색할 문자열을 입력하세요: ")
    
# #     input_word_list = list(input_word)
# #     print(input_word_list)
    
# #     # < 입력 받은 문자열이 문장 내 있을 경우 >
# #     # 1.검색된 문자열에 대한 정보를 출력
# #     # a. 검색된 문자열의 개수    
# #     for word in list_word:
# #         if input_word == word:
# #             choice_word_count += 1
# #     print(f"검색된 문자열의 개수: {choice_word_count}")
    
# #     # b. 검색된 문자열의 위치(들)
# #     n_location = 0
# #     list_location = []
# #     list_value = 0
# #     for i in input_word_list:
# #         for y in list_sentence:
# #             list_value += 1
# #             if y == i:
# #                 list_location.append(list_value)
                
# #     print(list_location)               
            
            
            


    
           
            




# # 위치는 문자열이 시작되는 인덱스를 기준으로 하며, 문장의 첫 번째 글자는 인덱스 0으로 한다
# # 2.전체 문장에 대한 정보를 출력
# # a. 단어의 개수 (단어는 띄어쓰기로 구분)
# # b. 전체 문자 수(공백과 개행 문자를 제외한 글자 수)
# # c. 줄 수 (The number of lines)

# # < 입력 받은 문자열이 문장 내 없을 경우 >
# # 해당 문자열이 없음을 화면에 출력하고, 검색할 문자열을 재입력 받는다
# # 검색된 문자열이 있을 때 까지 반복한다