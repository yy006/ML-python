# scikit-learn
オープンソースの機械学習アルゴリズムライブラリ
- ドキュメント：http://scikit-learn.org/stable/documentation
- ユーザーガイド：http://scikit-learn.org/stable/user_guide.
html
APIドキュメントと合わせて？

# Jupyter Notebook
ブラウザ上でコードを実行するためのインタラクティブな環境

本書全てのコード例　https://github.com/amueller/introduction_to_ml_with_python

# NumPy
Pythonで科学技術計算をする際の基本的なツール。多次元配列機能や、
線形代数やフーリエ変換、擬似乱数生成器などの、高レベルの数学関数など

http://www.scipy-lectures.org/
の最初の章を読むと良い

# SciPy
Pythonで科学技術計算を行うための関数を集めたもの。高度な線形代数ルーチンや、数学関数の最適化、信号処理、特殊な数学関数、統計分布など

SciPy Lecture Notes（http://www.scipy-lectures.org/）

# matplotlib
Pythonの科学技術計算向けのグラフ描画ライブラリ。折れ線グラフ、ヒストグラム、散布図などさまざまな可視化方法がサポートされている。

JupyterNotebookの内部では、`%matplotlib notebook`や%matplotlib inlineコマンドを用いると
図をブラウザ上に直接表示することができる

# pandas
データを変換したり解析したりするためのライブラリ。DataFrameというデータ構造を中心に構成されている。簡単に言うとpandasのDataFrameはテーブル（表）のようなもの

# mglearn
このライブラリは、グラフ描画やデータのロードなどの詳細なコードリストで本書が読みにくくならないようにするためのもの。コード中でmglearnを呼び出している部分があったら、きれいな絵を簡単に生成したり、何らかの興味深いデータをロードしている部分だと
思ってほしい

-----
本書を通じてNumPy、matplotlib、pandasを多用する。すべてのコードは次のように
インポートしていることを仮定している。
```
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
from IPython.display import display
```
さらに、Jupyter Notebookで、マジックコマンド```%matplotlib notebook```もしくは
`%matplotlib inline`を使っていることも仮定している