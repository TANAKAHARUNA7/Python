import numpy as np

num_features = 3
num_sample = 1000

np.random.seed(1)
np.set_printoptions(suppress=True, precision=3)
X = np.random.rand(num_sample, num_features)

# h(x) = wx1 + wx2 + wx3 + b
w_true = np.random.randint(1, 10, num_features)
b_true = np.random.randn() * 0.5

y = X @ w_true + b_true

 # Learning
w = np.random.rand(num_features)  # 초기 가중치
b = np.random.randn()  # 초기 절편
learning_rate = 0.01
epochs = 10000

for epoch in range(epochs):
    # prediction
    # @ -> 行列の掛け算記号
    prediction = X @ w + b

    # error -> 予測値と正解値の誤差
    error = prediction - y

    # gradient 
    gradient = X.T @ error / num_sample

    w = w - learning_rate * gradient
    b = b - learning_rate * error.mean()

print(f"w_true: {w_true}, b_true: {b_true}")
print(f"w : {w}, b : {b}")