import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# データ生成
x = np.random.rand(100, 1) * 10
y = 2.5 * x + np.random.rand(100, 1) * 4

# データ分割
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# モデル学習
model = LinearRegression()
model.fit(x_train, y_train)

# 予測または評価
y_pred = model.predict(x_test)
# プロット準備
fig, axes = plt.subplots(1, 2, figsize=(25, 10))
# 原本データ散布図
axes[0].scatter(x, y, color='blue', label='Original Data')
axes[0].set_title('Scatter plot of data')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend()

# 回帰線またはデータ散布図
x_val = np.linspace(0, 10, 100)
y_val = model.coef_[0, 0] * x_val + model.intercept_[0]

axes[1].scatter(x, y, color='blue', label='Original Data')
axes[1].plot(x_val, y_val, color='red', label='Regression Line')
axes[1].set_title('Linear Regression')
axes[1].legend()

plt.tight_layout()
plt.show()

# 回帰線出力
mse = mean_squared_error(y_test, y_pred)
print(f"MSE: {mean_squared_error(y_test, y_pred)}, 回帰個数: {model.coef_[0,0]}, 切片:{model.intercept_[0]}")


