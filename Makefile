PY=/usr/local/bin/python3
DIC=/usr/local/lib/mecab/dic/mecab-ipadic-neologd
DB='localhost:27017'

.PHONY: all
all:
	make data && make run

.PHONY: run
run:
	$(PY) src/doc2vec.py $(DIC)

data:
	$(PY) src/database.py $(DB)

.PHONY: clean
clean:
	rm -r ./data
