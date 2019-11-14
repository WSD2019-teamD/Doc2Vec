PY=/usr/local/bin/python3
DIC=/usr/local/lib/mecab/dic/mecab-ipadic-neologd

.PHONY: run
run:
	$(PY) src/main.py $(DIC)

.PHONY: clean
clean:
	rm -r ./data
