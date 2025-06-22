from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt

# 1. データセットの読み込みと準備
digits = load_digits()                          # 手書き数字の画像データ（8x8ピクセル）を読み込む
features = digits.data                          # (1797, 64): 各画像を64次元ベクトルとして取得
labels = digits.target                          # (1797,): 各画像の正解ラベル（0〜9）
learning_rate = 0.01                            # 学習率の設定
epoch = 100000                                  # エポック数（学習の繰り返し回数）

# 2. 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(
    features, labels, test_size=0.2, random_state=42, stratify=labels
)

np.set_printoptions(suppress=True)  # 出力設定：指数表記を禁止（小数表示を見やすく）

# 3. 特徴量の標準化（平均0、分散1にスケーリング）
scaler = StandardScaler()                       # 標準化オブジェクトの生成
X_train_std = scaler.fit_transform(X_train)     # 学習データの平均と分散でスケーリング
X_test_std = scaler.transform(X_test)           # テストデータにも同じスケーリングを適用

# 4. モデル初期化
num_features = X_train.shape[1]                 # 特徴量の数（64次元）
num_samples = X_train.shape[0]                  # 学習サンプルの数（1437個）
num_classes = 10                                # クラス数（0〜9）

W = np.random.randn(num_features, num_classes)  # 重み（64×10）をランダムに初期化
b = np.zeros(num_classes)                       # バイアス（10次元）をゼロで初期化

# 5. 学習ループ（エポック分繰り返す）
for ep in range(epoch):

    # 線形変換：各クラスごとのスコア（ロジット）を計算
    logit = X_train_std @ W + b                 # (1437, 10): 各サンプル × 各クラスのスコア

    # オーバーフロー防止のため、各サンプルごとの最大値を引く（数値の安定性）
    logit_max = np.max(logit, axis=1, keepdims=True)  # (1437, 1): 各行の最大値
    logit -= logit_max                                 # logit - 最大値

    # ソフトマックス関数によって確率に変換
    exp_logit = np.exp(logit)                          # 各logitを指数関数に変換
    exp_logit_sum = np.sum(exp_logit, axis=1, keepdims=True)  # 各サンプルの分母（和）
    softmax = exp_logit / exp_logit_sum                # ソフトマックス確率（正規化）

    # 正解ラベルを one-hot 表現に変換（例: 3 → [0,0,0,1,0,...,0]）
    i_matrix = np.eye(num_classes)                     # 単位行列（10×10）
    one_hot = i_matrix[y_train]                        # (1437, 10): one-hotに変換

    # 誤差（正解と予測の差）を計算
    error = one_hot - softmax                          # (1437, 10): 各クラスごとの誤差

    # 勾配（gradient）を計算
    gradient_w = -X_train_std.T @ error / num_samples  # (64, 10): 重みに対する勾配
    gradient_b = -np.sum(error, axis=0) / num_samples  # (10,): バイアスに対する勾配

    # パラメータの更新（勾配降下法）
    W -= learning_rate * gradient_w                    # 重みの更新
    b -= learning_rate * gradient_b                    # バイアスの更新

    # 損失関数（交差エントロピー）を計算
    loss = -np.sum(one_hot * np.log(softmax + 1e-10)) / num_samples  # 微小値を加えてlog(0)防止

    # 1000エポックごとに損失を表示
    if ep % 1000 == 0:
        print(loss)

    