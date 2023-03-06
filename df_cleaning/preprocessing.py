# imports
import re
import string
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from wordcloud import STOPWORDS, WordCloud
from emot.emo_unicode import UNICODE_EMOJI
from sklearn.base import BaseEstimator, TransformerMixin
from PIL import Image

class LowerCase(BaseEstimator, TransformerMixin):
    '''
    Turns X['Lyric'] into lowercase X['Lyric']
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['Lyric'] = X['Lyric'].str.lower()
        return pd.DataFrame(X)

class RegexRemover(BaseEstimator, TransformerMixin):
    '''
    Class to remove #'s and repeating characters
    '''

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['Lyric'] = X['Lyric'].apply(
            lambda x: re.sub(r'#[A-Za-z0-9]+', '', str(x)))
        X['Lyric'] = X['Lyric'].apply(
            lambda x: re.sub(r'#', '', str(x)))
        X['Lyric'] = X['Lyric'].apply(
            lambda x:re.sub(r'\@\w+|\#\w+|\d+','', str(x)))

        return pd.DataFrame(X)

class NumRemover(BaseEstimator, TransformerMixin):
    '''
    Removes digits from text
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['Lyric']  = X['Lyric'] .apply(
            lambda x: ''.join(char for char in x if not char.isdigit()))
        return pd.DataFrame(X)

class PuncRemover(BaseEstimator, TransformerMixin):
    '''
    Removes punctuation from text
    '''
    def __init__(self, extra_chars='“”‘’-'):
        self.extra_chars = extra_chars
        self.punctuation = string.punctuation + self.extra_chars
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        for punc in self.punctuation:
            X['Lyric'] = X['Lyric'].str.replace(punc, '')
        return pd.DataFrame(X)

class Lemmatizer(BaseEstimator, TransformerMixin):
    '''
    Performs standard lemmatizing on words and removes words that are shorter than 3 characters
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        lemmatizer = WordNetLemmatizer()
        X['Lyric'] = X['Lyric'].apply(
            lambda x: ' '.join(lemmatizer.lemmatize(word) for word in str(x).split(' ')
                               if len(lemmatizer.lemmatize(word))>2))
        return pd.DataFrame(X)

class WordRemover(BaseEstimator, TransformerMixin):
    '''
    Removes words from text
    '''

    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        def remove_stopw(text):
            word_tokens = word_tokenize(text)

            stop_words = list(stopwords.words('english'))
            emoji = list(UNICODE_EMOJI.keys())
            manual_sw = ["n't", '내', '너의', '난', '날', '내가', '너','나', '그', '니', '걸', '거야'
             '널', '네', '니가', '네가', '널', '너를', '넌', '내게', '이', 'l', 'u', '-',
            'na', 'ah', 'e','m', 'uh', 'eh', 's', 'la', 'a', 'o', 'ta', 't', 'oh', 'du', 'yeah', '’']
            removal = stop_words + emoji + manual_sw

            return ' '.join(w for w in word_tokens if not w in removal)

        X['Lyric'] = X['Lyric'].apply(remove_stopw)

        return pd.DataFrame(X)

class WordSplitter(BaseEstimator, TransformerMixin):
    '''
    Splits full_transcript into 'full_words' using .split()
    Then creates a new columns called 'num_words' that counts the 'full_words'
    '''
    def fit(self, X, y=None):
        return self

    def transform(self, X, y=None):
        X['full_words'] = X['Lyric'].str.split()
        X['num_words'] = X['full_words'].str.len()
        return pd.DataFrame(X)
