import fasttext
model = fasttext.skipgram('data/ja.txt', 'data/ja_model', dim=300, min_count=50)
