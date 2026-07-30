# Exercise 1: Classification Type Identification
# For each problem, identify whether it is:

# Binary Classification
# Multiclass Classification
# Examples:

# Disease / No Disease - Binary Classification.
# Cat / Dog / Horse - Multiclass Classification.
# Pass / Fail  - Binary Classication.
# Fraud / Genuine - Binary Classication.
# Red / Blue / Green - Multiclass Classifcation.

# Exercise 2: Threshold Prediction
# Using threshold = 0.5, predict the final class:
# Probability 0.910.720.490.210.50

# Output:
# Predicted Class

# Based on threshold prediction threshold = 0.5 it will belong to Class 1 

# Exercise 3: Sigmoid Understanding
# Given:
# z-5-2025
# Write:

# Which values are likely Class 0?
# Which values are likely Class 1?
# Explain why.
# z always belongs to nearby 0.5 the larger positive values belong to Class 1.
# and the smallest negative values belong to Class 1 .

# for z = -5 it will belong to Class 0.
# for z = 20 it will belong to Class 1.
# for z = 25 it will belong to Class 1.
    
# Exercise 4: Feature & Target Selection
# Given a Heart Disease Dataset:
# Age BP Cholesterol Heart_Disease
# Identify:

# Dataset - Age , BP , Cholestrol , Heart_Disease
# Features (X) - Age , BP , Cholestrol
# Target (y) - Heart_Disease
# Classification Type - Binary Classification


# Exercise 5: Train-Test Split Experiment
# Load the Heart Dataset.
# Create three different train-test splits:

# 80:20
# 70:30
# 60:40
# Train Logistic Regression on each.
# Compare:

# Accuracy
# Precision
# Which split performs best?

# import pandas as pd
# df = pd.read_csv("heart dataset.csv")
# print(df.isnull().sum())
# X = df[["Age" , "BP" , "Cholesterol" , "Heart_Rate" , "Smoking" ,"Exercise_Hours" ]]
# y = df["Heart_Disease"]
# from sklearn.model_selection import train_test_split
# X_train , X_test ,y_train , y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2,
#     random_state=42
# )
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=1000  , class_weight="balanced")
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_patient = [[40 , 170 , 201 , 80 , 0 , 0 ]]
# prediction = model.predict(new_patient)
# print("Having Disease:" , prediction)
# from sklearn.metrics import accuracy_score , recall_score , precision_score , f1_score
# print("accuracy score:" ,accuracy_score(y_test , y_pred))
# print("recall score:" ,recall_score(y_test , y_pred))
# print("precision score:" ,precision_score(y_test , y_pred))
# print("f1 score:" ,f1_score(y_test ,y_pred))

# # on test_size  = 0.3
# import pandas as pd
# df = pd.read_csv("heart dataset.csv")
# print(df.isnull().sum())
# X = df[["Age" , "BP" , "Cholesterol" , "Heart_Rate" , "Smoking" ,"Exercise_Hours" ]]
# y = df["Heart_Disease"]
# from sklearn.model_selection import train_test_split
# X_train , X_test ,y_train , y_test = train_test_split(
#     X,
#     y,
#     test_size=0.3,
#     random_state=42
# )
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=1000  , class_weight="balanced")
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_patient = [[40 , 170 , 201 , 80 , 0 , 0 ]]
# prediction = model.predict(new_patient)
# print("Having Disease:" , prediction)
# from sklearn.metrics import accuracy_score , recall_score , precision_score , f1_score
# print("accuracy score:" ,accuracy_score(y_test , y_pred))
# print("recall score:" ,recall_score(y_test , y_pred))
# print("precision score:" ,precision_score(y_test , y_pred))
# print("f1 score:" ,f1_score(y_test ,y_pred))

# # on test_size  = 0.4

# import pandas as pd
# df = pd.read_csv("heart dataset.csv")
# print(df.isnull().sum())
# X = df[["Age" , "BP" , "Cholesterol" , "Heart_Rate" , "Smoking" ,"Exercise_Hours" ]]
# y = df["Heart_Disease"]
# from sklearn.model_selection import train_test_split
# X_train , X_test ,y_train , y_test = train_test_split(
#     X,
#     y,
#     test_size=0.4,
#     random_state=42
# )
# from sklearn.linear_model import LogisticRegression
# model = LogisticRegression(max_iter=1000  , class_weight="balanced")
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_patient = [[40 , 170 , 201 , 80 , 0 , 0 ]]
# prediction = model.predict(new_patient)
# print("Having Disease:" , prediction)
# from sklearn.metrics import accuracy_score , recall_score , precision_score , f1_score
# print("accuracy score:" ,accuracy_score(y_test , y_pred))
# print("recall score:" ,recall_score(y_test , y_pred))
# print("precision score:" ,precision_score(y_test , y_pred))
# print("f1 score:" ,f1_score(y_test ,y_pred))

# Explanation : when i use test_size  = 0.2 the output was Having Disease: [1]
# accuracy score: 1.0
# recall score: 1.0
# precision score: 1.0
# f1 score: 1.0

# and when i use test_size = 0.3 the output was Having Disease: [1]
# accuracy score: 1.0
# recall score: 1.0
# precision score: 1.0
# f1 score: 1.0

# and when i use test_size  = 0.4 the output was Having Disease: [0]
# accuracy score: 0.75
# recall score: 0.6666666666666666
# precision score: 1.0
# f1 score: 0.8



# Exercise 6: Custom Threshold
# Using probabilities:

# [0.91,0.83,0.71,0.65,0.52,0.47,0.31]Predict classes using:

# Threshold = 0.5
# Threshold = 0.7
# Compare results and explain which observations changed class.


# for threshold = 0.5
# 0.91 - Class 1 , 0.83 - Class 1 , 0.71 - Class 1  , 0.65 - Class 1 , 0.52 - Class 1, 0.47 - Class 0 , 0.31 - Class 0
# for threshold = 0.7
# 0.91 - Class 1 , 0.83 - Class 1 , 0.71 - Class 1  , 0.65 - Class 0 , 0.52 - Class 0, 0.47 - Class 0 , 0.31 - Class 0

# Exercise 7: Probability Analyzer
# Train Logistic Regression on Heart Dataset.
# Instead of:

# model.predict()use:

# model.predict_proba()Display:

# First 20 probabilities
# Probability of Disease
# Probability of No Disease
# Then explain why some predictions are more confident than others.

# Exercise 8: Confusion Matrix Investigation
# After training:
# Calculate:

# TP
# TN
# FP
# FN
# Then answer:

# How many patients were correctly classified?
# How many false alarms occurred?
# How many disease cases were missed?
# Which mistake is more dangerous in healthcare?
# Provide justification.

# Exercise 9: Build a Diabetes Classifier
# Use Kaggle Diabetes Dataset.
# Tasks:

# Load Dataset
# EDA
# Missing Value Check
# Train-Test Split
# Logistic Regression
# Accuracy
# Precision
# Recall
# F1 Score
# Confusion Matrix Heatmap
# Finally answer:
# Would you trust this model in a real hospital? Why?

import pandas as pd
df = pd.read_csv("diabetes_prediction_dataset.csv")
print(df.head())
print(df.isnull().sum())
print(df["diabetes"].value_counts())
print(df["smoking_history"].unique())
print(df["gender"].unique())
X = df[["gender" , "age" , "hypertension" , "heart_disease" , "smoking_history" , "bmi" , "HbA1c_level" , "blood_glucose_level" ]]
y=df["diabetes"]
X["gender"] = X["gender"].map({"Female":0 , "Male":1})
X["smoking_history"] = X["smoking_history"].map({"former":0 , "never":1 , "No Info":2, "current":3 , "not current":4 , "ever":5})
Corr = X.corr()
print(Corr)
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(
    max_iter=10000,
    class_weight="balanced"
)
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_patient = [[1 , 59.0 , 1 , 1 , 1 , 29.7 , 7.0 , 190 ]]
prediction  = model.predict(new_patient)
print("Having diabetes:" , prediction)
from sklearn.metrics import accuracy_score , precision_score , f1_score , recall_score
print("accuracy score:",accuracy_score(y_test , y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("f1_score:" , f1_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))

# Exercise 10: Compare Regression vs Classification
# Build:
# Model 1
# Linear Regression
# Model 2
# Logistic Regression
# Using a Pass/Fail dataset.
# Compare:

# Predictions
# Output values
# Accuracy
# Write a report explaining:

# Why Linear Regression is not suitable for classification.
# Why Logistic Regression is better.
# Why probabilities are useful.
# Importance of threshold.


# Linear regression
import pandas as pd
df = pd.read_csv("laptop_price_dataset.csv")
print(df["brand"].unique())
print(df["processor"].unique())
print(df["Ram_type"].unique())
df.drop(columns=["name" , "CPU"] , inplace=True)
X = df[["brand" , "spec_rating" , "processor" ,  "Ram" , "Ram_type", "SSD_GB"]]
y = df["Price"]
X["brand"] = X["brand"].map({"MSI":0 , "HP":1 , "Acer":2 , "Lenovo":3 , "Dell":4 , "Apple":5 , "Asus":6})
X["processor"]  =X["processor"].map({"i3":0 , "i5":1 , "i7":2 , "Ryzen 5":3 , "M2":4 , "Ryzen 7":5})
X["Ram_type"]  = X["Ram_type"].map({"LPDDR4X":0 , "DDR4":1 , "DDR5":2 , "LPDDR5":3})
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test= train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_Laptop = [[1 , 99 , 1 ,  16 , 1 , 512 ]]
prediction = model.predict(new_Laptop)
print("New Laptop:" , prediction)
from sklearn.metrics import r2_score
r2 = r2_score(y_test , y_pred)
print("R2 is :",r2)


# Logistic Regression
import pandas as pd
df = pd.read_csv("student_pass_fail_dataset.csv")
print(df.isnull().sum())
df.drop(columns=["student_id"],inplace=True)
X = df[[ "study_hours" ,"attendance" , "previous_marks" , "assignments_completed" , "sleep_hours" , "internet_usage" ,"extracurricular" ]]
y = df["pass"]
X["extracurricular"] = X["extracurricular"].map({"Yes":0 , "No":1})
from sklearn.model_selection import train_test_split
X_train , X_test , y_train  , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=10000 , class_weight="balanced")
model.fit(X_train , y_train)
y_pred  = model.predict(X_test)
new_student  = [[2.0 , 72 , 83 , 4 , 8.0 , 5.0 , 0]]
prediction = model.predict(new_student)
print("new student :" , prediction)
from sklearn.metrics import recall_score , precision_score , f1_score , accuracy_score
print("accuracy score:" , accuracy_score(y_test ,y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("f1 score:" , f1_score(y_test ,y_pred))
print("recall score:" ,recall_score(y_test , y_pred))