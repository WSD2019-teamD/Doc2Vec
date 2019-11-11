PY=/usr/local/bin/python3
DIC=/usr/local/lib/mecab/dic/mecab-ipadic-neologd
DB=localhost:27017

.PHONY: run
run:
	$(PY) src/doc2vec.py $(DIC) $(DB)
