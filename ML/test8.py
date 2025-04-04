from sklearn.linear_model import SGDRegressor
from sklearn.metrics import mean_squared_error
import numpy as np

np.set_printoptions(suppress=True, precision=1)
X = np.random.rand(100, 1) * 10
# H(x) = w * x + b
# randn = 정규 분포
y = 2.5 * X +  np.random.randn(100, 1) * 2
y = y.ravel()

# モデル生成後ハイパーパラメーター設定
model = SGDRegressor(
    max_iter=100,             # 学習反復回数（epoch数）
    learning_rate="constant", # 学習率を一定にする
    eta0=0.01,                # 学習率（η）を 0.01 に設定
    penalty=None,             # 正則化なし
    random_state=0            # 乱数シード固定（再現性のため）
)

#　学習実施
model.fit(X, y)

#　評価
# Loss
y_pred = model.predict(X)

mse = mean_squared_error(y, y_pred)