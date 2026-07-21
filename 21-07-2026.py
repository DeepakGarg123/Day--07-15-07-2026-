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

import pandas as pd
df = {
    "name":["Deepak" , "Rahul" , "Aman" , "Rohit" , "Mohit" , "Karan" ,"Ajay"],
    "marks":[90 , 85 , 70 , 95 , 76 , 81 , 88]
}
df = pd.DataFrame(df)
print(df)
print(df.sample())
print(df.sample(3))
print(df.shape[0])
print(df.shape[1])