import pandas as pd
import re
df = pd.read_csv("news.csv" , sep="\t")
print(df.head())
print(df.tail())
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\S+@\S+" ,"", text)
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    text = re.sub(r"\s+"," ",text).strip()
    return text
df["cleaned_text"]  =df["News"].apply(clean_text)
print(df[["News" , "cleaned_text"]].head())
from nltk.tokenize import word_tokenize
def tokenization(text):
    tokens = word_tokenize(text)
    return tokens
df["after tokenization"] = df["cleaned_text"].apply(tokenization)
print(df[["cleaned_text" , "after tokenization"]].head())
from nltk.corpus import stopwords
import nltk
nltk.download("stopwords")
stopwords = set(stopwords.words("english"))
def stopwords_removal(tokens):
    filtered_tokens = []
    for word in tokens:
        if word not in stopwords:
            filtered_tokens.append(word)
    return filtered_tokens
df["removed_stopwords"] = df["after tokenization"].apply(stopwords_removal)
print(df[["after tokenization" , "removed_stopwords"]].head())
from nltk.stem import WordNetLemmatizer
def lemmatization(filtered_tokens):
    model = WordNetLemmatizer()
    lemmatized_tokens = []
    for word in filtered_tokens:
        lemma = model.lemmatize(word)
        lemmatized_tokens.append(lemma)
    return lemmatized_tokens
df["after lemmatization"] = df["removed_stopwords"].apply(lemmatization)
print(df[["removed_stopwords" , "after lemmatization"]].head())
def final_text(lemmatized_tokens):
    return " ".join(lemmatized_tokens)
df["final_sentence"] = df["after lemmatization"].apply(final_text)
print(df[["after lemmatization" , "final_sentence"]].head())
from sklearn.feature_extraction.text import TfidfVectorizer
model = TfidfVectorizer(
    max_features=3000,
    min_df=1,
    max_df=1.0,
    ngram_range=(1,2)
)
X = model.fit_transform(df["final_sentence"])
y = df["Category"]
print(X.shape)
print(model.get_feature_names_out())
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(
    max_iter=10000,
    class_weight="balanced"
)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
print(y_test.head(10))
print(y_pred[:10])
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
print("accuracy score:",accuracy_score(y_test , y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))
print("f1_score:" , f1_score(y_test , y_pred))

    




