
import pandas as pd
import pandas as pd
import numpy as np

data = pd.read_csv("./data/Products.csv", lineterminator='\n')

data



from nltk.corpus import stopwords
import string
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer



porter = PorterStemmer()
def tokinize_stemmer(words):
    """
    Take a string of text and tranform to root word
    """
    return [porter.stem(word) for word in words.split()]



def text_process(mess):
    """
    Takes in a string of text, then performs the following:
    1. Remove all punctuation
    2. Remove all stopwords
    3. Returns a list of the cleaned text
    """
    # Check characters to see if they are in punctuation
    nopunc = [char for char in mess if char not in string.punctuation]

    # Join the characters again to form the string.
    nopunc = ''.join(nopunc)
    
    # Now just remove any stopwords
    return [word for word in tokinize_stemmer(nopunc) if word.lower() not in stopwords.words('english')]