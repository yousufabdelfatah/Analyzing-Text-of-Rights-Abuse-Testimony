import gensim
import re
import spacy
from bertopic import BERTopic
from flair.embeddings import TransformerDocumentEmbeddings
import pandas as pd
import yaml

# Load AraVec model from gensim    
#model = gensim.models.Word2Vec.load("full_grams_cbow_300_twitter/full_grams_cbow_300_twitter.mdl")
#model.wv.save_word2vec_format("model.txt")

# using `gzip` to compress the .txt file
#!gzip model.txt
#!python -m spacy init vectors ar model.txt.gz output/

testimonies = pd.read_csv("Data/testimonies.csv")

# for experimentation
with open("params.yaml", "r") as fd:
    params = yaml.safe_load(fd)
    
ngrams = params["preprocessing"]["ngrams"]

# model = spacy.load("output/")

#topic_model = BERTopic(embedding_model=model)

# topics, probabilities = topic_model.fit_transform(testimonies)

# print the topics
# topic_model.get_topic_info()

# AraVec doesn't work well but what if we use Arabert
arabert = TransformerDocumentEmbeddings('aubmindlab/bert-base-arabertv02')

topic_model2 = BERTopic(embedding_model=arabert, n_gram_range=(ngrams["smallest"], ngrams["largest"]))

testimonies['أقوال بالتعرض للتعذيب'] = testimonies['أقوال بالتعرض للتعذيب'].astype(str)

topics, probabilities = topic_model2.fit_transform(list(testimonies['أقوال بالتعرض للتعذيب']))

# print the topics to json
topic_model2.get_topic_info()

# save the model
topic_model2.save("arabert_model")

