# 🔵 Pandas Practice Set (20 Questions)
# Easy
# Q1.

# Create a DataFrame

# Columns:

# Name
# Age
# City

# with 5 students.

# import pandas as pd
# data = {
#     "Name":["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit"],
#     "Age":[21 , 22 , 23 , 24 , 25],
#     "City":["Sangrur" , "Ludhiana" , "Delhi" , "Mohali" , "Balongi"]
# }
# df = pd.DataFrame(data)
# print(df.head())
# print(df.tail())
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df["Name"])
# print(df["Name"] , df["City"])
# print(df[df["Age"]>22])
# print(df[df["City"]=="Delhi"])
# print(df.sort_values("Age" , ascending=False))
# Q2.

# Display:

# head()
# tail()
# Q3.

# Print:

# shape
# columns
# info()
# Q4.

# Print statistical summary.

# Q5.

# Select only the Name column.

# Q6.

# Select Name and City together.

# Q7.

# Filter students whose Age > 20.

# Q8.

# Filter students whose City is Delhi.



# Next Challenge (Interview Level)

# Isi DataFrame par ye 5 questions solve karo:

# Add a new column Marks with values:

# 90, 85, 95, 80, 88
# Display only students with Marks > 85.
# Find the average marks.
# Display the student with the highest marks.
# Sort the DataFrame by Marks in descending order.

# Ye questions placement aur interviews me bahut common hote hain. 💪


# import pandas as pd
# data = {
#     "Name":["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit"],
#     "Age":[21 , 22 , 23 , 24 , 25],
#     "City":["Sangrur" , "Ludhiana" , "Delhi" , "Mohali" , "Balongi"],
#     "Marks":[90 , 85, 95 , 80 , 88]
# }
# df = pd.DataFrame(data)
# print(df[df["Marks"]>85])
# # print(df["Marks"].mean())
# result = df.groupby("Name")["Marks"].sum()
# result = result.sort_values(ascending=False).head(1)
# print(result)
# print(df["Marks"].mean())
# print(df.sort_values("Marks" , ascending=False))


# import pandas as pd
# df = pd.read_csv("students.csv")
# print(df.head(3))
# print(df.tail(2))
# print(df.shape)
# print(df.columns)
# print(df.info())
# print(df.describe())
# print(df["Name"])
# print(df[df["Marks"]>85])
# print(df[df["Course"]=="Python"])
# print(df.sort_values("Marks" , ascending=False))
# print(df["Marks"].mean())
# print(df.sort_values("Marks" , ascending=False).head(1))
# print(df.drop_duplicates())
# marks = df["Marks"].fillna(df["Marks"].mean())


# 1. matplotlib is basically a library in python used for data visualization
# import pandas as pd
# import matplotlib.pyplot as plt
# data  = {
#     "Students": ["Deepak", "Rahul", "Aman"],
#     "Marks": [90, 85, 95]
# }
# df = pd.DataFrame(data)
# plt.bar(df["Students"] , df["Marks"] ,color = "green")
# plt.xlabel("Students")
# plt.ylabel("Marks")
# plt.title("Students result based on marks")
# plt.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# data = {
#     "Courses" : ["Python", "SQL", "Gen AI"],
#     "Students" : [40, 30, 30]
# }
# df = pd.DataFrame(data)
# plt.pie(df["Students"] , labels=df["Courses"]  ,autopct="%1.1f%%")
# plt.xlabel("Courses")
# plt.ylabel("Students")
# plt.title("Courses based on Students")
# plt.show()


import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Marks" : [45,67,89,90,76,55,88,92,61]
}
df = pd.DataFrame(data)
plt.hist(df["Marks"] , bins = 10  ,color="skyblue" )
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.title("Marks distribution")
plt.grid(True)
plt.show()
