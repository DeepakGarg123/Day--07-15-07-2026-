import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("Spam_dataset.csv")
X = df["Email"]
y=df["Spam"]
vectorizer  =CountVectorizer()
X = vectorizer.fit_transform(X)
print(vectorizer.get_feature_names_out())
print(X.toarray())
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test  =train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train ,y_train)
y_pred  =model.predict(X_test)
new_email  = ["Win lottery"]
vectorized_email = vectorizer.transform(new_email)
prediction = model.predict(vectorized_email)
print("email is spam or not:" , prediction)
from sklearn.metrics import accuracy_score  ,recall_score , precision_score , f1_score
print("accuracy score:" , accuracy_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))
print("f1 score:" , f1_score(y_test , y_pred))
print("precision score:" ,precision_score(y_test , y_pred))



import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("sentiment analysis.csv")
X = df["Review"]
y = df["Sentiment"]
vectorizer = CountVectorizer(stop_words="english" , lowercase=True)
X = vectorizer.fit_transform(X)
print(vectorizer.get_feature_names_out())
print(X.toarray())
from sklearn.model_selection import train_test_split
X_train , X_test , y_train  ,y_test  =train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=10000 , class_weight="balanced")
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_sentiment = ["The movie was not good at all, a complete waste."]
new_sentiment_vecotrized = vectorizer.transform(new_sentiment)
prediction = model.predict(new_sentiment_vecotrized)
print("is sentimented or not:", prediction)
from sklearn.metrics import accuracy_score , recall_score , f1_score , precision_score
print("accuracy score:" ,accuracy_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("f1 score:" , f1_score(y_test , y_pred))

