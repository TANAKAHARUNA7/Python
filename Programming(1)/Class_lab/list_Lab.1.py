# ショッピングリスト作成
shopping_list = []
#リスト内に”牛乳”、”パン”、”卵”、”リンゴ”を追加
shopping_list.extend(["우유","빵","계란","사과"]) # .extend([])を使うことで結果で[]を表示せず追加することができる
shopping_list.append("우유") # .append([])とかくとリストの中にリストを作る感じになる

# リスト内を出力
print("현재 쇼핑 리스트",shopping_list)

# トイレットペーパーをリストの1番前に追加
shopping_list.insert(0,"휴지")

# オレンジジュースをリストの2番目に追加
shopping_list.insert(2,"오랜지 주스")
# 最後にチキン、ライスをリストに追加
shopping_list.extend(["치킨","밥"])
 
# リスト内をすべて表示
print("최종 쇼핑 리스트",shopping_list)

