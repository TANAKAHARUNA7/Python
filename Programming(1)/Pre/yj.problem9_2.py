text = list(input("文字列を入力してください: "))

text = text.replace("-","")
# text.remove("-")
 
if len(text) != 12:
    print("12桁の住民番号を入力してください")
 
check_number = [2,3,4,5,6,7,8,9,2,3,4,5]

num = 0

for i in range(12):
    num += int(text[i]) * check_number[i]
    
if ( 11 - ( num % 11 )) % 10 == int(text[-1]):
    print("有効な住民番号です")    
else:
    print("有効でない住民番号です")  

