import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

from database import fetchData
from doc2vec import clustering
from stopwords import maybe_download


if not os.path.exists('./data/hateb.csv'):
    fetchData()

if not os.path.exists("./data/stop.txt"):
    maybe_download("./data/stop.txt")

if not os.path.exists('./data/hateb_cluster.csv'):
    clustering(sys.argv[1])
 

df = pd.read_csv('./data/hateb_cluster.csv')

categories = df['category'].unique()
df2 = pd.DataFrame()

# 各クラスターの文書数をカテゴリーごとに数える
for category in categories:
    df2[category] = [((df['category'] == category) & (df['cluster_id'] == i)).sum() for i in range(8)]

print(df2)
df2.to_csv('./data/category.csv')

# グラフ出力
df2.plot.bar(stacked=True)
plt.title("Document clusters")
plt.xlabel('cluster ID')
plt.ylabel('number of documents')
plt.show()
