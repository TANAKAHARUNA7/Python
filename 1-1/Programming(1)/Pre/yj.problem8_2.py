# 初期値（baseValue）を入力してグローバル変数として宣言
basevalue = float(input("基本の値を入力してください: "))

def selectOperation():
    global basevalue # →全域のbasevalueの値を呼び出してくる 
 # 加算、減算、乗算、除算のいずれかの選択しを出力し入力を受ける。
    print("1,足し算")
    print("2,引き算")
    print("3,掛け算")
    print("4,割り算")
    choice = int(input("選択: "))  # int()をつけることで選択肢を数字で指定

# 実行したい数字の入力をうける   
    num1 = float(input("数字の入力: "))
    
#割り算選択の際、分母が0の場合、「エラー：0で割ることができません」というメッセージを出力。 
    if choice == 4 and num1 == 0:
        print("エラー:0では割れません")
        return
# 足し算   
    if choice == 1:
        basevalue += num1
# 引き算           
    elif choice == 2:
        basevalue -= num1
# かけ算   
    elif choice == 3:
        basevalue *= num1
# 割り算   
    elif choice == 4:
        basevalue /= num1
    print("計算結果は: ",basevalue)
    return
# 結果を出力
selectOperation()

