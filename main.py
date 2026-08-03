# def add (a,b):
#     return a+b
# def sub (a,b):
#     return a-b
# def mult (a,b):
    # return a*b






# def calculate(price, tax=18):
#     return price + tax
# calculate()

# a = [10, 20, 30]
# b = a
# a = a + [40]
# print(b)



# import numpy as np
# arr = np.array(
#     [45 , "Deepak" , 45.77]

# )
# print(np.ones(3,3))





import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
df = pd.read_csv("Spam_dataset.csv")
print(df.head())
X = df["Email"]
y = df["Spam"]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)
print(vectorizer.get_feature_names_out())
print(X.toarray())
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train , y_train)
y_pred  =model.predict(X_test)
new_email = ["Won lottery today"]
new_email_vectorized = vectorizer.transform(new_email)
prediction = model.predict(new_email_vectorized)
print("is spam or not:" , prediction)
from sklearn.metrics import accuracy_score ,recall_score , precision_score ,f1_score
print("accuracy score:" ,accuracy_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("f1 score:" ,f1_score(y_test , y_pred))

