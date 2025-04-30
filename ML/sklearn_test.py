from sklearn.datasets import fetch_california_housing

data = fetch_california_housing()

# 特徴量
X = data.data
# 目的変数
y = data.target

feature_message = data.feature_names

print(type(data), type(X), type(feature_message))
# 
