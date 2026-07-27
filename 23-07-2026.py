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
df["Experience"] = df["Experience"].fillna(df["Experience"].mean())
print(df.isnull().sum())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())
print(df.isnull().sum())
print(df.isnull().sum())
print(df.drop_duplicates())
print(df.groupby("Department")["Salary"].max())
print(df.groupby("City")["Performance Rating"].max())
print(df.sort_values("Salary" , ascending=False).head(5))
category_salary = df.groupby("Department")["Salary"].mean()
category_salary.plot(kind="bar")
plt.title("Avergae Salary by department")
plt.xlabel("Department")
plt.ylabel("Salary")
plt.show()
employees_city = df["City"].value_counts()
employees_city.plot(kind="pie" , autopct = "%1.1f%%")
plt.title("Employees by City")
plt.show()
plt.hist(df["Salary"] , bins=5)
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.title("Salary Distribution")
plt.show()




"""Exercise 2 – Retail Sales Intelligence System
Create a dataset containing 100 sales records.
Columns:

Order ID
Product
Category
City
Quantity
Price
Discount
Tasks
1. Create a new column:

FinalAmount = (Quantity × Price) - Discount
2. Find:
Highest revenue product.
Lowest revenue product.
Average order value by category.
City with the highest sales.
3. Sort products by total revenue.
4. Visualize:
Category-wise revenue (Bar Chart).
Sales distribution (Histogram).
City-wise order percentage (Pie Chart).
5. Write five business recommendations.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("retail_sales.csv")
df["Final Amount"] = df["Quantity"]*df["Price"]-df["Discount"]
print(df.groupby("Product")["Final Amount"].agg(
    ["max" , "min"]
)
)
category_revenue = df.groupby("Category")["Final Amount"].sum()
plt.bar(category_revenue.index , category_revenue.values , color = "green")
plt.xlabel("Category")
plt.ylabel("Total Revenue")
plt.title("Category wise revenue")
plt.grid(True)
plt.show()
plt.hist(df["Final Amount"] , bins = 5 , color="skyblue" , edgecolor = "black")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.title("Sales distribution")
plt.grid(True)
plt.show()
city_orders = df["City"].value_counts()
plt.pie(city_orders , labels=city_orders.index , autopct="%1.1f%%")
plt.ylabel("City-wise")
plt.title("City-wise order percentage")
plt.show()
"""


"""Exercise 3 – Hospital Management Data Analysis
Create a dataset with 75 patient records.
Columns:

Patient ID
Department
Doctor
Age
Bill Amount
City
Tasks
1. Identify duplicate patients.
2. Handle missing values appropriately.
3. Find:
Department generating the highest revenue.
Doctor treating the maximum number of patients.
Average bill amount by department.
City contributing the highest hospital revenue.
4. Create:
Bar chart → Revenue by Department.
Pie chart → Patients by Department.
Histogram → Bill Amount.
5. Write five observations for hospital management.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("hospital_management_75_records.csv")
print(df.duplicated())
print(df.isnull().sum())
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Bill Amount"] =df["Bill Amount"].fillna(df["Bill Amount"].mean())
df["City"] =df["City"].fillna(df["City"].mode()[0])
print(df.isnull().sum())
department_revenue = df.groupby("Department")["Bill Amount"].sum()
department_revenue = department_revenue.sort_values(ascending=False)
print(department_revenue)
doctor_patient = df.groupby("Doctor")["Patient ID"].count()
doctor_patient = doctor_patient.sort_values(ascending=False)
print(doctor_patient)
city_revenue = df.groupby("City")["Bill Amount"].sum()
city_revenue = city_revenue.sort_values(ascending=False)
print(city_revenue)
department_revenue = df.groupby("Department")["Bill Amount"].sum()
plt.bar(department_revenue.index , department_revenue.values , color = "green")
plt.xlabel("Department")
plt.ylabel("Revenue")
plt.title("Revenue by department")
plt.show()
doctor_patient = df.groupby("Department")["Patient ID"].count()
plt.pie(doctor_patient , labels = doctor_patient.index , autopct="%1.1f%%")
plt.title("patients by department")
plt.legend()
plt.show()
plt.hist(df["Bill Amount"] , bins = 30 , color = "skyblue" , edgecolor = "black")
plt.xlabel("Bill Amount")
plt.ylabel("Frequency")
plt.title("Bill Amount")
plt.show()
"""



"""Exercise 4 – Netflix Content Analytics
Create a dataset with 60 movies or series.
Columns:

Title
Genre
Language
Rating
Duration
Release Year
Tasks
1. Remove duplicate titles.
2. Fill missing ratings with the average rating.
3. Find:
Most popular genre.
Average duration by genre.
Highest-rated movie.
Number of movies released after 2020.
4. Sort movies by rating.
5. Create:
Bar chart → Average Rating by Genre.
Pie chart → Language Distribution.
Histogram → Movie Duration.
6. Write five insights for a streaming platform.

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("netflix_content_analytics_60_records.csv")
print(df.isnull().sum())
print(df.duplicated(subset="Title"))
print(df.drop_duplicates(subset="Title"))
df["Rating"] = df["Rating"].fillna(df["Rating"].mean())
print(df.isnull().sum())
result = df.groupby("Genre")["Title"].count()
result = result.sort_values(ascending=False)
print(result.head(1))
duration_genre = df.groupby("Genre")["Duration"].mean()
print(duration_genre)
rating_movie = df.groupby("Title")["Rating"].sum()
rating_movie = rating_movie.sort_values(ascending=False)
print(rating_movie.head(1))
release_2020 = df[df["Release Year"]>2020]
print(release_2020)
Rating = df.groupby("Title")["Rating"].sum()
Rating = Rating.sort_values(ascending=False)
print(Rating)
Genre = df.groupby("Genre")["Rating"].mean()
plt.bar(Genre.index , Genre.values , color ="pink")
plt.xlabel("Genre")
plt.ylabel("Rating")
plt.title("Average Rating by Genre")
plt.show()
Language = df["Language"].value_counts()
Language.plot(kind="pie" , labels = Language.index , autopct = "%1.1f%%")
plt.title("Language Distribution")
plt.show()
plt.hist(df["Duration"] , bins=10 , color="skyblue" , edgecolor = "black")
plt.xlabel("Duration")
plt.ylabel("Frequency")
plt.title("Movie Duration")
plt.grid(True)
plt.show()
"""



"""Exercise 5 – Complete EDA Case Study (Capstone)
Create a dataset of your choice (minimum 100 records) such as:

E-commerce
Banking
Education
Sports
Tourism
Agriculture
Requirements
Perform a complete EDA workflow:
1. Read the dataset.
2. Explore it using:
head()
tail()
info()
describe()
3. Check and handle missing values.
4. Remove duplicates.
5. Use value_counts() on at least two categorical columns.
6. Sort by two different numeric columns.
7. Perform at least three groupby() analyses.
8. Create:
Bar chart
Pie chart
Histogram
9. Answer 10 business questions based on the data.
10. Write a one-page EDA report summarizing:
Dataset overview
Cleaning steps
Key statistics
Visualizations
Business insights
import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("capstone_eda_ecommerce_100_records.csv")
print(df)
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df["City"] = df["City"].fillna(df["City"].mode()[0])
df["Price"] =df["Price"].fillna(df["Price"].mean())
df["Payment Mode"] = df["Payment Mode"].fillna(df["Payment Mode"].mode()[0])
print(df.isnull().sum())
print(df.groupby("City")["Price"].sum())
print(df.groupby("Product")["Quantity"].max())
print(df.groupby("Product")["Discount"].sum())
City = df.groupby("City")["Price"].sum()
plt.bar(City.index , City.values , color = "green")
plt.xlabel("City")
plt.ylabel("Price")
plt.title("City vs Price")
plt.show()
Category = df["Category"].value_counts()
Category.plot(kind="pie" , labels = "Category.index" ,autopct="%1.1f%%")
plt.title("Category wise distribution ")
plt.show()
"""
