# Pre-trained model for fastText, tokenized with mecab-ipadic-NEologd
- Compatible with [fastText.py](https://github.com/salestock/fastText.py) (fasttext 0.8.3 in pypi)
- Tokenized with [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)

## Background
Doing japanese NLP task with [fastText](https://github.com/facebookresearch/fastText) and [MeCab](http://taku910.github.io/mecab/), I found [fastText.py](https://github.com/salestock/fastText.py)(fasttext 0.8.3 in pypi) [is not updated](https://github.com/salestock/fastText.py/pull/128) with the up-to-date fastText(I checked it in 20170912). So [pre-trained model provided in fastText repository](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md) didn't work. While [pre-trained models by Kyubyong](https://github.com/Kyubyong/wordvectors) worked with fastText.py as it is trained with old version of fastText, it seems it used default MeCab dictionary. So I trained fastText model with japanese wiki data (20170820 dump) and mecab-ipadic-NEologd (20170907).

## Environment
* nltk >= 1.11.1
* regex >= 2016.6.24
* lxml >= 3.3.3
* numpy >= 1.11.2
* mecab & mecab python binding
* fasttext & Cython

## How to train own model
1. Download the japanese [wikipedia database backup dumps](https://dumps.wikimedia.org/backup-index.html).
2. Extract running texts to `data/` folder.
3. Install MeCab and mecab-ipadic-NEologd.
4. Run `$ python build_corpus.py --lcode=ja --max_corpus_size=1000000000`. Adjust maximum corpus size as you want.
5. Run `$ python ft.py` to get fastText word vector in `data/` folder. Adjust min_count as you want in `ft.py`.

## Download pre-trained model
[Link](https://drive.google.com/open?id=0B0FtN_HpeUHHT0UtSDBvRHJVWms) (Vector size: 300, Vocabulary size: 92056)

## References
- [Kyubyong/wordvectors](https://github.com/Kyubyong/wordvectors)
- [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)
- [fastText](https://github.com/facebookresearch/fastText)
- [fastText.py](https://github.com/salestock/fastText.py)
- [MeCab](http://taku910.github.io/mecab/)
