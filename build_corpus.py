# coding: utf-8
#!/usr/bin/python2
import argparse
import codecs
import lxml.etree as ET
import os
import regex

# arguments setting
parser = argparse.ArgumentParser()
parser.add_argument('--lcode', help='ISO 639-1 code of target language. See `lcodes.txt`.')
parser.add_argument('--max_corpus_size', type=int, default=1000000000, help='the maximum size of the corpus. Feel free to adjust it according to your computing power.')
args = parser.parse_args()

lcode = args.lcode
if lcode == 'ja':
    import MeCab # See https://pypi.python.org/pypi/mecab-python/0.996
    mecab = MeCab.Tagger("-Owakati")
    print "mecab succesfuly loaded!"
else:
    raise ValueError("DataIsNotJapanese")

max_corpus_size = args.max_corpus_size
fname = "{}wiki-20170820-pages-articles-multistream.xml".format(lcode) # change this (date) according to the name of the file you downloaded.

def clean_text(text):
    global lcode

    # Common
    text = regex.sub("(?s)<ref>.+?</ref>", "", text) # remove reference links
    text = regex.sub("(?s)<[^>]+>", "", text) # remove html tags
    text = regex.sub("&[a-z]+;", "", text) # remove html entities
    text = regex.sub("(?s){{.+?}}", "", text) # remove markup tags
    text = regex.sub("(?s){.+?}", "", text) # remove markup tags
    text = regex.sub("(?s)\[\[([^]]+\|)", "", text) # remove link target strings
    text = regex.sub("(?s)\[\[([^]]+\:.+?]])", "", text) # remove media links

    text = regex.sub("[']{5}", "", text) # remove italic+bold symbols
    text = regex.sub("[']{3}", "", text) # remove bold symbols
    text = regex.sub("[']{2}", "", text) # remove italic symbols

    if lcode in ['ja']: # japanese
        text = regex.sub(u"[^\r\n\p{Han}\p{Hiragana}\p{Katakana}ー。！？]", "", text)
    else:
        raise ValueError("DataIsNotJapanese")

    # Common
    text = regex.sub("[ ]{2,}", " ", text) # Squeeze spaces.
    return text

def sentence_segment(text):
    '''
    Args:
      text: A string. A unsegmented paragraph.

    Returns:
      A list of sentences.
    '''
    global lcode
    if lcode in ['ja']:
        sents = regex.split(u"([。！？])?[\n]+|[。！？]", text)
    else:
        raise ValueError("DataIsNotJapanese")
    return sents

def word_segment(sent):
    '''
    Args:
      sent: A string. A sentence.

    Returns:
      A list of words.
    '''
    global lcode
    if lcode in ['ja']:
        words = mecab.parse(sent.encode('utf8')).split()
    else: # Mostly european languages
        raise ValueError("DataIsNotJapanese")

    return words

def build_corpus():
    global lcode, max_corpus_size, fname
    with codecs.open("data/{}.txt".format(lcode), 'w', 'utf-8') as fout:
        i = 1
        j = 1
        ns = "{http://www.mediawiki.org/xml/export-0.10/}" # namespace
        for _, elem in ET.iterparse("data/{}".format(fname), tag=ns+"text"):
            running_text = elem.text
            try:
                running_text = clean_text(running_text)
                sents = sentence_segment(running_text)
                for sent in sents:
                    if sent is not None:
                        words = word_segment(sent)
                        if len(words) > 10:
                            if lcode in ['ja']:
                                fout.write(" ".join(words).decode('utf8') + "\n")
                            else:
                                fout.write(" ".join(words) + "\n")

            except:
                continue # it's okay as we have a pretty big corpus!
            elem.clear() # We need to save memory!
            if i % 1000 == 0:
                print i,
                fsize = os.path.getsize("data/{}.txt".format(lcode))
                if fsize > max_corpus_size:
                    break
            i += 1

if __name__ == "__main__":
    build_corpus()

    print "Done"
