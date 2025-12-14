#  NLTK Library - Streaming
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
# Sample text
text = "Running ran runs easily and quickly."

# Tokenization of corpus
tokenize_words = word_tokenize(text)
print(f"Tokenize Words : {tokenize_words}")

# Apply stemming - Porter stemmer
porterStemmer = PorterStemmer()
porter_stemmed = [porterStemmer.stem(word) for word in tokenize_words]
print(f"\n Porter Stemmed Words : {porter_stemmed}")

# Apply stemming - Lanchaster stemmer
lancasterStemmer = LancasterStemmer()
lancaster_stemmed = [lancasterStemmer.stem(word) for word in tokenize_words]
print(f"\n Lanchaster Stemmed Words : {lancaster_stemmed}")