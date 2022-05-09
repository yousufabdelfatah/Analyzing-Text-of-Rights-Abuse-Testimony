import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import string
import re
from sklearn.feature_extraction.text import CountVectorizer
import arabic_reshaper
from bidi.algorithm import get_display
from ar_wordcloud import ArabicWordCloud
import matplotlib.pyplot as plt
import nltk
from snowballstemmer import stemmer

testimonies = pd.read_csv("Data/testimonies.csv")

# change from object type to string type
testimonies['أقوال بالتعرض للتعذيب'] = testimonies['أقوال بالتعرض للتعذيب'].astype(str)

# data cleaning
# this can be accomplished with camel-tools package but this way gives me a little bit more control over
# exactly what changes I make to the text
arabic_punctuations = '''`÷×؛<>_()*&^%][ـ،/:"؟.,'{}~¦+|!”…“–ـ'''
english_punctuations = string.punctuation
punctuations_list = arabic_punctuations + english_punctuations

arabic_diacritics = re.compile("""
                             ّ    | # Tashdid
                             َ    | # Fatha
                             ً    | # Tanwin Fath
                             ُ    | # Damma
                             ٌ    | # Tanwin Damm
                             ِ    | # Kasra
                             ٍ    | # Tanwin Kasr
                             ْ    | # Sukun
                             ـ     # Tatwil/Kashida
                        #  """, re.VERBOSE)

# this helps with "orthofrpahic ambiguity by dealing with spelling inconsistencies"
def normalize_arabic(text):
    text = re.sub("[إأآا]", "ا", text)
    text = re.sub("ى", "ي", text)
    text = re.sub("ؤ", "ء", text)
    text = re.sub("ئ", "ء", text)
    text = re.sub("ة", "ه", text)
    text = re.sub("گ", "ك", text)
    return text


def remove_diacritics(text):
    text = re.sub(arabic_diacritics, '', text)
    return text


def remove_punctuations(text):
    translator = str.maketrans('', '', punctuations_list)
    return text.translate(translator)


def remove_repeating_char(text):
    return re.sub(r'(.)\1+', r'\1', text)

testimonies = testimonies["أقوال بالتعرض للتعذيب"].apply(normalize_arabic)\
    .apply(remove_diacritics).\
        apply(remove_punctuations).\
            apply(remove_repeating_char)

stopwords = open('Arabic_Stop.txt', "r")
stopwords = stopwords.read().replace('\n', ' ').split(' ')
len(stopwords)

stopwords = [normalize_arabic(item) for item in stopwords]
stopwords = [remove_diacritics(item) for item in stopwords]
stopwords = [remove_punctuations(item) for item in stopwords]
stopwords = [remove_repeating_char(item) for item in stopwords]

# Create tokenizer that includes lemmatizations
# tokenize with a regular expression to limit just to useful english words

class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`']
    def __init__(self):
        self.ar = stemmer("arabic")
    def __call__(self, doc):
        return [self.ar.stemWord(t) for t in nltk.tokenize.word_tokenize(doc) if t not in self.ignore_tokens]
    
tokenizer=LemmaTokenizer()

vectorizer = CountVectorizer(stop_words= stopwords, # lemmatized stop words list
                    lowercase=True, # make everything lower case
                    tokenizer = tokenizer, # tokenizer we created above
                    ngram_range=(1,2), # return bigrams and unigrams
                    min_df=5, # ignore words that appear in less than 5 documents
                    max_df=0.8) # ignore words that appear in more than 80% of documents

# lemmatize the stopwords list
stopwords = tokenizer(' '.join(stopwords))

X = vectorizer.fit_transform(testimonies)

dtm = vectorizer.transform(testimonies)

dtm = pd.DataFrame(dtm.toarray(), columns = vectorizer.get_feature_names())

freq = dtm.sum(axis = 0).sort_values(ascending = False)

awc = ArabicWordCloud(background_color="black")

freq = pd.Series(freq, name = "Number")

freq = freq[1:20]

dict = freq.to_dict()

dict_wc = awc.from_dict(dict, ignore_stopwords=True)
awc.plot(dict_wc, width=15, height=15)

freq_index_fixed = []

for i in list(freq.index.astype(str)):
    x = arabic_reshaper.reshape(i)
    y = get_display(x)
    freq_index_fixed.append(y)

# keywords barchart
plt.rcParams["figure.figsize"] = (15,10)
plt.bar(freq_index_fixed, freq.values)

