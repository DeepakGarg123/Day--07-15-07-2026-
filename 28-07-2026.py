# Exercise 1 — Identify the ML Problem
# For each scenario, write:

# Machine Learning or Traditional Programming?
# If ML, identify:
# Supervised
# Unsupervised
# Semi-supervised
# Reinforcement

# Scenarios:

# ATM PIN verification
# Netflix Recommendations
# Detecting fake credit card transactions
# Robot learning to walk
# Grouping customers based on shopping habits
# Face Unlock in smartphones
# Chess-playing AI
# Calculator

# 1 . Atm pin verification  - No machine learning is used because it is not the matter of guessing or predicting the atm pins . ml models are not accurate that they matches the pin.
# 2. Netflix Recommendations - yes the machine learning is used and the unsupervised learning is used because we don't give any labelled data the machine has to guess that the user might like these type of mobvies based on watch history.
# 3. Detecting fake credit card transactions - Supervised ml because the bank has all the data that the card is spam or not spam
# 4. Robot learning to walk - Reinforcement learning because we give reward based on walking and penalty based on falling
# 5. Grouping customers based on shopping habits - Unsupervised because the ml model has to make clusters or groups no labelled data
# 6. Face unlock  - Supervised because your phone has saved data faces
# Chess-playing AI - Reinforcement learning because you give rewards based on winning match and penalty based on losing
# Calculator - Traditional Programming

# Exercise 2 — Dataset Analysis
# Create a dataset containing

# Student Name
# Age
# Study Hours
# Attendance
# Final Marks
# City
# Answer:

# Dataset
# Observation
# Features
# Target
# Number of observations
# Number of features

# df = pd.read_csv("students.csv")
# 1 . Dataset - the whole table (the csv file)
# 2. Observation - the single row in dataset
# 3. Features - the data that is given columns
# 4. Target - target is the need to be predict
# 5. no. of observations - 10
# 6. no. of features - 6



# Exercise 3 — Feature Selection Challenge
# For each problem identify X and y.
# Example:
# Predict House Price
# Columns

# Area
# Bedrooms
# Bathrooms
# City
# Price
# Questions
# What are the Features?
# What is the Target?

# Repeat for:

# Car Price
# Employee Salary
# Diabetes Prediction
# Loan Approval
# Movie Collection

# Area   bedrooms  bathrooms  City   price

# 1. the features are the data we have given like (Area   bedrooms  bathrooms  City)
# 2. the target is that we need to predict like Price
# 3.  Car Price
# features - Car_Name,Brand,Year
# Target - Price
# 4. Employee Salary  
# features - Employee_Name,Age,Experience,Education,Department
# Target - Salary
# 5. Diabetes Prediction
# Features - Patient_ID,Age,Glucose,Blood_Pressure
# Target - Diabetes
# 6. Loan Approval
# Fetaures - Applicant_ID,Age,Income,Credit_Score,Loan_Amount
# Target - Loan_Approved
# 7. Movie Collection
# Features - Movie_Name,Genre,Budget,Duration,IMDB_Rating,Screens
# Target - Box_Office_Collection



# Exercise 4 — Regression or Classification?
# Decide whether each problem is
# Regression
# or
# Classification

# Predict Salary - Regression
# Predict Blood Group - Classificaition
# Predict Age - Regressoin
# Predict Customer Churn - Classification
# Predict Height - Regression
# Predict Pass/Fail - Classification
# Predict House Price - Regression
# Predict Disease - Classification
# Predict Temperature - Regression
# Predict Spam Email - Classification


# Exercise 5 — Build Your Own ML Workflow
# Choose ONE industry

# Banking
# Hospital
# Agriculture
# School
# Restaurant
# Cricket
# Draw the entire Machine Learning Workflow.
# Explain every step in your own words.
# No coding.


# Patient_ID,Age,BMI,Blood_Pressure,Glucose,Cholesterol,Smoking,Exercise,Diabetes
# P001,45,28.5,140,180,220,Yes,No,Yes
# P002,30,22.1,120,95,180,No,Yes,No
# P003,55,31.4,150,210,250,Yes,No,Yes
# P004,40,26.2,130,120,190,No,Yes,No
# P005,60,34.0,160,240,280,Yes,No,Yes
# P006,35,24.8,125,110,185,No,Yes,No
# P007,50,29.6,145,190,230,Yes,No,Yes
# P008,42,27.1,135,140,200,No,Yes,No
# P009,48,30.2,148,205,240,Yes,No,Yes
# P010,33,23.5,118,100,175,No,Yes,No

# 1. Data Collection - data is collected
# 2. EDA - Operations perform like data cleaning  , filling missing values
# 3. Features(X) - that we have data to find the target
# 4. Target(Y) - we find our goal based on the features
# 5. Train Test Split - Dataseet is divided in to two parts : train and test training 70-80% and 20% test
# 6. Train Model - training model using model.fit(X)
# 7. Prediction - testing model using model.predict()
# 8. Evaluation - we check how well our model is trained or test


# Exercise 6 — Manual Prediction
# Suppose a model learns
# Salary = 6000 × Experience + 25000Predict salary for

# 2 years
# 4 years
# 6 years
# 8 years
# 10 years
# Then explain
# What does
# 6000
# represent?
# What does
# 25000
# represent?

# y=mx+c
# Salary = 6000*Experience + 25000
# 1. 37000
# 2. 49000
# 3. 61000
# 4. 73000
# 5. 85000
# 1. 6000 reperesent the m i.e. slope or gradient
# 2. 25000 reperesent the c i.e. y-intercept 

# Exercise 7 — Create Your Own Dataset
# Create your own dataset having
# 50 rows
# Choose any topic

# Cars
# Books
# Mobiles
# Cricket
# College
# Then identify

# Dataset
# Observations
# Features
# Target


# Brand,Ram,Storage,Waterproof,Price
# Samsung,6GB,128Gb,Yes,25000
# Oppo,4GB,64Gb,No,12000
# 1. Dataset - Samsung,6GB,128Gb,Yes,25000
# Oppo,4GB,64Gb,No,12000
# 2. Observations - Samsung,6GB,128Gb,Yes,25000
# 3. Features - Brand,Ram,Storage,Waterproof
# 4. Target - Price

# Exercise 8 — Machine Learning Terminology Mapping
# Given this dataset
# NameExperienceSkillsSalary
# Answer
# Dataset
# Observation
# Features
# Target
# Training Data
# Testing Data
# Algorithm
# Model
# Prediction
# using this dataset.


# Name,Experience,Skills,Salary
# Rahul,2,Python,35000
# Deepak,1,Python,30000
# Aman,5,Java,65000
# Simran,7,AI,90000
# Neha,3,Python,50000

# 1. Dataset - the whole data combination of observations(
# #Rahul,2,Python,35000
# # Deepak,1,Python,30000
# # Aman,5,Java,65000
# # Simran,7,AI,90000
# # Neha,3,Python,50000
# )
# 2. Observation - #Rahul,2,Python,35000
# 3. Features - # Name,Experience,Skills
# 4. Target - Salary
# 5. Trainig Data - 70-80% of the data is trained
# 6. Testing Data - 20% of the data is tested
# 7. Algorithm - the method or we can say the set of rules from which the machine learns
# 8. Model - after the appliness of algorithm the model we get is the trained ModuleNotFoundError
# 9. Prediction - the machine generated the new data. 


# Exercise 9 — Insurance Dataset Investigation
# Using the Insurance Dataset,
# without training any model,
# answer:

# Which feature is likely to affect insurance charges the most?
# Which feature is least useful?
# Which categorical columns need encoding?
# Which column is the target?
# Which columns are numerical?
# Explain your reasoning.

# Age,Sex,BMI,Children,Smoker,Region,Charges
# 19,female,27.9,0,yes,southwest,16884.92
# 31,male,25.7,1,no,southeast,4449.46
# 45,male,30.5,2,yes,northwest,28923.14
# 28,female,22.4,0,no,northeast,3866.86
# 52,male,33.8,3,yes,southeast,37270.15

# 1. Smoker because the smoker usually affect their health so medical charges are affected.
# 2. Region is least useful because no matter the person belongs from it will not affect the medical charges
# 3. Sex , Children , Region because the machine model can't understand the categorical data.
# 4. Charges is the target because based on the features we need to predict the charges
# 5. Age , BMI , Children , Charges

# Exercise 10 — Mini End-to-End ML Project (No Code Repetition)
# Choose any one domain:

# House Price Prediction
# Used Car Price Prediction
# Student Marks Prediction
# Salary Prediction
# Mobile Price Prediction
# Write a report covering:

# Problem Statement
# Dataset Description
# Features (X)
# Target (y)
# Type of Machine Learning
# Regression or Classification?
# Why Machine Learning is suitable instead of Traditional Programming?
# Which algorithm would you use first and why?
# How would you evaluate the model?
# Mention two possible limitations of your approach.


# Salary prediction
# Employee_Name,Age,Experience,Education,Department,Salary
# Rahul,24,1,BCA,IT,32000
# Deepak,22,0,BCA,IT,28000
# Aman,27,4,MCA,Software,58000
# Simran,30,7,MTech,AI,92000
# Neha,26,3,BTech,Software,50000

# Problem Statement - in this we are having features(Employee_Name,Age,Experience,Education,Department) based on these we have to find the salary
# Dataset - the dataset contains information about employee_name , age , experience , education , department,salary
# features -  Employee_Name,Age,Experience,Education,Department
# Target - Salary
# Type of ml - Supervised because we have given the data employeename , age , experience , department , salary
# Regression or classification - Regression because salary is continuous numerical value
# Why Machine Learning is suitable instead of Traditional Programming? - In traditional Programming we have to give manually or set the rules but in machine learning we have data and the machine learns from the data and predict new values.
# Which algorithm would you use first and why? - i would choose linear Regression because it is simple and straight line graph is drawn using y=mx+c equation here m is slope and c is intercept.
# How would you evaluate the model? - using r2 score we can check the accuracy of the model like 0.74888 it means our model is giving 74.8% correct prediction.

# If a new student has:

# Age = 21
# Study Hours = 5
# Attendance = 92
# Previous Marks = 84


# | Student | Age | Study_Hours | Attendance | Previous_Marks | Final_Marks |
# | ------- | --: | ----------: | ---------: | -------------: | ----------: |
# | Rahul   |  20 |           2 |         75 |             60 |          65 |
# | Aman    |  21 |           5 |         90 |             80 |          88 |
# | Deepak  |  22 |           4 |         85 |             75 |          82 |
# | Simran  |  20 |           6 |         95 |             85 |          92 |
# | Neha    |  21 |           3 |         80 |             70 |          74 |

# Part A – ML Basics
# Q1. 

# Is this problem suitable for:

# Traditional Programming
# Machine Learning

# Explain why.
# this probelm is suitable for machine learning because in traditonal programming if we have given a new data of student we can't find the Final_Marks manually on the other hand machine learning learns from the data and predicts the new data based on patterns. 
# # Q2.

# # Which type of Machine Learning is used?

# # Supervised
# # Unsupervised
# # Semi-Supervised
# # Reinforcement

# Supervised machine learning is used in this because we have given labelled data with student ,  age  , study_hours , attendance , previous_marks , final_marks.
# # Q3.

# # Is this problem:

# # Regression
# # Classification

# # Explain your answer.
# this problem is of regression because we have to predict a number not a category.
# # Part B – Dataset Terminology
# # Q4.

# # What is the Dataset?
# the whole data is known as dataset or we can say a combination of observations.
# # Q5.

# # What is one Observation?
# a single row in the dataset is known as the observation.
# # Q6.

# # Identify the Features (X).
#  Student | Age | Study_Hours | Attendance | Previous_Marks
# # Q7.

# # Identify the Target (y).
# Final_Marks
# # Q8.

# # How many observations are present?
# there are 5 observations present in the dataset.
# # Q9.

# # How many features are present?
# there are 5 features present in the dataset.
# # Part C – Workflow
# # Q10.

# # Write the complete Machine Learning workflow in order.
# 1. Data collection
# 2. EDA
# 3. Features
# 4. Target
# 5. Train-Test-Split
# 6. Train Model
# 7. Prediction
# 8. Evaluation
# # Q11.

# # Why do we split the data into Training and Testing?
# We split the data into training and testing because to make sure our machine learning model learns from the data analyzes the pattern and try to predict the accurate predictions.
# # Q12.

# # What is the difference between an Algorithm and a Model?
# Algorithm is a set of rules or we can say a procedure and model is a outcome or say final output that is made from the algorithm by using set of rules. 
# # Q13.

# # What does the fit() function do?

# the fit function is used for training the model model.fit(X)
# # Q14.

# # What does the predict() function do?
# predict function is used to predict the output model.predict()
# # Part D – Reasoning
# # Q15.

# # Which feature do you think affects Final_Marks the most?
# Study_Hours affect the final_marks most because as much the student study he will get the more marks
# # Explain your answer.

# # Q16.

# # Which feature do you think is the least useful?

# # Explain your answer.
# Age is least useful feature because age no matters study_hours matter the most and attendance if the student is regular in the Class.
# # Q17.

# # If a new student has:

# # Age = 21
# # Study Hours = 5
# # Attendance = 92
# # Previous Marks = 84

# # What will the machine try to predict?
# the machine will try to predict the final_marks between 85 and 91 
# # Q18.

# # Would you use Linear Regression for this problem?

# # Why?
# because linear regression is simple to use and no of any toughness there is an equation y = mx+c

# import pandas as pd

# df = pd.read_csv("students.csv")

# print(df.head())

# # Features
# X = df[["Age", "Study_Hours", "Attendance", "Previous_Marks"]]

# # Target
# y = df["Final_Marks"]

# from sklearn.model_selection import train_test_split

# X_train, X_test, y_train, y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )

# from sklearn.linear_model import LinearRegression

# model = LinearRegression()

# model.fit(X_train, y_train)

# # Predict for test data
# y_pred = model.predict(X_test)

# # Predict for new student
# new_student = [[21, 5, 94, 84]]

# prediction = model.predict(new_student)

# print("Predicted Marks:", prediction)

# from sklearn.metrics import r2_score

# r2 = r2_score(y_test, y_pred)

# print("R2 Score:", r2)


import pandas as pd
df = pd.read_csv("employees_salary.csv")
print(df.head())
X = df[["Age" , "Experience" , "Projects"]]
y = df["Salary"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_Employee = [[30 , 7 , 5 ]]
prediction = model.predict(new_Employee)
print("Predicted Salary:" , prediction)
from sklearn.metrics import r2_score
r2 = r2_score(y_test , y_pred)
print(r2)
