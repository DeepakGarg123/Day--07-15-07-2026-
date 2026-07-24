# Maan le

# Student.csv

# hai.

# Uska code likh:

# Pandas import karo.
# CSV read karo.
# Puri table print karo.
# First 5 rows.
# Last 5 rows.

# import pandas as pd
# df = pd.read_csv("students.csv")
# print(df)
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.shape)
# print(df.shape[0])
# print(df.shape[1])
# print(df.columns)

# Practice Question

# Dataset:

# Name	Age	Salary	Rating	Active
# Deepak	21	35000	4.5	True
# Rahul	22	45000	4.2	False
# Bata:

# df.dtypes ka output kya hoga?

# Har column ke saamne datatype likh. 💪

import pandas as pd
data = {
    "Name" :["Deepak" ,"Rahul"],
    "Age":[21 , 22],
    "Salary":[35000 , 45000],
    "Rating":[4.5 , 4.2],
    "Active":[True , False]
}
df = pd.DataFrame(data)
print(df.dtypes)
print(df.isnull())
print(df.isnull().sum())


# 🎯 Practice

# Dataset:

# Name	Marks
# Deepak	90
# Rahul	80
# Aman	❌
# Mohit	70
# Karan	❌

# ❓ Question:

# Marks.mean() kitna hoga?
# fillna(Marks.mean()) ke baad Aman aur Karan ke Marks kitne ho jayenge?

import pandas as pd
df = pd.read_csv("marks.csv")
print(df.isnull().sum())
df = df.dropna()
print(df)
print(df.duplicated())
print(df.drop_duplicates())

# Questions
# Q1.

# Salary ko highest se lowest arrange karo.

# Q2.

# Experience ko lowest se highest arrange karo.

# Q3.

# Department ke hisaab se arrange karo aur har department me highest salary pehle dikhao.

# 💡 Hint:

# by = ["Department", "Salary"]
# Q4.

# Sirf Top 3 highest-paid employees dikhao.

# Q5. ⭐ (Interview)

# Salary ke basis par sort karo aur sirf Employee aur Salary columns print karo.

import pandas as pd
data = {
    "Employee": ["Deepak", "Rahul", "Aman", "Mohit", "Karan"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [45000, 60000, 55000, 40000, 50000],
    "Experience": [2, 5, 3, 1, 4]
}
df = pd.DataFrame(data)
print(df)
print(df.sort_values("Salary" , ascending=False))
print(df.sort_values("Experience" , ascending=True))
df.sort_values(
    by = ["Department" , "Salary"] , 
    ascending=[True , False]
)
print(df.sort_values("Salary" , ascending=False).head(3))
print(df.sort_values("Salary" , ascending=True))

# Questions
# Q1.

# Marks ko highest se lowest arrange karo.

# Q2.

# Attendance ko lowest se highest arrange karo.

# Q3.

# Course ke hisaab se arrange karo aur har course ke andar highest marks pehle dikhao.

# 💡 Hint:

# by=["Course", "Marks"]
# ascending=[True, False]
# Q4.

# Top 2 students dikhao jinke marks sabse zyada hain.

# Q5.

# Sirf Student aur Marks columns print karo descending order me.

# Expected columns:

# Student    Marks
# Riya       97
# Rahul      95
# Mohit      91
# Deepak     88
# Karan      84
# Aman       76
# ⭐ Bonus (Interview Level)

# Top 3 students print karo jinki:

# Marks highest hon
# Aur output me sirf ye columns aaye:
# Student
# Course
# Marks


# import pandas as pd
# data = {
#      "Student": ["Deepak", "Rahul", "Aman", "Mohit", "Karan", "Riya"],
#     "Course": ["Python", "Gen AI", "Python", "SQL", "Gen AI", "SQL"],
#     "Marks": [88, 95, 76, 91, 84, 97],
#     "Attendance": [85, 92, 78, 96, 88, 90]
# }
# df = pd.DataFrame(data)
# print(df.sort_values("Marks" , ascending=False))
# print(df.sort_values("Attendance" , ascending=False))
# print(df.sort_values(
#     by=["Course" , "Marks"],
#     ascending=[True,False]
# ))
# print(df.sort_values("Marks").head(2))
# print(df.sort_values(
#     by = ["Student" , "Marks"],
#     ascending=[False , False]
# ))


# import pandas as pd
# data = {
#     "Brand": ["HP", "Dell", "Lenovo", "Acer", "Asus", "HP", "Dell"],
#     "RAM": [8, 16, 8, 4, 16, 32, 8],
#     "Price": [55000, 72000, 48000, 35000, 68000, 95000, 61000],
#     "Rating": [4.2, 4.6, 4.1, 3.9, 4.5, 4.8, 4.3]
# }
# df = pd.DataFrame(data)
# print(df.sort_values("Price" , ascending=False))
# print(df.sort_values("Ram" , ascending=True))
# print(df.sort_values(
#     by=["Brand" , "Price"],
#     ascending=[True,False]
# ))
# print(df.sort_values("Laptop" ,ascending=False).head(3))
# print(df.sort_values("Price" ,ascending=False)[["Brand" , "Price"]])


import pandas as pd
data = {
    "Student": ["Deepak", "Rahul", "Aman", "Mohit", "Karan", "Riya"],
    "Course": ["Python", "Python", "SQL", "SQL", "Gen AI", "Gen AI"],
    "Marks": [90, 80, 70, 85, 95, 75]
}
df = pd.DataFrame(data)
print(df.groupby("Course")["Marks"].mean())
print(df.groupby("Course")["Marks"].max())
print(df.groupby("Course")["Marks"].min())
print(df.groupby("Course")["Marks"].sum())
print(df.groupby("Course")["Marks"].count())
result = df.groupby("Course")["Marks"].mean()
result = result.sort_values(ascending=False)
print(result)