# learning json
# json.dump for writing the data and for storing the data in json file
"""import json
student ={
    "name" : "Deepak" ,
    "age" :21,
    "city" :"Mohali"
}
file =open("student.json" ,"w" ,)
json.dump(student,file , indent=4)
file.close() """
# json.load for reading the file 
"""
import json
file =open("student.json" , "r")
data = json.load(file)
print(data)
file.close()
"""

"""import json
employee = {
    "id":101,
    "name":"Rahul",
    "Salary":50000
}
with open("employees.json" ,"w") as file:
    json.dump(employee,file , indent=4)

import json
with open("employees.json" ,"r") as file:
    data = json.load(file)
    print(data)"""
"""
from math import *
print(factorial(6))

from math import factorial
print(factorial(4))"""


"""
import main
print(main.add(10,2))
print(main.sub(10,2))
print(main.mult(10,2))"""

"""import numpy as np
arr = np.array([10,20,30])
print(arr[1:])"""

# 2D array

# import numpy as np
# arr =([
#     ([10,20,30]),
#     ([50,60,70])
# ])
# print(arr[0][2])

# Q1. Print the complete array.
# Q2. Print the second row.
# Q3. Print the third column.
# Q4. Print the element 50 using indexing.
# Q5. Print the last element.
# Q6. Multiply the entire array by 2.
# Q7. Add 10 to every element.
# Q8. Print the shape of the array.
# Q9. Print the size of the array.
# Q10. Print only the first two rows.

# import numpy as np
# arr = np.array([
#     [10,20,30],
#     [40,50,60],
#     [70,80,90]
# ])
# print(arr)
# print(arr[1])
# print(arr[:,2])
# print(arr[1][1])
# print(arr[2][2])
# print(arr*2)
# print(arr+10)
# print(arr.shape)
# print(arr.size)
# print(arr[0:2])

# First column
# Last row
# Middle element
# Last two rows
# First two columns
# Multiply array by 5
# Add 100 to every element

"""import numpy as np
arr = np.array([
    [2,4,6],
    [8,10,12],
    [14,16,18]
])

print(arr[:,1])  #print(arr[Rows , Columns])
print(arr[2])
print(arr[])"""

"""import json
student = {
    "name" :"Deepak",
    "age" : 21,
    "city" : "Sangrur"
}
with open("students.json" , "w") as file:
    json.dump(student , file , indent = 4 )

import json
with open("students.json" , "r") as file:
    data = json.load(file)
    print(data)
"""
"""import json
product = {
    "id" :101,
    "name" :"Laptop",
    "price":65000
}
with open("product.json" , "w") as file:
    json.dump(product , file , indent=4)

with open("product.json" , "r") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["price"])"""


"""import json
course ={
    "name": "Rahul",
    "course": "Python",
    "duration": "6 Months",
    "fees": 25000
}
with open("course.json" , "w") as file:
    json.dump(course , file , indent=4)

with open("course.json" , "r") as file:
    data = json.load(file)
    print("Rahul is learning" ,data["course"])
    print("Course duration:" , data["duration"])
    print("Fees:" ,data["fees"])"""

import json
employee ={
    "id" :201,
    "name" :"Aman",
    "salary" :50000,
    "department" :"AI"
}    
with open("employee.json" , "w") as file:
    json.dump(employee , file , indent=4)
    
