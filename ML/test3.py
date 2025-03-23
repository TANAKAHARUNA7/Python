import numpy as np

#　初期値を適当に設定
w = np.random.rand() # ランダムな傾き 
b = np.random.rand() # ランダムなバイアス

# 学習率
alpha = 0.01

# 勤続年数と給料データ
x = np.array([1, 2, 3, 4, 5])
y = np.array([300, 350, 400, 450, 500])

# 勾配降下法を10回実行
for _ in range(10):
    # 予測値の計算
    y_pred = w * x + b
    
    # コスト関数の計算（MSE）
    loss = np.mean((y_pred - y) ** 2)
    
    # 勾配の計算
    dw = np.mean(2 * (y_pred - y) * x) # wに対する勾配
    db = np.mean(2 * (y_pred - y))     # bに対する勾配
    
    # パラメーターの更新
    w = w - alpha * dw
    b = b - alpha * db
    
    print(f"w: {w:.3f}, b: {b:.3f}, Loss: {loss:.3f}")
