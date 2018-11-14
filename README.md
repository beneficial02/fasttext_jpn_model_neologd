# Pre-trained model for fastText
- Compatible with [fastText.py](https://github.com/salestock/fastText.py) (fasttext 0.8.3 in pypi)
- Tokenized with [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)

## Background
Doing japanese NLP task with [fastText](https://github.com/facebookresearch/fastText) and [MeCab](http://taku910.github.io/mecab/), I found [fastText.py](https://github.com/salestock/fastText.py)(fasttext 0.8.3 in pypi) [is not updated](https://github.com/salestock/fastText.py/pull/128) with the up-to-date fastText(I checked it in 20170912). So [pre-trained model provided in fastText repository](https://github.com/facebookresearch/fastText/blob/master/pretrained-vectors.md) didn't work. [Pre-trained models by Kyubyong](https://github.com/Kyubyong/wordvectors) worked with fastText.py(0.8.3) as it is trained with old version of fastText, but it seemed to use default MeCab dictionary. So I trained fastText model with japanese wikipedia data (20170820 dump) and mecab-ipadic-NEologd (20170907).

## Environment
* nltk >= 1.11.1
* regex >= 2016.6.24
* lxml >= 3.3.3
* numpy >= 1.11.2
* MeCab & MeCab python binding
* [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)
* [fastText.py](https://github.com/salestock/fastText.py)

## How to train your own model
1. Download the japanese [wikipedia database backup dumps](https://dumps.wikimedia.org/backup-index.html).
2. Extract running texts to `data/` folder.
3. Set up the environment.
4. Run `$ python build_corpus.py --lcode=ja --max_corpus_size=1000000000`. Adjust max_corpus_size as you want.
5. Run `$ python ft.py` to get fastText word vector in `data/` folder. Adjust min_count as you want in `ft.py`.

## Download pre-trained model
[click here](https://drive.google.com/open?id=1ED7o_h3KO3fKcDSRHXiuAFL3fxEM5z78) (Vector size: 300, Vocabulary size: 92056)

## References
- [Kyubyong/wordvectors](https://github.com/Kyubyong/wordvectors)
- [mecab-ipadic-NEologd](https://github.com/neologd/mecab-ipadic-neologd)
- [fastText](https://github.com/facebookresearch/fastText)
- [fastText.py](https://github.com/salestock/fastText.py)
- [MeCab](http://taku910.github.io/mecab/)
