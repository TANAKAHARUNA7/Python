#入力された年齢に応じて「青少年（Teenager）」、「大人（Adult）」、「老年（Senior）」に分類
age = int(input("年齢を入力してください"))
 
# 13歳から19歳の間は "Teenager" 
if 13 <= age <= 19:
    print("Teenager")
# 20歳から64歳の間は "Adult"
elif 20 <= age <= 64:
    print("Adult") 
# 65歳以上は "Senior"
elif  65 <= age :
    print("Senior")
# 範囲に合わない入力値については「Unknown age group」
else:
    print("Unknown age group")

