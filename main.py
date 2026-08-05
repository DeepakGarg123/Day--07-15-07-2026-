# text = "I LOVE Machine Learning"
# text = text.lower()
# tokens = text.split()
# stopwords = ["i"]
# clean_sentence = []
# for word in tokens:
#     if word not in stopwords:
#         clean_sentence.append(word)
# print(clean_sentence)



# from nltk.stem import PorterStemmer
# stemmer  =PorterStemmer()
# print(stemmer.stem("Playing"))
# print(stemmer.stem("Played"))
# print(stemmer.stem("Plays"))
# print(stemmer.stem("Player"))

# import nltk
# nltk.download("wordnet")
# nltk.download("omw-1.4")
# from nltk.stem import WordNetLemmatizer
# Lemmatizer = WordNetLemmatizer()
# print(Lemmatizer.lemmatize("Playing" , pos="v"))
# print(Lemmatizer.lemmatize("Plays" , pos="v"))
# print(Lemmatizer.lemmatize("studies" , pos="v"))
# print(Lemmatizer.lemmatize("Player" , pos="v"))
# print(Lemmatizer.lemmatize("better" , pos="v"))


# from sklearn.feature_extraction.text import CountVectorizer
# corpus =[
#     "Machine Learning",
#     "Python Machine",
#     "Python Learning"
# ]
# vectorizer = CountVectorizer()
# X  =vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names_out())
# print(X.toarray)


# import pandas as pd
# from sklearn.feature_extraction.text import CountVectorizer
# df = pd.read_csv("Spam_dataset.csv")
# print(df.head())
# X = df["Email"]
# y = df["Spam"]
# vectorizer = CountVectorizer()
# X = vectorizer.fit_transform(X)
# print(vectorizer.get_feature_names_out())
# print(X.toarray())
# from sklearn.model_selection import train_test_split
# X_train , X_test , y_train , y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression()
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_email = ["Congratulations you have won a lottery claim tomorrow"]
# new_email_vectorized  = vectorizer.transform(new_email)
# prediction = model.predict(new_email_vectorized)
# print("email is spam or not:" , prediction)
# from sklearn.metrics import accuracy_score , recall_score , precision_score , f1_score
# print("accuracy score:" , accuracy_score(y_test , y_pred))
# print("recall score:" , recall_score(y_test , y_pred))
# print("precision score:" , precision_score(y_test , y_pred))
# print("f1 score:" , f1_score(y_test , y_pred))






