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

from math import sqrt
print(sqrt(16))






