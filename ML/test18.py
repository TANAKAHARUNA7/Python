import numpy as np

num_features = 4 # 入力（x）の項目は４つ
num_sample = 1000 # Sample（データ）は1000個

np.random.seed(5) # 毎回同じ乱数がでるように固定

# 0 ~ 2の範囲で4つの特徴を持つ1000このデータを作る                    
X = np.random.rand(num_sample, num_features) * 2
# 1 ~ 10の範囲で正解の重みを作る
w_true = np.random.randint(1, 11, (num_features, 1))
b_true = np.random.randn() * 0.5
y = X @ w_true + b_true 

#########################################
# 最初の予測モデルのパラメータ（重みとバイアス）を適当に決める
w = np.random.rand(num_features, 1)
b = np.random.rand()
# 学習率（learning rate）
learn_rate = 0.01

for _ in range(10000):
    # 予測値
    predict_y = X @ w + b

    # 誤差
    error = predict_y - y 
    # x = np.random.randint(1, 4, (2,2)) # [2 1 1]
    # y = np.random.randint(1, 4, (2,2)) # [2 2 1]

    # 切片
    gradient_w = X.T @ error / num_sample
    gradient_b = error.mean()

    w = w - learn_rate * gradient_w
    b = b - learn_rate * gradient_b

print(f"w_true: {w_true}\nb_true: {b_true}\n\n")
print(f"w: {w}\nb: {b}")
    # print(f"{x}\n{w}\n{x@w}") # 7