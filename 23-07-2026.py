# Exercise 1 – Employee Performance Analytics Dashboard
# Create a CSV file with at least 50 employee records.
# Columns:

# Employee ID
# Name
# Department
# City
# Experience
# Salary
# Performance Rating
# Tasks
# 1. Read the dataset.
# 2. Check dataset information using info().
# 3. Find missing values and fill numeric missing values with the column average.
# 4. Remove duplicate records.
# 5. Display:
# Department with the highest average salary.
# City with the highest average performance rating.
# Top 5 highest-paid employees.
# 6. Create:
# Bar chart → Average Salary by Department.
# Pie chart → Employees by City.
# Histogram → Salary Distribution.
# 7. Write five business insights.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("employees.csv")
print(df)
print(df.info())
print(df.isnull().sum())
print(df.drop_duplicates())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("City")["Performance Rating"].max())



# Exercise 2 – Retail Sales Intelligence System
# Create a dataset containing 100 sales records.
# Columns:

# Order ID
# Product
# Category
# City
# Quantity
# Price
# Discount
# Tasks
# 1. Create a new column:

# FinalAmount = (Quantity × Price) - Discount
# 2. Find:
# Highest revenue product.
# Lowest revenue product.
# Average order value by category.
# City with the highest sales.
# 3. Sort products by total revenue.
# 4. Visualize:
# Category-wise revenue (Bar Chart).
# Sales distribution (Histogram).
# City-wise order percentage (Pie Chart).
# 5. Write five business recommendations.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("retail_sales.csv")
df["Final Amount"] = df["Quantity"]*df["Price"]-df["Discount"]
print(df.groupby("Product")["Final Amount"].max())


# Exercise 3 – Hospital Management Data Analysis
# Create a dataset with 75 patient records.
# Columns:

# Patient ID
# Department
# Doctor
# Age
# Bill Amount
# City
# Tasks
# 1. Identify duplicate patients.
# 2. Handle missing values appropriately.
# 3. Find:
# Department generating the highest revenue.
# Doctor treating the maximum number of patients.
# Average bill amount by department.
# City contributing the highest hospital revenue.
# 4. Create:
# Bar chart → Revenue by Department.
# Pie chart → Patients by Department.
# Histogram → Bill Amount.
# 5. Write five observations for hospital management.



# Exercise 4 – Netflix Content Analytics
# Create a dataset with 60 movies or series.
# Columns:

# Title
# Genre
# Language
# Rating
# Duration
# Release Year
# Tasks
# 1. Remove duplicate titles.
# 2. Fill missing ratings with the average rating.
# 3. Find:
# Most popular genre.
# Average duration by genre.
# Highest-rated movie.
# Number of movies released after 2020.
# 4. Sort movies by rating.
# 5. Create:
# Bar chart → Average Rating by Genre.
# Pie chart → Language Distribution.
# Histogram → Movie Duration.
# 6. Write five insights for a streaming platform.

# Exercise 5 – Complete EDA Case Study (Capstone)
# Create a dataset of your choice (minimum 100 records) such as:

# E-commerce
# Banking
# Education
# Sports
# Tourism
# Agriculture
# Requirements
# Perform a complete EDA workflow:
# 1. Read the dataset.
# 2. Explore it using:
# head()
# tail()
# info()
# describe()
# 3. Check and handle missing values.
# 4. Remove duplicates.
# 5. Use value_counts() on at least two categorical columns.
# 6. Sort by two different numeric columns.
# 7. Perform at least three groupby() analyses.
# 8. Create:
# Bar chart
# Pie chart
# Histogram
# 9. Answer 10 business questions based on the data.
# 10. Write a one-page EDA report summarizing:
# Dataset overview
# Cleaning steps
# Key statistics
# Visualizations
# Business insights