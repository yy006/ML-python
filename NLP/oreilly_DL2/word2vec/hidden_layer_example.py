# 入力層から隠れ層への変換の例
import numpy as np

c = np.array([[1, 0, 0, 0, 0, 0, 0]]) # 入力
W = np.random.randn(7, 3) # 重み 正規分布でランダムにとる
h = np.dot(c, W) # 中間ノード 行列の積
print(h)

# cはone hotなので、cWは対応する場所の行ベクトルだけ抜き出すことと対応

