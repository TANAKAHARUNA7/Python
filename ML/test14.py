import numpy as np
# H(x) = 5X1 + 3X2 + 3
num_of_samples = 5
num_of_features = 2

# data set
np.random.seed(42)
np.set_printoptions(False, suppress=True)

# np.random.rand(行数, 列数) -> 0〜1の間のランダムな小数を作る
X = np.random.rand(num_of_samples , num_of_features) * 10
x_true = [5, 3]
b_true = 4
noise = np.random.randn(num_of_samples) * 0.5
y = X[:,0] * 5 + X[:, 1] * 3 + b_true + noise

print(X)
print(y)
# print(X[:,0] * 5)
# print(X[:,1] * 3) # 全部の列を選択　→　“：”
# print(X[:,0] * 5 + X[:, 1] * 3 + b_true) 
