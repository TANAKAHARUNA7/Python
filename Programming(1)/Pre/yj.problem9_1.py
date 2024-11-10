# 入力
# 1.出発時間（時間）
Depart_houre = int(input("出発時（時間）を入力してください: "))
# 2.出発時間（分）
Depart_minutes = int(input("出発時（分）を入力してください: "))
# 3.到着時間（時間)
arrival_houre = int(input("到着時（時間）を入力してください: "))
# ４.到着時間（分）
arrival_minutes = int(input("到着時（分）を入力してください: "))
# ５.移動距離
moving_distance = float(input("移動距離を入力してください: "))

#時間を分に換算
Depart_time = Depart_houre * 60 + Depart_minutes
arrival_time = arrival_houre * 60 + arrival_minutes
mova_time = (arrival_time - Depart_time ) / 60

# 平均移動時間
average_speed = moving_distance / mova_time                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             

#出力
# 1.移動距離
print("移動距離: %.1f"%moving_distance,"km")
# 2.出発時間（時間）
print("出発時間: ",Depart_houre,"時",Depart_minutes,"分")
# 3.到着時間（時間）
print("到着時間: ",arrival_houre,"時",arrival_minutes,"分")
# 4.平均速度
print("平均速度: %.2f"%average_speed,"km/h")

# 速度の状態
# ⓵59km/h以下　遅い
if average_speed <= 59:
    print("速度の状態: 遅い")
# ⓶60～89km/h　普通
elif 60 <= average_speed <= 89:
    print("速度の状態: 普通")
# ⓷90km/h以上　早い
else:
    print("速度の状態: 高速")