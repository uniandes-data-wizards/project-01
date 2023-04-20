from sklearn.base import BaseEstimator, TransformerMixin
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from nltk.stem import LancasterStemmer, WordNetLemmatizer
import re

stop_words = set(stopwords.words('spanish'))

class Preprocessor(BaseEstimator, TransformerMixin):
    def __init__(self):
        pass
    
    def fit(self, X, y=None):
        return self

    def transform(self, X):
        def clean_text(text):
            words = word_tokenize(str(text))
            words = self.to_lowercase(words)
            words = self.replace_numbers(words)
            words = self.remove_punctuation(words)
            words = self.remove_non_ascii(words)
            words = self.remove_stopwords(words)
            words = self.stem_and_lemmatize(words)
            return ' '.join(words)
        
        cleaned_X = X.apply(clean_text)

        return cleaned_X

    def remove_non_ascii(self, words):
        return [word.encode('utf-8', 'ignore').decode('utf-8', 'ignore') for word in words]
    
    def to_lowercase(self, words):
        return [word.lower() for word in words]

    def remove_punctuation(self, words):
        return [re.sub(r'[^\w\s]', '', word) for word in words if re.sub(r'[^\w\s]', '', word) != '']

    def replace_numbers(self, words):
        return [re.sub(r'\d+', '', word) for word in words if re.sub(r'\d+', '', word) != '']

    def remove_stopwords(self, words):
        return [word for word in words if word not in stop_words]

    def stem_words(self, words):
        stemmer = LancasterStemmer()
        return [stemmer.stem(word) for word in words]

    def lemmatize_verbs(self, words):
        lemmatizer = WordNetLemmatizer()
        return [lemmatizer.lemmatize(word, pos='v') for word in words]

    def stem_and_lemmatize(self, words):
        stems = self.stem_words(words)
        lemmas = self.lemmatize_verbs(words)
        return stems + lemmas

    # New method to encode sentimiento
    def encode_sentiment(self, sentiment):
        if sentiment == 'positivo':
            return 1
        else:
            return 0
