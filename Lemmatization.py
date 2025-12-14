#  NLTK Library - Lemmetization
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
import nltk

# Download required resources
nltk.download('wordnet')
nltk.download('punkt')
nltk.download('omw-1.4')

def lemmatization_fun1():
# Sample text
    text = "Running ran runs easily and quickly."

    # Tokenization of corpus
    words = word_tokenize(text)
    print(f"Tokenize Words : {words}")

    # Apply Lemmatization
    lemmatize = WordNetLemmatizer() #creating object
    lemmatize_words = [lemmatize.lemmatize(word,pos=wordnet.VERB)for word in words ]
    print("\n Lemmatized words: ",lemmatize_words)

def lemmatization_fun2():
    # A sentiment analysis system needs to normalize customer reviews for consistent analysis.
    reviews = ["The cats were running around.","A better solution was provided."]
    lemmatize_reviews = []
    lemmatize = WordNetLemmatizer()

    for review in reviews:
        words = word_tokenize(review)
        lemmatize_words = [lemmatize.lemmatize(word,pos = wordnet.VERB)for word in words]
        lemmatize_reviews.append(" ".join(lemmatize_words))

    print("\n row Reviews:",reviews)
    print("\n Lemmatize Reviews:",lemmatize_reviews)

lemmatization_fun2()