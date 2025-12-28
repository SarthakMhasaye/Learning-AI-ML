# NLTK Library - stop word
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

import nltk
nltk.download("stopwords")
nltk.download("punkt")

# Sample text
sentence = "Green power installation startup solar square increase $40 in series B"

# Word tokenization
tokens = word_tokenize(sentence)
print(f" \n Tokens : {tokens}\n")

#  remove the stop word
# Get the english stop word

stop_word = set(stopwords.words('english'))
# print(f"\n Total stop words : {stop_word} \n")

token_without_stopword = [word for word in tokens if word.lower() not in stop_word]
print(token_without_stopword)