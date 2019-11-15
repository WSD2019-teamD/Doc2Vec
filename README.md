# Doc2Vec

Doc2Vecで文書のクラスタリング

現時点ではクラスタリング結果の棒グラフ表示を行う

## 実行方法


MongoDBサーバーのURLを記述したファイルを`dbserver`という名前でトップディレクトリに配置してください \
Makefileの変数は各自の環境に合わせて変更してください

`make data`でDBサーバーからデータを取得(すでに取得済みの場合は何もしない) \
`make run `でクラスタリングを実行し結果を表示

`make`または`make all`で両方を順番に実行します

データを再取得したい場合は`make clean`でデータを一度消去してください


