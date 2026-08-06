# from sklearn.feature_extraction.text import CountVectorizer
# documents = [
#     "Python is easy",
#     "I love Python",
#     "Python is powerful"
# ]
# model = CountVectorizer(stop_words="english")
# X = model.fit_transform(documents)
# print(model.get_feature_names_out())
# Counts = X.toarray().sum(axis = 0)
# print(Counts)

# from sklearn.feature_extraction.text import TfidfVectorizer
# resume = """
# Python SQL Machine Learning Deep Learning NLP
# """

# job_description = """
# Looking for a Python Developer with SQL,
# Machine Learning, Deep Learning and NLP skills.
# """
# model = TfidfVectorizer()
# X = model.fit_transform([resume , job_description])
# print(model.get_feature_names_out())
# print(X.toarray())


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
resume = """
Python SQL Machine Learning Deep Learning NLP
"""

job_description = """
Looking for a Python Developer with SQL,
Machine Learning, Deep Learning and NLP skills.
"""
model = TfidfVectorizer(stop_words="english")
X  = model.fit_transform([resume , job_description])
print(model.get_feature_names_out())
similarity  = cosine_similarity(X)
print(similarity)
print(X.toarray())