from gensim.models import Word2Vec

sentences = [
    ["i", "love", "playing", "cricket"],
    ["i", "love", "playing", "football"],
    ["i", "love", "watch", "cricket"],
    ["i", "love", "watch", "football"]
]

model = Word2Vec(sentences=sentences, vector_size=100, window=2, min_count=1, sg=0)

print("Vector for 'cricket':", model.wv["cricket"])
print("Most similar to 'cricket':", model.wv.most_similar("cricket"))
print
