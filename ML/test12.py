import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error

# X : 0 ~ 10の間で無作為数100個
# y : 2.5x + 少しのノイズ
np.random.seed(0)  # 乱数が毎回同じ順番で出る（再現可能）
print(np.random.rand(3))
X = np.random.rand(100, 1) * 10
y = 2.5 * X + np.random.randn(100, 1) * 2
y = y.ravel()  # yを1次元に（SGDRegressorが1次元を要求するため）

model = SGDRegressor(max_iter = 1000,
                     learning_rate='constant',
                     eta0=0.01,
                     penalty=None,
                     random_state=0)

model.fit(X, y)
y_pred = model.predict(X)
mse = mean_squared_error(y, y_pred)
print(f"MSE: {mse:.4f}")
print(f"傾き（coef_）: {model.coef_[0]:.2f}")
print(f"切片（intercept_）: {model.intercept_[0]:.2f}")

x_line = np.linspace(0, 10, 100).reshape(-1, 1)
y_line = model.predict(x_line)

plt.scatter(X, y, label = 'Date', alpha=0.6)
plt.plot(x_line, y_line, color='red', label='SGD Regression Line')
plt.xlabel("X")
plt.ylabel("y")
plt.title("Linear Regression with SGDRegressor")
plt.legend()
plt.grid(True)
plt.show()

