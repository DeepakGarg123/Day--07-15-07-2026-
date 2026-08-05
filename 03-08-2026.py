# Exercise 2: Bag of Words using CountVectorizer
# documents = [
#     "I love NLP and Machine Learning",
#     "Machine Learning is amazing",
#     "I love learning new things"
# ]
# Tasks

# Apply CountVectorizer.
# Print vocabulary.
# Print BoW matrix.
# Convert sparse matrix into array.


from sklearn.feature_extraction.text import CountVectorizer
documents = [
    "I love NLP and Machine Learning",
    "Machine Learning is amazing",
    "I Love learning new things"
]
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(X.toarray())


# Exercise 3: TF-IDF Vectorizer
# Input
# Use the same documents from Exercise 2.
# Tasks

# Apply TfidfVectorizer.
# Print vocabulary.
# Print TF-IDF matrix.
# Convert matrix into array.

from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "I love NLP and Machine Learning",
    "Machine Learning is amazing",
    "I Love learning new things"
]
vectorizer = TfidfVectorizer()
tfidf = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(tfidf.toarray())


from sklearn.feature_extraction.text import TfidfVectorizer
documents = [
    "Python is a popular programming language used for machine learning",
    "Machine learning uses Python and data science techniques",
    "Deep learning and artificial intelligence are transforming technology",
    "Python is widely used for artificial intelligence and data analysis",
    "Data science includes statistics machine learning and visualization"
]
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(documents)
print(vectorizer.get_feature_names_out())
print(X.toarray())


# Exercise 4: Document Similarity using Cosine Similarity
# text1 = "I love NLP"
# text2 = "I enjoy NLP and text processing"
# Tasks

# Convert both texts into TF-IDF vectors.
# Calculate cosine similarity.
# Print similarity score.


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text1 = "I love NLP"
text2 = "I enjoy NLP and text processing"
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([text1 , text2])
print(vectorizer.get_feature_names_out(X))
similarity = cosine_similarity(X)
print(similarity)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
Resume  = "Python Machine Learning SQL Deep Learning NLP"
Job_Description= "Looking for a Python developer with Machine Learning NLP SQL and Deep Learning skills."
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform([Resume , Job_Description])
print(vectorizer.get_feature_names_out(X))
similarity = cosine_similarity(X)
print(similarity)

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
text1 = "I love NLP"
text2 = "I enjoy NLP and text processing"
doc1 = "Python is a popular programming language used for machine learning"
doc2 = "Machine learning uses Python and data science techniques"
doc3 = "Deep learning and artificial intelligence are transforming technology"
vectorizer = CountVectorizer()
X = vectorizer.fit_transform([text1 , text2 , doc1 , doc2 , doc3])
print(vectorizer.get_feature_names_out())
similarity = cosine_similarity(X)
print(similarity)


