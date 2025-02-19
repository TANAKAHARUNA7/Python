num = 1

try:  # ★ ここから例外が発生するまでの処理が実行される
    print("1")  # ★ (1) "1" を出力
    
    if num == 1:
        raise KeyboardInterrupt  # ★ (2) 強制的に KeyboardInterrupt エラーを発生！

    print("2")  # ★ (3) ここには到達しない（エラーで try が中断）
    
except KeyboardInterrupt:
    print("4")  # ★ (4) "KeyboardInterrupt" が発生したので "4" を出力

else:
    print("5")  # ★ (5) `except` が実行されたので `else` はスキップ

finally:
    print("6")  # ★ (6) `finally` は必ず実行されるので "6" を出力

print("7")  # ★ (7) `try-except-finally` が終わったので "7" を出力

