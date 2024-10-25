import os  # os  モデュールインポート

# 現在の Working Directoryの 経路を持ってきて'msg'変数に保存
msg = os.getcwd()
print(type(msg), msg) # タイプ　<class 'str'>, 値は現在のディレクトリーの経路

# 現在のディレクトリーのファイルまたは下位ディレクトリーの目録を持ってきて'msg'変数の保存
msg = os.listdir()
print(type(msg), msg)

# 現在のディレクトリーに'kin'という名前の新しいディレクトリーを生成
os.mkdir("kin")

# 現在の作業ディレクトリを生成された 'kin'ディレクトリに変更
os.chdir("kin")

# 現在 Working Directory 経路を持ってきて 'msg' 変数に保存
msg = os.getcwd()
print(type(msg), msg)  # これで経路は'kin'ディレクトリを含んだ経路になる


#########################################################

# f_handler_1 = open("test_1.txt", "r")

# msg = "king"

# f_handler_1.write(msg)

# f_handler_1.close()



