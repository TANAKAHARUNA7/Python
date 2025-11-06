class MyDataset:
    # コンストラクタ：データ（特徴とラベル）を入れて初期化する
    def __init__(self, feature: list, label: list) -> None:
        # 例: feature = [1, 2, 3], label = [10, 20, 30]
        # ※ 実運用では feature と label の長さが同じかチェックするのが安全
        self.feature: list = feature
        self.label: list = label

    # 人が読む用の表示（print(dataset) などで使われる）
    def __str__(self):
        # \ を使って1行で書いているが、見やすさ重視なら3連クォートでもOK
        return f"Dataset: \nfeature: {self.feature}\
            \nlabel: {self.label}"
    
    # 添字アクセス（取り出し）：dataset[i] → (feature[i], label[i])
    def __getitem__(self, index) -> tuple:
        # 例: dataset[2] → (3, 30)
        return self.feature[index], self.label[index]
    
    # 添字代入（入れ替え）：dataset[i] = (new_feature, new_label)
    def __setitem__(self, index: int, value: tuple[list, list]) -> None:
        # 例: dataset[2] = ([5], [50])
        # ※ ここでは「[5]」のように“リスト”を入れている点に注意。
        #   もとの feature 要素が int（1,2,3）なので、型を揃えるなら 5 / 50 のようにスカラーを入れるほうが自然。
        self.feature[index] = value[0]
        self.label[index] = value[1]
    
    # データ数（要素数）を返す：len(dataset) で呼ばれる
    def __len__(self):
        # Pythonの「シーケンスプロトコル」により、__len__ と __getitem__ があれば
        # for ループで自動的に繰り返せる（__iter__ を自作しなくてもOK）
        return len(self.feature)
    
    # __repr__ は開発者向けの“正確な表現”。デバッグやREPL表示に使われる
    # def __repr__(self):
    #     # 再現可能な形にするのが理想（クラス名(引数…)の形式）
    #     return f"MyDataset({self.feature!r}, {self.label!r})"


# --------- ここから動作例 ---------
dataset = MyDataset([1, 2, 3], [10, 20, 30])

print(dataset[2])  # get → 2番目(sample)の値 (feature, label) => (3, 30)

dataset[2] = ([5], [50])  # 2番目(sample)を入れ替え

print(dataset[2])  # => ([5], [50])

# for ループ（__len__ と __getitem__ により反復可能）
# 内部的には index=0,1,2,... と順に __getitem__ が呼ばれる
for x, y in dataset:  # dataset.__iter__() が無くてもOK（シーケンス扱い）
    print(f"x, y: {x}, {y}")
