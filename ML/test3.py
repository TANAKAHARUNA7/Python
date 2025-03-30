import numpy as np

# ランダムに初期の傾き（w）とバイアス（b）を決定
w = np.random.rand()  # 傾き（slope）：給料がどれだけ勤続年数に依存するか
b = np.random.rand()  # バイアス（切片）：勤続年数が0のときの初期給料

# 学習率（alpha）：勾配に対してどれだけパラメーターを更新するかを決定する値
alpha = 0.01

# 勤続年数（x）と対応する給料データ（y）
x = np.array([1, 2, 3, 4, 5])        # 入力データ（特徴量）
y = np.array([300, 350, 400, 450, 500])  # 目的変数（教師データ）

# 勾配降下法でパラメーターを10回更新（エポック数：10）
for _ in range(10):
    # 予測値を計算：y = wx + b の形
    y_pred = w * x + b

    # 平均二乗誤差（MSE）を計算：予測値と実測値の誤差の2乗の平均
    loss = np.mean((y_pred - y) ** 2)

    # wに関する勾配：∂Loss/∂w
    dw = np.mean(2 * (y_pred - y) * x)

    # bに関する勾配：∂Loss/∂b
    db = np.mean(2 * (y_pred - y))

    # パラメーターを更新：勾配の方向に少しずつ動かしてLossを減らす
    w = w - alpha * dw
    b = b - alpha * db

    # 現在のパラメーターとLossを出力
    print(f"w: {w:.3f}, b: {b:.3f}, Loss: {loss:.3f}")

