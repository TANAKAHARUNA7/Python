# bar = "hello world" # スペースも文字に含まれる

# print(len(bar)) # len() ⇒　文字の数を数える
# print(bar[0], bar[1], bar[2], bar[3], bar[-1], bar[-2], bar[-3]) # -1 ⇒ 後ろから数える
# print(len(bar), bar[len(bar)-1])

num = "234567-9738393"

check = [1,2,3,4,5,6,7,8,9,2,3,4,5]
sum = 0
count = 0 

for i in num:
    if i != "-" and count < 12: # if の条件を満たさなかったらforに戻る
       sum += int(i) * check[count]   
       count += 1 # check = [] の元素を順番に表示していく
       
check_value = (11 - (sum % 11)) % 10 
 
if check_value == int(num[-1]):
    print("有効な番号")      
else:
    print("有効でない番号") # numのリストを1つずつ表示する
    
    
Value = 79

if Value >= 90:
    print("A")
elif Value >= 80:
    print("B")    
elif Value >= 70:
    print("C")    
elif Value >= 60:
    print("D")    
else:
    print("E") 
    
    