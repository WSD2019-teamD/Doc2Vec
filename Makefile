PY=/usr/local/bin/python3
DIC=/usr/local/lib/mecab/dic/mecab-ipadic-neologd

.PHONY: all
all:
	make data && make run

.PHONY: run
run:
	$(PY) src/doc2vec.py $(DIC)

data:
	$(PY) src/database.py

.PHONY: clean
clean:
	rm -r ./data
