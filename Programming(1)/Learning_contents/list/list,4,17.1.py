grades = [90, 70, 98, 100]

# sum() -> リスト内の全ての数を足す。
average_grade = sum(grades) / len(grades)
print(average_grade)

# 変数　＝　sorted() -> リストを並び変える。(元のリストはそのままで)
# 変数　＝ sorted(リスト名，reverse=True) -> 大きい⇒小さい順
# 変数　＝　sorted() or sorted(リスト名，reverse=False) -> 小さい⇒大きい順
sorted_grades = sorted(grades, reverse=True)
print(sorted_grades)

# .sort() -> 小さい⇒大きい順。元のリストの並びも変わる
# grades.sort()
# print(grades)

# 整理されたリストから特定の成績の位置を探して順位を計算する。
# index() -> リスト内の値を表示する。
# リストのインデックスは0から始まるため実際の順位を求めるにはインデックスに　1を足す。
rank = sorted_grades.index(90) + 1
print(rank)


