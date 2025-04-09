# 必要なライブラリのインポート
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error

# データの作成: xは0〜10の範囲でランダムに生成（100個）
x = np.random.rand(100, 1) * 10
# y = 2.5 * x にノイズ（最大4）を加えたデータを作成
y = 2.5 * x + np.random.rand(100, 1) * 4

# データをトレーニングセットとテストセットに分割（8:2）
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# yは1次元配列に変換（SGDRegressorは1次元yを要求）
y_train = y_train.ravel()
y_test = y_test.ravel()

# SGDRegressorのモデルを定義
model = SGDRegressor(
    loss='squared_error',       # 損失関数（最小二乗誤差）
    learning_rate='constant',   # 学習率は一定
    eta0=0.01,                  # 初期学習率
    max_iter=1000,              # 最大1000回のイテレーション
    random_state=42             # 再現性のためのシード
)

# モデルの学習（x_trainとy_trainを使用）
model.fit(x_train, y_train)

# テストデータに対して予測
y_pred = model.predict(x_test)

# グラフ描画の準備（2つのグラフを横並びに表示）
fig, axes = plt.subplots(1, 2, figsize=(25, 10))

# 左のグラフ：元データの散布図
axes[0].scatter(x, y, color='blue', label='Original Data')
axes[0].set_title('Scatter plot of data')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend()

# 線形回帰直線の描画のためのx値（0〜10を100個に分割）
x_val = np.linspace(0, 10, 100)
# 回帰直線のy値を計算（y = ax + b）
y_val = model.coef_[0] * x_val + model.intercept_[0]

# 右のグラフ：元データと回帰直線の表示
axes[1].scatter(x, y, color='blue', label='Original Data')
axes[1].plot(x_val, y_val, color='green', label='SDG Regression Line')
axes[1].set_title('SDG Linear Regression')
axes[1].legend()

# レイアウトを整えて表示
plt.tight_layout()
plt.show()

# 平均絶対誤差（Mean Absolute Error）を計算して出力
mse = mean_absolute_error(y_test, y_pred)
print(f"MSE: {mse:.4f}, 回帰回数: {model.coef_[0]:.4f}, 切片: {model.intercept_[0]:.4f}")
