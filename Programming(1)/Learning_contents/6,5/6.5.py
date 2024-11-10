#  リストコンポレーション　ー＞　リスト内の元素を動的に生成する方法
# 数式　for 選択項目in 選択リスト　if　条件

# 반복이 정상적

done_break = False
for value in range(3): # N -> 
    
    input_value = int(input(""))
    
    if input_value <= 0:
        done_break = True
        break
    
    print(value)

msg = 'break 사용' if done_break else 'break 미사용'

print(msg)

# ------------------------------------------------

for value in range(3): # N -> 
    
    input_value = int(input(""))
    
    if input_value <= 0:
        msg = 'break 사용'
        break
    
    print(value)
else:  # 반복문 종료 and break 미사용
    msg = 'break 미사용'

print(msg)


