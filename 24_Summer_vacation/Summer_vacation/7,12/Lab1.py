# 学生成績処理プログラム
# 成績の入力を受けリストに保存して入力された値を出力する

# 学生の情報を保存するためのディクショナリーを生成
dict_std_info = {}

def std_grade_input():
    global std_num, count, total_avg
    
    # 学生たちの情報を入力する
    std_num = int(input("学番を入力"))
    name = input("名前を入力")
    kor = int(input("国語成績入力"))
    eng = int(input("英語成績入力"))
    math = int(input("数学成績入力"))

    # 総合点数と平均点を計算
    total_sum = kor + eng + math
    avg = total_sum / 3
    
    # 入力データの個数と全体の学生の平均点を求めるための計算
    count += 1
    total_avg = (total_avg + avg) / count
    
    # Dictionaryを作用し学番をkey値に、残りの情報はValueとしてリストに保存
    dict_std_info[std_num] = [name, kor, eng, math, total_sum, avg]




while True:
    print("=" * 20)
    print("1. 成績を入力してください")
    print("")






# 学生たちの情報を保存するためのディクショナリーを生成
    std_info = {}
 
# 1．学生の成績入力関数の定義






# 2．学生目録出力関数の定義






# 3．学生目録出力関数の定義 






# 無限ループを通してプログラム終了まで無限反復 
# 
# 
# 
# #