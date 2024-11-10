# ユーザーから入力されたパスワードが安全かどうかを検証するプログラムを作成.

# password = input("비밀번어를 입력하세요: ")

# パスワードは次の基準
# 1)長さは8文字以上
# if len(password) >= 8:
#     # 2)少なくとも1つの数字
#     has_number = False
#     for char in password:
#         if char.isdigit():
#            has_number = True
#            has_uppercase = False
#            for char in password:
#                if char.isupper():
#                   has_uppercase = True
#                   print("パスワードが安全です")
#                   break
#                else:
#                   print("パスワードは安全でない")
#         else:
#             print("パスワードは安全でない")
# else:
#     print("パスワードは安全でない")


# 3)少なくとも1つの大文字
# いずれかが十分でない場合、パスワードは安全でない
# すべての条件が満たされている場合は「パスワードが安全です」
# 

password = input("비밀번어를 입력하세요: ")

def password_num(password):
    has_len = False
    if len(password) >= 8:
        has_len = True
    
    has_number = False
    for char in password:
        if char.isdigit():
            has_number = True
        
    has_uppercase = False
    for char in password:
        if char.isupper():
            has_uppercase = True
    if  has_len and  has_number and  has_uppercase:
        return True        
    
if  password_num(password):
    print("パスワードが安全です")
else:
    print("パスワードが安全ではありません")
    




