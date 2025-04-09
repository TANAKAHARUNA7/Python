import numpy as np

# <class 'numpy.ndarray'> → NumPyの配列オブジェクト（ndarray型）であることを意味する
# random.rand() : 0〜1の間の乱数を生成する関数
# rand() の引数は「配列の形（次元）」を意味する
print(type(np.random.rand(2, 3)))  # 出力は <class 'numpy.ndarray'>

# set_printoptions：NumPy配列の出力形式を設定する関数
# suppress=True：指数表記（例: 1e-5）を使わず、通常の小数で表示
# precision=2：小数点以下2桁まで表示（例: 0.13）
np.set_printoptions(suppress=True, precision=2)

# 2行3列の乱数を生成
bar = np.random.rand(2, 3)
print(bar)  # 2次元配列（行列）
print("----" * 10)

# 各要素に10を掛ける → 0〜10の間の乱数にスケール変換
bar = bar * 10
print(bar)
