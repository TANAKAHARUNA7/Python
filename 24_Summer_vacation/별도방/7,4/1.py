import os # Operating System

# 現在ウォーキングディレクトリーを文字列で返還
print(os.getcwd())

# ファイルを開く：
# 絶対参照
f_handler = open("c:/foo/bar/test.txt", "r")

# 相対参照
# f_handler = open("bar/test.txt", "r")

                   # ../ ../ -> 二段階上にあがる
# f_handler = open("../foo/bar/test.txt", "r")


# ファイルの内容を読んで返還する
msg = f_handler.read()

# ファイル出力
print(msg)

# オープンされたファイルを閉じる
f_handler.close()