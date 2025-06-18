from sklearn.datasets import load_digits # 手書き数字データセットの読み込み用関数
from sklearn.model_selection import train_test_split # データ分割用関数
from sklearn.preprocessing import StandardScaler # 標準化（スケーリング）用クラス
import numpy as np
import matplotlib.pyplot as plt  # グラフ表示（ここでは未使用

# 1. データセットのロード（load_digitsは8×8の手書き数字画像を含む）
digits = load_digits()
# 特徴量（画像のピクセル情報）とラベル（0〜9の正解数字）を取得
features = digits.data     # shape: (1797, 64)  ← 各画像が8×8ピクセル=64次元ベクトル
labels = digits.target     # shape: (1797,)     ← 対応する数字ラベル（0〜9）
print(features.shape)
print(labels.shape)
print(labels[:30])


# 2. データを学習用とテスト用に分割
X_train, X_test, y_train, y_test = train_test_split(
    features,        # 入力データ（特徴量
    labels,          # 正解ラベル
    test_size=0.2,   # テストデータは20%
    random_state=42, # 再現性を保つための乱数シード
    stratify=labels  # 各クラスの割合を均等に保つ（クラスの偏りを防ぐ）
)

# 3. 特徴量の標準化（平均0、分散1に変換）
scaler = StandardScaler()    # StandardScalerオブジェクトの生成
X_train_std = scaler.fit_transform(X_train)   # 学習データでスケーラーを学習＆変換
X_test_std = scaler.transform(X_test)         # テストデータは学習時のスケーラーを使用して変換


np.set_printoptions(suppress=True)

num_features = X_train_std.shape[1]  # 入力データ次元 (64)
num_sample = X_train_std.shape[0]    # 学習sample
num_classes = 10                     # 分割クラス個数(0~9)

W = np.random.randn(num_features, num_classes) # 64, 10 
b = np.zeros(num_classes) # 10, 
learning_rate = 0.01
epochs = 10000

for epoch in range(epochs):

    # X (1437, 64) @ w (64, 10) + b (10, )
    logit = X_train_std @ W + b # 1437, 10
    logit_max = np.max(logit, axis=1, keepdims=True)
    logit -= logit_max
    exp_logit = np.exp(logit)
    exp_logit_sum = np.sum(exp_logit, axis=1, keepdims=True)
    softmax = exp_logit / exp_logit_sum

    i_matrix = np.eye(num_classes)
    one_hot = i_matrix[y_train]

    # error = softmax(1437 - 10) - one_hot (1437 )
    error = softmax - one_hot

    gradient_w = X_train_std.T @ error / num_sample
    gradient_b = np.sum(error, axis=0) / num_sample

    W -= learning_rate * gradient_w
    b -= learning_rate * gradient_b
    loss = np.log(softmax + 1e-15) * one_hot

    if epoch % 1000 == 0:
        print(loss)