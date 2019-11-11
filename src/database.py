from pymongo import MongoClient
import pandas as pd

# MongoDBに接続し, テキストデータを取得
def getDocuments(url):
    client = MongoClient(url)
    collection = client['scraping-book']['items']

    df = pd.DataFrame.from_dict(list(collection.find())).astype(object)
    return list(df['content'])
