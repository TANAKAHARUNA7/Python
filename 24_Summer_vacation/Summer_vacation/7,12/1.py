std_grades = {}  # Ditctionary

std_grades[240001] = ["홍길동", 10, 20, 30, 60, 30] 
std_grades[240002] = ["홍길삼", 100, 200, 300, 600, 300] 
std_grades[240003] = ["홍길사", 1000, 2000, 3000, 6000, 3000] 
std_grades[240003] = ["홍길오", {"국어": 100, "수학" : 20, "영어": 30}] 

print(std_grades[240003][-1])
print(sum(std_grades[240004][1].values()))

# # bar = { "name" : "ycjung", "age" : 20, "phone" : 123-456}

# # # keys()   : 키 값 
# # # values() : 데이터 값
# # # items()  : 키 + 데이터


# # print(bar.keys())  # dict_keys(['name', 'age', 'phone'])

# # for key in bar.keys():
# #     print(key)
#     # name
#     # age
#     # phone
    
    
# #############################################################
    
# bar = { "영어" : 20, "수학" : 30, "국어" : 40}

# # keys()   : 키 값 
# # values() : 데이터 값
# # items()  : 키 + 데이터


# # keys値とvalues値をセットでtupleタイプで出力
# print(bar.items())  #　dict_items([('영어', 20), ('수학', 30), ('국어', 40)])

# for key, value in bar.items():
#     print(key, "\t", value)  


# sum = 0

# for record in bar.values():
#     sum += record
# print(sum)


# for subject in bar.keys():
#     print(subject, "\t", end="")


###################################################################


# print(bar["name"])

# bar["email"] = "ycjung@yju.ac.kr"

# if "email" in bar:
#     print("True")
# else:
#     print("False")
    
# if "mobile" in bar.keys():
#     print("True")
# else:
#     print("False")


############################################################################

# bar = {
#     "ycj" : {"name" : "정영철", "age" : 20, "etc" : {"성적" : 100, "등급": "A"}},
#     "lny" : {"name" : "이나영", "age" : 30}
#         }

# print(bar["ycj"]) # {'name': '정영철', 'age': 20, 'etc': {'성적': 100, '등급': 'A'}}
# print(bar["ycj"]["etc"]["성적"])
# print(bar["ycj"]["etc"]["등급"])

##########################################################################

bar = {
    "ycj" : {"name" : "정영철", "age" : 20},
    "lny" : {"name" : "이나영", "age" : 30}
        }

for item in bar.values():
    for e in item.values():
        print(e)





