import pandas as pd
import os

if __name__ == "__main__":
    from pymongo import MongoClient

    if not os.path.exists('./data'):
        os.mkdir('./data')

    url = open('dbserver', 'r').read()

    # MongoDBに接続し, テキストデータを取得
    client = MongoClient(url)
    collection = client['test']['hateb']

    df = pd.DataFrame.from_dict(list(collection.find())).astype(object)
    pd.DataFrame.to_csv(df, './data/hateb.csv')


# 保存したcsvファイルからDataFrameを構成
def getDataFrame():
    df = pd.read_csv('./data/hateb.csv')
    return df
