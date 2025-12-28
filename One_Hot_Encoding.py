# #  One Hot Encoding:-technique used to convert categorial data in a binary format that can
# #    be easily understand and processed by machine learning algorithm
# from sklearn.preprocessing import OneHotEncoder
# import numpy as np

# # Sample Data
# tokens = ["cat","dog","mouse"]

# words = np.array(tokens).reshape(-1,1)

# # initialize the ohe
# encoder = OneHotEncoder(sparse_output=False)
# one_hot_matrix = encoder.fit_transform(words)


# Practicle Example
# Spam detection model
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
# Step 1:- Collect sample sentence and labels
documents = [
    "Get reach wth the investment",
    "Important message regarding your account",
    "Your free coupan is waiting",
    "Congrats!!,for winning a lottery"
]

# Labels :- 1 for the spam and 0 for not spam
labels = [1,0,1,0]

# Step 2;_ One Hot Encoding :- convert text data into numerical form using one hot encoding

# initialize OHE
vectorizer = CountVectorizer(binary=True)
X = vectorizer.fit_transform(documents)

# Show the vocublary
print("\n Vocublary:",vectorizer.get_feature_names_out())

# Show the one hot encoded matrix
print("One hot encoded matrix:",)
# print(X.toarray())

# Step 3:- Model trainning
#  split data into trainning and testing

X_train,X_test,y_train,y_test = train_test_split(X,labels,test_size=0.2,random_state=42)
#  Traain a native bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train,y_train)

# Predict the labels of test
y_pred = classifier.predict(X_test)

# Evaluate the model
accuracyScore = accuracy_score(y_test,y_pred)
print("\n accuracy:",accuracyScore)

# Step 4:- Prediction
new_sentence = [
    "Free cash price waiting for you"
    "Important message regarding your account",
]

new_data = vectorizer.transform(new_sentence)

# Predict Category
predictData = classifier.predict(new_data)

for sentence,prediction in new_sentence,predictData:
    label = "Spam" if prediction == 1 else "Not Spam"
    print(f"Sentence: {sentence} -->Predicted:{label}")