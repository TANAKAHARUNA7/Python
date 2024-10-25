# Nの入力を受け保存されたパターンで星を出力
n = int(input("Nの数を入力してください: "))

# ⓵　1番目の列からＮ番目の列まで星野個数を1つずつ追加させる。
for i in range(1,n + 1):
    star = i * "*"
    print(star)
# ⓶　Ｎ番目の列以降からは星の数は減少させて最後の列では星１つを出力。
for i in range(n-1,0,-1):
    star = i * "*"
    print(star)