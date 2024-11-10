# 掛け算プログラム：　2段から9段までの掛け算を出力します。
# range(X,y)からy-1までの数
# factor -> かけられる数のこと　 multiplier -> かける数のこと

# factor = range(2,10)  2,3,4,5,6,7,8,9
# multiplier = range(1.10) 1,2,3,4,5,6,7,8,9

for factor in range(2,10): # 右詰め　forは繰り返す（勝手に縦に）ていう意味。最後に「:」で閉める必要あり
    for multiplier in range(1,10):   # スペースを入れることで右詰めになる
     print(factor, "X", multiplier, "=", factor*multiplier)
    print("-------------")    # 見やすいように段が終わるたびに表示する。出しゃばっていいから前の行を超えていい
    