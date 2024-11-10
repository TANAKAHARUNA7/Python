#ユーザーから"left","right", "up", "down"のいずれかの単語を入力を受ける
direction = input("方向を入力してください")

# 文字に従って、「左に移動します」、「右に移動します」、「上に移動します」、「下に移動します」を出力する
r = "right"
u  = "up"
d = "down"
l = "left"

if direction == r:
    print("右に移動します")
elif direction == l:
    print("左に移動します")
elif direction == u:
    print("上に移動します")
elif direction == d:
    print("下に移動します")
else:
    print("不明なコマンドです")