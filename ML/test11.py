from sklearn.model_selection import train_test_split
import numpy as np

# 1. ダミーデータ生成
# -x: 総100個のサンプル
# 　　各サンプルは3個の特性（feature）を持つ
# -y: 各サンプルの2進分類ラベル（0または1）
X = np.random.rand(100, 3)
y = np.random.randint(0, 2, size=100)

# 2. データセット1次元分割
# - 全体のデータの70％をTrain用、
# 　30%をテスト用（validation/test）に分割
X_train, X_temp, y_train, y_temp = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 3. データセット2次元分割
# - テストデータセット（30%）を再度50:50に分け
#　検証用とテスト用に分割
#　結果敵には全体基準で各15％づつ占める
X_val, X_test, y_val, y_test = train_test_split(
    X_temp, y_temp, test_size=0.5, random_state=42
)

# 4. 分割されたデータセットの大きさ出力
# - 各データセットがよく分けられているかshapeを通して確認
print("訓練データの大きさ:", X_train.shape)  # (70, 3) -> 全体の　70％
print("検証データの大きさ:", X_val.shape)    # (15, 3) -> 全体の　15％
print("テストデータの大きさ:", X_test.shape) # (15, 3) -> 全体の　15％


