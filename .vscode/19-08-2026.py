# Q1. 
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize
# text = 'Python is easy to learn. NLP is interesting. AI is the future.'
# tokens = sent_tokenize(text)
# print(tokens)
# tokenizer = word_tokenize(text)
# print(tokenizer)
# print(len(tokens))
# print(len(tokenizer))

# Q2. 
# from nltk.tokenize import word_tokenize
# from collections import Counter
# text = 'Python is powerful and Python is easy. Python is popular.'
# print(text.lower())
# tokens = word_tokenize(text)
# print(tokens)
# frequency = Counter(tokens)
# print(frequency)

# Q3.
# from nltk.tokenize import word_tokenize
# text = 'Python 3.12 is amazing! I have 2 projects.'
# tokens = word_tokenize(text)
# print(tokens)
# Alpahbetic_tokens = [] 
# Numeric_Tokens = []
# special_character_tokens = []
# for token in tokens:
#     if token.isalpha():
#         Alpahbetic_tokens.append(token)
#     elif token.replace('.', "" , 1).isdigit():
#         Numeric_Tokens.append(token)
#     else:
#         special_character_tokens.append(token)

# print('Alphabetic:')
# print(Alpahbetic_tokens)
# print('Numeric:')
# print(Numeric_Tokens)
# print('special:')
# print(special_character_tokens)
        

# # Q4.
# from nltk.tokenize import word_tokenize
# text = "Machine Learning is changing the world in 2026!"
# tokens = word_tokenize(text)
# print(tokens)
# alphabetic_tokens = []
# numeric_tokens = []
# special_character_tokens = []
# Total_number_of_Tokens = len(tokens)
# print(Total_number_of_Tokens)
# unique_tokens = set(tokens)
# print(unique_tokens)
# for token in tokens:
#     if token.isalpha():
#         alphabetic_tokens.append(token)
#     elif token.isdigit():
#         numeric_tokens.append(token)
#     else:
#         special_character_tokens.append(token)
# print(len(alphabetic_tokens))
# print(len(numeric_tokens))
# print(len(special_character_tokens))
# print(tokens)

# Q5.

# from nltk.tokenize import word_tokenize
# def clean_tokens(text):
#     text = text.lower()
#     tokens = word_tokenize(text)
#     cleaned_tokens = []
#     for token in tokens:
#         if token.isalpha()and len(token)>=3:
#             cleaned_tokens.append(token)
#     return cleaned_tokens
# text = input("enter text:")
# result = clean_tokens(text)
# print(result)
        














# Q6.
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize
# from nltk.corpus import stopwords
# text = "Python is an amazing programming language!"
# sentences = sent_tokenize(text)
# print(sentences)
# words = word_tokenize(text)
# print(words)
# lowercase = text.lower()
# print(lowercase)
# cleaned_tokens = []
# for token in words:
#     if token.isalpha():
#         cleaned_tokens.append(token.lower())
# print(cleaned_tokens)
# stop_words = stopwords.words("english")
# final_tokens = []
# for word in cleaned_tokens:
#     if word not in stop_words:
#         final_tokens.append(word)
# print(final_tokens)

# Q7.

# from nltk.tokenize import word_tokenize
# text = "Hello, world! NLP is amazing. Python's power is incredible."
# split = text.split()
# print(split)
# print(len(split))
# tokens = word_tokenize(text)
# print(tokens)
# print(len(tokens))


# Q8.
import re
text = "I love #Python and #AI! Check https://example.com @student123 :blush:"
hashtags = re.findall(r"#\w+", text)
print(hashtags)
mentions = re.findall(r"@\w+", text)
print(mentions)
urls = re.findall(r"https?://\S+", text)
print(urls)

# Q10.



    