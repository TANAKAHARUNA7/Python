# 初期資本金で株式を購入し、以後、株式価格が変動した後に株式を販売して得られる利益や発生する損失を計算する

# ユーザーから次の情報を受ける。
# １）初期資本金（例：10000）
# ２）株式の購入価格（例：100）
# ３）買う株式の数（例：50）
# ４）販売時の株価（例：150）

capital = int(input("初期資本金を入力してください： "))
stock_price = int(input("株式の価格を入力してください： "))
stock_Value = int(input("株式の数を入力してください： "))
sell_stock = int(input("販売時の株価を入力してください： "))

# 総購入費用    =    購入価格   X   株式数
total_buy_price =  stock_price * stock_Value 

# 購入後に残った資本金 = 初期資本金 - 総購入費用
rest = capital - total_buy_price
print("購入後の残りの資本金:",float(rest))

# 販売金額     =     販売時の株価  x  株式数
total_sell_stock = sell_stock * stock_Value
# 予想利益  =     販売金額   -    総購入費用
get_money = total_sell_stock - total_buy_price
# 結果出力：購入後に残った資本金と予想利益（または損失）を出力。
print("予想利益：",float(get_money))

# 株式販売時の予想利益or損失利益が発生した場合出力
if get_money < 0 :
    print("損失")
else:
    print("予想された利益")
 


