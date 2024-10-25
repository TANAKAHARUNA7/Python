# moji = ""
# for i in range(3):
#     num = i + 1
#     moji += (str(num))
#     print(moji)


# ioji = ""
# for i in range(3):
#     num = i + 1
#     ioji = (str(num)) + ioji
#     print(ioji)    

# list1 = []
# list2 = []

# for i in range(1,101):
#     if i % 2 == 0:
#         list1.append(i)
#     else:
#         list2.append(i)
        
# print("偶数:",list1)
# print("奇数:",list2)


# star = "*"
# stars = ""
# for i in range(5):
#     stars += star
#     print(stars)

student = ["sato","suzuki","tanaka","takahashi","ito"]
for i in student:
    print(i,end=" ") # 改行したくない場合は end=”” ,空白で区切りたい場合は end=” “, カンマで区切りたい場合は end=”,”

for V,i in enumerate(student): # enumerate() -> 元素の位置とその中身を表示
    print(V,i)

total = 0
for i in range(100):
    if  i % 2 == 0:
        continue
    print(i)
    total += i
    
print(total)