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
# text = "Machine Learning is changing the world in 2026 and in 20.37!"
# tokens = word_tokenize(text)
# print(tokens)
# alphabetic_tokens = []
# numeric_tokens = []
# special_character_tokens = []
# Total_number_of_Tokens = len(tokens)
# print(Total_number_of_Tokens)
# unique_tokens = set(tokens)
# print(unique_tokens)
# print(len(unique_tokens))
# for token in tokens:
#     if token.isalpha():
#         alphabetic_tokens.append(token)
#         print(alphabetic_tokens)
#     elif token.replace('.' , '' , 1).isdigit():
#         numeric_tokens.append(token)
#         print(numeric_tokens)
#     else:
#         special_character_tokens.append(token)
#         print(special_character_tokens)
# print(len(alphabetic_tokens))
# print(len(numeric_tokens))
# print(len(special_character_tokens))
# print(tokens)
# longest_token = max(tokens , key=len)
# print(longest_token)
# shortest_token = min(tokens , key = len)
# print(shortest_token)


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
# lowercase = []
# for word in words:
#     lowercase.append(word.lower())
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
 
# import re
# text = input("Enter text:")
# tokens = re.findall( r"https?://\S+|#\w+|@\w+|\d+(?:\.\d+)?|[A-Za-z]+|[^\w\s]" , text)
# print(tokens)
# Normal_words = []
# Hashtags = []
# Mentions = []
# URLs = []
# Numbers = []
# Special_characters_emojis = []
# for word in tokens:

#     if re.fullmatch(r"https?://\S+", word):
#         URLs.append(word)

#     elif re.fullmatch(r"#\w+", word):
#         Hashtags.append(word)

#     elif re.fullmatch(r"@\w+", word):
#         Mentions.append(word)

#     elif word.isalpha():
#         Normal_words.append(word)

#     elif word.replace(".", "", 1).isdigit():
#         Numbers.append(word)

#     else:
#         Special_characters_emojis.append(word)
# print(Normal_words)
# print(Numbers)
# print(URLs)
# print(Hashtags)
# print(Mentions)
# print(Special_characters_emojis)


#Q9. 
# words = [
#     "playing",
#     "unhappiness",
#     "internationalization",
#     "misunderstanding",
#     "machinelearning"
# ]

# subword_map = {
#     "playing": ["play", "ing"],
#     "unhappiness": ["un", "happy", "ness"],
#     "internationalization": ["international", "ization"],
#     "misunderstanding": ["mis", "understand", "ing"],
#     "machinelearning": ["machine", "learning"]
# }

# for word in words:

#     word_tokens = [word]
#     character_tokens = list(word)

#     subword_tokens = subword_map[word]

#     print("Original Word:", word)
#     print("Word Tokens:", word_tokens)
#     print("Character Tokens:", character_tokens)
#     print("Subword Tokens:", subword_tokens)


# #Q10.
# from nltk.tokenize import word_tokenize
# from nltk.tokenize import sent_tokenize
# from collections import Counter
# import string
# from nltk.corpus import stopwords
# text = input("Enter text:")
# sentences = sent_tokenize(text)
# print(len(sentences))
# tokens = word_tokenize(text)
# print(len(tokens))
# unique_tokens = set(tokens)
# print(len(unique_tokens))
# alphabetic_tokens = []
# numeric_tokens = []
# punctuation_tokens = []
# for word in tokens:
#     if word.isalpha():
#         alphabetic_tokens.append(word)
#     elif word.replace("." , "" , 1).isdigit():
#         numeric_tokens.append(word)
#     elif word in string.punctuation:
#         punctuation_tokens.append(word)

# print(len(alphabetic_tokens))
# print(len(numeric_tokens))
# print(len(punctuation_tokens))

# most_common_token = Counter(tokens)
# print(most_common_token.most_common(1))
# most_common_token = Counter(tokens)
# print(most_common_token.most_common(5))

# total_length = 0
# for token in tokens:
#     total_length = total_length+len(tokens)
# number_of_tokens = len(token)
# average_tokens = total_length/number_of_tokens
# print(average_tokens)

# longest_token = max(tokens , key=len)
# print(longest_token)
# shortest_token  = min(tokens , key=len) 
# print(shortest_token)

# stop_words = stopwords.words('english')
# stopwords_tokens = []
# for token in tokens:
#     if token.lower() in stop_words:
#         stopwords_tokens.append(token)
# print(len(stopwords_tokens))

# final_tokens = []
# for token in tokens:
#     if token.isalpha() and token not in stop_words:
#         final_tokens.append(token)
        
        





