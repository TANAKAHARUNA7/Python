# ㅂ
#

msg = "hello"

for char in msg :
    print(msg)
    

for char in (msg := "hello"):
    print(msg)


# is , is not -> Identity operator

bar = [2, 4, 5]
foo = [2, 4, 5]

if bar is foo:
    print("참")
else:
    print("거짓")

# 삼항(ternary) 연산자
strike_out = True
print("페배" if strike_out else "승리")

if strike_out:
    print("페배")
else:
    print("승리")
    
    