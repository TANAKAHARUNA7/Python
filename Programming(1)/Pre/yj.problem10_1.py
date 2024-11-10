# 図書タイトルを入力すると、図書リストに追加していくプログラム
books = []

# 終了」と入力するまでこのプロセスを繰り返し、最後に全体の本リストを出力してください
while True:
    title = input("図書の題名を入力してください(終了するなら'終了'を入力): ")
    if title == '終了':
       break
    books.append(title)
print("図書目録: ",books)       
