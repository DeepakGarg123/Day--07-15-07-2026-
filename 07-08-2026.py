# Exercise 1: Load and Explore the Dataset
# Dataset: news category
# Task

# Load the dataset using Pandas.
# Display:
# Shape of the dataset
# Column names
# First 5 rows
# Last 5 rows

# Check for:
# Missing values
# Duplicate rows

# Display the number of news articles in each category.

import pandas as pd
import re
df = pd.read_csv("news.csv" , sep='\t')
print(df.head())
print(df.shape)
print(df.columns)
print(df.tail())
print(df.isnull().sum())
print(df.duplicated())
print(df["Category"].value_counts())
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\S+@+\S+","",text)
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    text = re.sub(r"\s+"," ",text)
    return text
df["cleaned_text"] = df["News"].apply(clean_text)

print(df[["News", "cleaned_text"]].head())
from nltk.tokenize import word_tokenize
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
def tokenize_text(text):
    tokens = word_tokenize(text)
    return tokens
df["tokenization"] = df["cleaned_text"].apply(tokenize_text)
print(df[["cleaned_text" , "tokenization"]].head())
from nltk.corpus import stopwords
nltk.download("stopwords")
stopwords = set(stopwords.words('english'))
def remove_stopwords(tokens):
    filterd_tokens = []
    for word in tokens:
        if word not in stopwords:
            filterd_tokens.append(word)
    return filterd_tokens
df["removed stopwords"] = df["tokenization"].apply(remove_stopwords)
print(df[["tokenization" , "removed stopwords"]].head())
from nltk.stem import WordNetLemmatizer
def lemmatization(filterd_tokens):
    lemmatized_tokens = []
    model = WordNetLemmatizer()

    for word in filterd_tokens:
        lemma = model.lemmatize(word)
        lemmatized_tokens.append(lemma)

    return lemmatized_tokens
    
df["lemmatized_words"] = df["removed stopwords"].apply(lemmatization)

print(df[["removed stopwords", "lemmatized_words"]].head())

def create_final_text(lemmatized_tokens):
    return " ".join(lemmatized_tokens)
df["final_text"]  =df["lemmatized_words"].apply(create_final_text)
print(df[["lemmatized_words" , "final_text"]].head())

from sklearn.feature_extraction.text import TfidfVectorizer
model = TfidfVectorizer(
    max_features=3000,
    min_df=1,
    max_df=1.0,
    ngram_range=(1,2)
)
X = model.fit_transform(df["final_text"])
y = df["Category"]
print(X.shape)
print(model.get_feature_names_out()[:20])
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test  =train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(
    class_weight="balanced"
    max_iter=10000
)
model.fit(X_train , y_train)
y_pred  = model.predict(X_test)

