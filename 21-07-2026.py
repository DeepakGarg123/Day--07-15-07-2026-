# import pandas as pd
# data = {
#     "Name":["Deepak" , "Rahul" , "Aman"],
#     "Course":["Gen ai" , "data science" ,"Python" ],
#     "Duration":[6 , 3 , 8]
# }
# df = pd.DataFrame(data)
# print(df)


# import pandas as pd
# data = {
#     "name" :["Deepak" , "Bharat" , "David" , "Arman"],
#     "Age" : [21 , 20 , 22 , 21],
#     "Course" :["Gen_ai" , "Mern_stack" , "Web development" , "Backend"],
#     "Duration":[6 , 6 , 6 , 6]
# } 
# df = pd.DataFrame(data)
# print(df)

# import pandas as pd
# data = {
#     "Name":["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit" , "Karan" , "Ajay"],
#     "marks":[90,85,70,95,76,81,88]
# }
# data = pd.DataFrame(data)
# print(data)
# print(data.head())
# print(data.head(3))
# print(data.tail())
# print(data.tail(2))

# import pandas as pd
# df = {
#     "name":["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit" , "Karan" ,"Ajay"],
#     "marks":[90 , 85 , 70 , 95 , 76 , 81 , 88]
# }
# df = pd.DataFrame(df)
# print(df)
# print("--------------")
# print(df.sample())
# print("---------------")
# print(df.sample(3))
# print("----------------")
# print(df.shape[0])
# print("-----------------")
# print(df.shape[1])
# print("-----------------")
# print(df.info())
# print("------------------")
# print(df.describe())
# print("------------------")

# import pandas as pd
# data  = {
#     "Name" :["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit" , "Karan" ],
#     "Age" : [21 , 22 , 20 ,23 , 24 , 21],
#     "Course" :["Gen ai" , "Python" , "Data Science" , "Gen ai" , "Python" , "Data Science"],
#     "Marks" :[90 , 85 , 78 , 88 , 92 , 91]
# }
# data = pd.DataFrame(data)
# print("----------------------")
# print(data)
# print("----------------------")
# print(data.shape)
# print("----------------------")
# print(data.columns)
# print("----------------------")
# print(data.index)
# print("----------------------")
# print(data.head(3))
# print("----------------------")
# print(data.tail(2))
# print("----------------------")
# print(data.sample(2))
# print("----------------------")
# print(data.info())
# print("----------------------")
# print(data.describe())
# print("----------------------")
# print(data.nunique())
# print("The END")


# import pandas as pd
# data = {
#     "Name" :["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit"],
#     "Age": [21, 22, 20, 23, 24],
#     "City": ["Sangrur", "Patiala", "Mohali", "Delhi", "Chandigarh"],
#     "Course": ["Gen AI", "Python", "Data Science", "Gen AI", "Python"],
#     "Marks": [90, 85, 78, 92, 88]
# }
# df =pd.DataFrame(data)
# print(df.loc[1])
# print(df.loc[4])
# print(df.loc[0])
# print(df.loc[2 , "Marks"])
# print(df.loc[3,"City"])
# print(df.loc[4 , "Course"])
# print(df.loc[1, "Age"])
# print(df.loc[0 , "Name"])
# print(df.loc[2 ,"City"])
# print(df.loc[3  , "Marks"])


# import pandas as pd
# data = {
#     "Name"  :["Deepak" , "Rahul" , "Aman"  , "Rohit" , "Mohit" , "Karan"],
#     "Age" :[21 , 22 , 23, 21 , 22 , 23],
#     "City" :["Sangrur" , "Patiala" , "Mohali" , "Delhi" , "Chandigarh" , "Bathinda"],
#     "Course":["Gen ai" , "Python" , "Data Science" , "Gen ai" , "Python" , "Data Science"],
#     "Marks":[95 , 98 , 91 , 92 , 93, 96]
# }
# df =pd.DataFrame(data)
# print(df.loc[1:3])
# print("-------------------------------------")
# print(df.loc[: , ["Name" , "Course"]])
# print("-------------------------------------")
# print(df.loc[2:4 ,  ["Name" , "Marks"]])
# print("-------------------------------------")
# print(df.loc[: , ["Age"]])
# print("-------------------------------------")
# print(df.loc[: , ["Marks" , "City"]])
# print("The END")

# Boolean Filtering
# import pandas as pd
# data ={
#     "Name":["Deepak","Rahul","Aman","Rohit","Mohit"],
#     "Age":[21,22,20,23,24],
#     "Course":["Gen AI","Python","Data Science","Gen AI","Python"],
#     "Marks":[95,82,91,76,98]
# }
# df = pd.DataFrame(data)
# print(df[df["Marks"]>90])
# print("-------------------------------------")
# print(df[df["Age"]>20])
# print("-------------------------------------")
# print(df[df["Course"]=="Python"])
# print("-------------------------------------")
# print(df[df["Marks"]<90])
# print("-------------------------------------")
# print(df[df["Name"]=="Deepak"])
# print("The END")


# import pandas as pd
# data = {
#     "Name":["Deepak","Rahul","Aman","Rohit","Mohit"],
#     "Age":[21,22,20,23,24],
#     "Course":["Gen AI","Python","Data Science","Gen AI","Python"],
#     "Marks":[95,82,91,76,98]
# }
# df =pd.DataFrame(data)
# print(df[(df["Marks"]>90) & (df["Age"]>21)])
# print(df[(df["Name"]=="Deepak") & (df["Course"]== "Gen AI")])


import pandas as pd
data = {
    "Name": ["Deepak", "Rahul", "Aman", "Rohit", "Mohit", "Karan", "Priya", "Neha"],
    "Age": [21, 22, 20, 23, 24, 21, 22, 20],
    "City": ["Sangrur", "Patiala", "Mohali", "Delhi", "Chandigarh", "Bathinda", "Mohali", "Delhi"],
    "Course": ["Gen AI", "Python", "Data Science", "Gen AI", "Python", "Data Science", "Gen AI", "Python"],
    "Marks": [95, 82, 91, 76, 98, 88, 93, 79]
}
df = pd.DataFrame(data)
print(data)
print(df["City"]=="Mohali")
print(df[(df["Marks"]>90) & (df["Age"]>21)])
print(df[(df["Course"]=="Gen AI") & (df["Marks"]>=90)])
print(df[(df["City"]=="Delhi") & (df["Marks"]<80)])
print(df[(df["Age"]==21) & df("Course")=="Data Science"])
