"""Exercise 1: Load and Explore the Dataset
Dataset: spam.csv
Task:

Load the dataset using Pandas.
Display:
Shape of the dataset
Column names
First 5 rows
Count of Spam and Ham (Non-Spam messages).

Expected Output:

Dataset information and category distribution.

import pandas as pd
df = pd.read_csv("spam_dataset.csv")
print(df.shape)
print(df.columns)
print(df.head(5))
print(df["label"].value_counts())
"""



"""Exercise 2: Text Cleaning
Task:
Create a function clean_text() that:

Converts text to lowercase.
Removes email addresses.
Removes numbers.
Removes special characters and punctuation.
Removes extra spaces.
Apply the function to the message column and create a new column named cleaned_message.
Print:

Original message
Cleaned message

import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords
df = pd.read_csv("spam_dataset.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\S+@\S+","",text)
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    text = re.sub(r"\s+","",text)
    return text
df["cleaned_message"] = df["message"].apply(clean_text)
print("Original Message:\n")
print(df["message"])
print("cleaned message:\n")
print(df["cleaned_message"])
"""



# Exercise 3: Tokenization
# Task:

# Create a function tokenize_text() that splits the cleaned message into individual words.
# Store the output in a new column named tokens.
# Print:
# Total number of tokens in the first message.
# First 20 tokens of the first message.


import pandas as pd
import re
from nltk.corpus import stopwords
df = pd.read_csv("spam_dataset.csv")
print(df.head())
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\S+@\S+","",text)
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    text = re.sub(r"\s+"," ",text).strip()
    return text
def tokenize_text(text):
    return text.split()
df["cleaned message"] = df["message"].apply(clean_text)
df["tokens"] = df["cleaned message"].apply(tokenize_text)
print("Total number of Tokens:" , len(df["tokens"].iloc[0]))
print("First 20 tokens:",df["tokens"].iloc[0][:20])



# Exercise 4: Stopword Removal
# Task:

# Load English stopwords from NLTK.
# Create a function remove_stopwords().
# Remove stopwords from the tokens column.
# Store the result in a new column named tokens_after_stopwords.
# Print:
# Number of tokens before stopword removal.
# Number of tokens after stopword removal.
# First 20 tokens after stopword removal




import pandas as pd
import re
from nltk.corpus import stopwords
df = pd.read_csv("spam_dataset.csv")
print(df.head())
def clean_text(text):
    text = str(text).lower()
    text = re.sub(r"\S+@\S+","",text)
    text = re.sub(r"\d+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    text = re.sub(r"\s+"," ",text).strip()
    return text
def tokenize_text(text):
    return text.split()
df["cleaned message"] = df["message"].apply(clean_text)
df["tokens"] = df["cleaned message"].apply(tokenize_text)
print("Total number of Tokens:" , len(df["tokens"].iloc[0]))
print("First 20 tokens:",df["tokens"].iloc[0][:20])
stopwords = set(stopwords.words("english"))
def remove_stopwords(tokens):
    return[word for word in tokens if word not in stopwords]
df["tokens_after_stopwords"] = df["tokens"].apply(remove_stopwords)
print("tokens before stopword removal:")
print(len(df["tokens"].iloc[0]))
print("tokens after stopword removal:")
print(df["tokens_after_stopwords"].iloc[0][:20])


