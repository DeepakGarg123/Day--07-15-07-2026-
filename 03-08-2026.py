# Exercise 1: Resume Keyword Analyzer
# Create a program that:

# Takes a resume text as input
# Converts it to lowercase
# Tokenizes words
# Removes stopwords
# Displays:
# Total words
# Unique words
# Top 10 most frequent words

# Expected Skills:

# Tokenization
# Stopwords
# Vocabulary

text = input("enter text:")
print(text.lower())
print(len(text))

# Exercise 2: News Article Cleaner
# Given a paragraph copied from a news website:
# Perform:

# Lowercasing
# Remove punctuation
# Tokenization
# Stopword removal
# Display final cleaned text.
# Expected Skills:

# NLP preprocessing pipeline


# Exercise 3: Build Vocabulary Generator
# Input:
# 3 documents from user.
# Output:

# Vocabulary:
# ["python","machine","learning","nlp",...]Also display:

# Total Vocabulary SizeExpected Skills:

# Corpus
# Vocabulary

text = input("enter 1st sentence:")
text1 = input("enter 2nd sentence:")
text2 = input("enter 3rd sentence:")
Corpus = 
# Exercise 4: Manual BoW Generator
# Without CountVectorizer.
# Input:

# doc1 = "I love NLP"
# doc2 = "NLP is amazing"
# doc3 = "I love coding"Generate BoW table manually using Python.
# Expected Skills:

# Vocabulary
# Frequency counting


# Exercise 5: Similarity Finder using BoW
# Input:
# 5 documents.
# Convert them into BoW vectors.
# Find:
# Most Similar Document Pairusing cosine similarity.
# Expected Skills:

# Vectorization
# Similarity


# Exercise 6: TF-IDF Keyword Extractor
# Input:
# 5 documents.
# Apply TF-IDF.
# For every document display:

# Top 3 Most Important WordsExpected Skills:

# TF-IDF understanding


# Exercise 7: Spam Keyword Detector
# Dataset:
# Create 20 messages manually.
# Example:
# Win Money Now

# Meeting at 5 PMUse:

# BoW
# TF-IDF
# Find words with highest importance.
# Determine:
# Which words strongly indicate spam?Expected Skills:

# NLP + Business Thinking


# Exercise 8: Job Description Analyzer
# Input:
# A software engineer job description.
# Tasks:

# Clean text
# Remove stopwords
# Generate TF-IDF
# Extract top 15 keywords
# Output:
# Top Skills RequiredExpected Skills:

# Real-world NLP