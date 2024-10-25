import os

# mrmdir ファイル名

# cd ..　#　一つ上のファイルへ
# cd ..  -> ../

# Relative reference
#f_handler = open(r"imgs/test.txt", "r")

# Absolute reference
# ファイルを開く：
f_handler = open(r"c:/myGame/imgs/test.txt", "r")

# ファイルの内容を読んで返還する
msg = f_handler.read()

print(msg)

# 
f_handler.close()




