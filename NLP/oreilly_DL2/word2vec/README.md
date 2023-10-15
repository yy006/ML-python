ゼロから作るDeeplearning2 自然言語処理編の実装
[本書のソースコード](https://github.com/oreilly-japan/deep-learning-from-scratch-2)

- 文章の各言葉を低い次元の実数ベクトルで表現したい
- CBOW or skip-gramのNNモデルと階層的ソフトマックス or ネガティブサンプリングの計算高速化手法の二つを組み合わせたもの

train.py 
- corpus, word_to_id, id_to_word = ptb.load_data('train')  

引数：データタイプ（'train'、'val'、または'test'）
戻り値：単語ID の配列と、単語からIDへのマッピングとIDから単語へのマッピングの2つの辞書

- contexts, target = create_contexts_target(corpus, window_size)  

引数：単語ID の配列、コンテキストのウィンドウサイズ
戻り値：コンテキストとターゲットをそれぞれ NumPy の多次元配列として返す

- model = CBOW(vocab_size, hidden_size, window_size, corpus)  

引数：語彙数、中間層のニューロン数、ウィンドウサイズ、単語ID の配列
CBOWモデルのインスタンスを作成

- trainer = Trainer(model, optimizer)  

引数：model、最適化アルゴリズム
Trainerインスタンスを作る

- trainer.fit(contexts, target, max_epoch, batch_size)  

引数：コンテキスト、ターゲット、
作ったTrainerインスタンスにデータとハイパラを渡して学習