#Q1.
# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# while True:
#     text = input("Enter text: ")
#     if text.lower() == "exit":
#         break
#     result = classifier(text)
#     sentiment = result[0]["label"]
#     confidence = result[0]["score"]
#     print(sentiment)
#     print(confidence)


#Q2.
# from transformers import pipeline

# reviews = [
#     "I love this movie.",
#     "This movie is terrible.",
#     "Amazing movie!",
#     "I hate this movie.",
#     "Very good experience."
# ]

# classifier = pipeline("sentiment-analysis")

# results = classifier(reviews)

# positive_count = 0
# negative_count = 0

# for i in range(len(results)):

#     result = results[i]

#     sentiment = result["label"]

#     confidence = result["score"] * 100

#     print( i + 1,  sentiment,  round(confidence, 2), "%")

#     if sentiment == "POSITIVE":
#         positive_count += 1

#     else:
#         negative_count += 1

# print("Total Positive Reviews:", positive_count)
# print("Total Negative Reviews:", negative_count)


# Q3. 
# from transformers import pipeline
# generator = pipeline('text-generation')
# result = generator(
#     "Python Programming is" , 
#     max_length = 50
# )
# print(result)

# Q4. 
# from transformers import pipeline
# classifier = pipeline('sentiment-analysis')
# generator = pipeline('text-generation')
# while True:
#     print("1. Sentiment Analysis")
#     print("2. Text Generation")
#     print("3. Exit")

#     choice = int(input("Enter your choice:"))
#     if choice==1:
#         text = input("Enter your text")
#         result = classifier(text)
#         print(result)
#     elif choice==2:
#         sentence = input("Enter your sentence:")
#         result = generator(sentence , max_length = 50)
#         print(result)
#     elif choice==3:
#         break
#     else:
#         print("please select an option from given menu")

# Q5
# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# results = []
# while True:
#     review = input("Enter review: ")
#     if review.lower() == "exit":
#         break
#     result = classifier(review)
#     sentiment = result[0]["label"]
#     confidence = result[0]["score"] * 100
#     results.append({
#         "review": review,
#         "sentiment": sentiment,
#         "confidence": confidence
#     })
# if len(results) > 0:
#     positive = 0
#     negative = 0
#     total_confidence = 0
#     for result in results:
#         print(result["review"])
#         print(result["sentiment"])
#         print(result["confidence"])

#         if result["sentiment"] == "POSITIVE":
#             positive += 1
#         else:
#             negative += 1
#         total_confidence += result["confidence"]
#     average_confidence = total_confidence / len(results)
#     print("Total Reviews:", len(results))
#     print("Positive:", positive)
#     print("Negative:", negative)
#     print("Average Confidence:", round(average_confidence, 2), "%")


# Q6.

# from transformers import pipeline
# generator = pipeline("text-generation")
# def blog_introduction():

#     topic = input("Enter topic: ")
#     prompt = "This blog is used to demonstrate " + topic
#     result = generator(prompt, max_length=100)
#     print(result[0]["generated_text"])

# def product_description():

#     product = input("Enter Product description: ")
#     prompt = "This product is about " + product
#     result = generator(prompt, max_length=100)
#     print(result[0]["generated_text"])


# def social_media_post():

#     post = input("Enter Social media post: ")
#     prompt = "Write a social media post about " + post
#     result = generator(prompt, max_length=100)
#     print(result[0]["generated_text"])


# while True:

#     print("1. Blog Introduction")
#     print("2. Product description")
#     print("3. Social media post")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         blog_introduction()

#     elif choice == "2":
#         product_description()

#     elif choice == "3":
#         social_media_post()

#     elif choice == "4":
#         break

#     else:
#         print("Choose from the given options..")
     

# Q7.

# from transformers import pipeline
# classifier = pipeline("sentiment-analysis")
# generator = pipeline("text-generation")
# review = input("Enter your review: ")
# result = classifier(review)
# sentiment = result[0]["label"]
# print("Sentiment:", sentiment)
# prompt = "Write a polite response to this " + sentiment + " review: " + review
# response = generator(prompt, max_length=100)
# print("AI Response:")
# print(response[0]["generated_text"])

# Q8.

# from transformers import pipeline
# sentiment_analyzer = pipeline("sentiment-analysis")
# text_generator = pipeline("text-generation")

# def analyze_sentiment():
#     text = input("\nEnter text: ")
#     result = sentiment_analyzer(text)
#     label = result[0]["label"]
#     confidence = result[0]["score"]
#     print(label)
#     print(confidence)

# def generate_text():
#     prompt = input("\nEnter prompt: ")
#     result = text_generator(
#         prompt,
#         max_length=50,
#         num_return_sequences=1
#     )

#     generated_text = result[0]["generated_text"]
#     print("\nGenerated Text:")
#     print(generated_text)

# def analyze_multiple_reviews():
#     number_of_reviews = int(input("\nEnter number of reviews: "))
#     reviews = []
#     for i in range(number_of_reviews):
#         review = input(f"Enter review {i + 1}: ")
#         reviews.append(review)
#     results = []
#     for review in reviews:
#         result = sentiment_analyzer(review)
#         label = result[0]["label"]
#         confidence = result[0]["score"]
#         review_result = {
#             "review": review,
#             "label": label,
#             "confidence": confidence
#         }
#         results.append(review_result)
#     positive_count = 0
#     negative_count = 0
#     total_confidence = 0
#     for result in results:
#         if result["label"] == "POSITIVE":
#             positive_count += 1
#         elif result["label"] == "NEGATIVE":
#             negative_count += 1
#         total_confidence = total_confidence + result["confidence"]
#     average_confidence = total_confidence / len(results)
#     print("Total Reviews:", len(results))
#     print("Positive:", positive_count)
#     print("Negative:", negative_count)

#     print(
#         "Average Confidence:",
#         round(average_confidence * 100, 2),
#         "%"
#     )

# while True:
#     print("1. Analyze Sentiment")
#     print("2. Generate Text")
#     print("3. Analyze Multiple Reviews")
#     print("4. Exit")
#     choice = input("\nEnter your choice: ")

#     if choice == "1":

#         analyze_sentiment()

#     elif choice == "2":

#         generate_text()

#     elif choice == "3":

#         analyze_multiple_reviews()

#     elif choice == "4":

#         print("\nThank you for using AI Assistant!")
#         break

#     else:

#         print("\nInvalid choice. Please try again.")

