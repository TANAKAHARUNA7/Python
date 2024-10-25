import os  # os モデュールインポート

# 現在　Working Directory 経路を持ってきて ‘msg’ 変数に保存 
msg = os.getcwd()
print(type(msg), msg)  # 

msg = os.listdir()
print(type(msg), msg)

os.mkdir("kin")

os.chdir("kin")

msg = os.getcwd()
print(type(msg), msg)