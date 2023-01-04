import re
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
factory = StemmerFactory()
stemmer = factory.create_stemmer()

stopwords_path = r'data/stopword_indonesia.txt'


def load_stopwords():
    with open(stopwords_path) as f:
        teks = f.readlines()
    f.close()
    stopwords_indo = [x.replace('\n', '') for x in teks]

    return stopwords_indo


def text_cleaning(text):
    # Removing extra new lines / tabs / period / all text mark and emoticon
    result = text.lower()
    result = result.replace('-', ' ')
    result = result.replace('+', ' ')
    result = result.replace('..', ' ')
    result = result.replace('.', ' ')
    result = result.replace(',', ' ')
    result = result.replace('\n', ' ')
    result = re.findall('[a-z\s]', result, flags=re.UNICODE)  # remove emoticon
    result = "".join(result)
    final = " ".join(result.split())

    return final


def manual_stopwords_remover(text):
    all_stopwords = load_stopwords()
    teks = text.split(' ')
    teks = [w for w in teks if w not in all_stopwords]
    teks = " ".join(teks)
    return teks


def brand_remover(text):
    brand_and_other_words = ['mie', 'danone',
                             'indomie', 'aqua', 'salted', 'egg', 'aja', 'gak']
    teks = text.split(' ')
    teks = [w for w in teks if w not in brand_and_other_words]
    teks = " ".join(teks)
    return teks


def word_stemming(text):
    return stemmer.stem(text)


def preprocessed_data(teks):
    hasil = text_cleaning(teks)
    hasil = manual_stopwords_remover(hasil)
    hasil = brand_remover(hasil)
    hasil = word_stemming(hasil)

    return hasil
