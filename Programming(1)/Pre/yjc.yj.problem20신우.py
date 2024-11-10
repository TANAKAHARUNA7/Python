import random
while True:
    print("1. 九九の出力\n2. ランダム値の三角形出力\n3. 終了")
    main = int(input("希望するメニュー番号を入力してください: "))
    if main == 1: # 1番を選択した場合
        while True:
            input_num = input("開始段と終了段を入力してください: ") 
            input_num = input_num.split("~") # ~を基準に分割
            start = int(input_num[0]) # startはinput_numの0番目を整数に変換した値
            end = int(input_num[1]) if len(input_num) > 1 else start # endはinput_numの1番目を整数に変換した値、~がなく1つだけ入力された場合はstartと同じ
            if 2 <= start <= 9 and 2 <= end <= 9: # startとendが2~9の範囲内の場合のみ九九を実行
                for dan in range(start, end + 1):
                    for num in range(1, 10):
                        print(f"{dan} x {num} = {dan * num}")
                    print()
                break
            else: # 2~9の範囲外の値が入力された場合はエラー
                print("2~9の範囲で入力してください")

    elif main == 2:
        while True: # while文を使用して、2~3の値でなければ再入力を促す
            num = int(input("三角形の高さの行数を入力してください（2以上3以下）\n"))
            rand_num_list = [] # 重複値の検査用の乱数リストを作成
            if 2 <= num <= 3: # 2~3の正確な値を受け取ると実行する
                for i in range(1, num + 1): 
                    for j in range(num - i): # 空白を出力
                        print(" ", end = "")
                    for j in range(i): # 乱数を出力
                        while True:
                            rand_num = random.randint(0, 9) # 0から9までの乱数を生成
                            if rand_num not in rand_num_list: # 乱数がrand_num_listにないか確認
                                rand_num_list.append(rand_num) # リストに追加
                                break # 重複がなければループを終了
                        print(rand_num, end = "")
                    print()
                break
            else:
                print("2または3を入力してください。")

    elif main == 3:
        print("プログラムを終了します。")
        break

    else:
        print("\n1〜3の範囲の正しいメニュー番号を入力してください。")
