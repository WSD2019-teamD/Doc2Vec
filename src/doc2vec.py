#coding: UTF-8

import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from gensim.models.doc2vec import Doc2Vec
from gensim.models.doc2vec import TaggedDocument
from sklearn.cluster import KMeans
from collections import defaultdict

from parse import parseText
from database import getDataFrame


# https://qiita.com/YIPG/items/476c814ea6d548e070e5

dic = sys.argv[1]
df = getDataFrame()
td = []

# 1文書ずつ、単語に分割してリストに入れていく[([単語1,単語2,単語3],文書id),...]こんなイメージ
# words：文書に含まれる単語のリスト（単語の重複あり）
# tags：文書の識別子（リストで指定．1つの文書に複数のタグを付与できる）
for i in range(len(df)):
    wordlist = parseText(text=str(df['content'][i]), sysdic=dic)
    td.append(TaggedDocument(words=wordlist, tags=[i]))

#モデル作成
model = Doc2Vec(documents=td, dm = 1, vector_size=300, window=8, min_count=10, workers=4)

#ベクトルをリストに格納
vectors_list=[model.docvecs[n] for n in range(len(model.docvecs))]

#ドキュメント番号のリスト
doc_nums=range(len(model.docvecs))

#クラスタリング設定
#クラスター数を変えたい場合はn_clustersを変えてください
n_clusters = 8
kmeans_model = KMeans(n_clusters=n_clusters, verbose=1, random_state=1, n_jobs=-1)

#クラスタリング実行
kmeans_model.fit(vectors_list)

#クラスタリングデータにラベル付け
labels=kmeans_model.labels_

#ラベルとドキュメント番号の辞書づくり
cluster_to_docs = defaultdict(list)
for cluster_id, doc_num in zip(labels, doc_nums):
    cluster_to_docs[cluster_id].append(doc_num)

#クラスター出力
for docs in cluster_to_docs.values():
    print(docs)


# DataFrameにcluster_idのカラムを追加
df['cluster_id'] = labels

categories = df['category'].unique()
df2 = pd.DataFrame()
# 各クラスターの文書数をカテゴリーごとに数える
for category in categories:
    df2[category] = [((df['category'] == category) & (df['cluster_id'] == i)).sum() for i in range(8)]

# グラフ出力
df2.plot.bar(stacked=True)
plt.title("Document clusters")
plt.xlabel('cluster ID')
plt.ylabel('number of documents')
plt.show()
