import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_absolute_error

x = np.random.rand(100, 1) * 10
y = 2.5 * x + np.random.rand(100, 1) * 4

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

y_train = y_train.ravel()
y_test = y_test.ravel()
print(y_train.shape)  # ravel()前 → (80, 1)
y_train = y_train.ravel()
print(y_train.shape)  # ravel()後 → (80,)


model = SGDRegressor(
    loss = 'squared_error',
    learning_rate='constant',\
    eta0=0.01,
    max_iter=1000,
    random_state=42
)

model.fit(x_train, y_train)

y_pred = model.predict(x_test)

fig, axes = plt.subplots(1, 2, figsize=(25, 10))

axes[0].scatter(x, y, color='blue', label='Original Data')
axes[0].set_title('Scatter plot of data')
axes[0].set_xlabel('X')
axes[0].set_ylabel('Y')
axes[0].legend()

x_val = np.linspace(0, 10, 100)
y_val = model.coef_[0] * x_val + model.intercept_[0]

axes[1].scatter(x, y, color='blue', label='Original Data')
axes[1].plot(x_val, y_val, color='green', label='SDG Regression Line')
axes[1].set_title('SDG Linear Regression')
axes[1].legend()

plt.tight_layout()
plt.show()

mse = mean_absolute_error(y_test, y_pred)
print(f"MSE: {mse:.4f}, 回帰回数: {model.coef_[0]:.4f},\
    切片: {model.intercept_[0]:.4f}")