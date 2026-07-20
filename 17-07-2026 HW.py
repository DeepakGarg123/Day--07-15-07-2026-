"""Section 1: OOP (10 Marks)
Q1

Create a class Student.

Attributes:

name
age

Method:

display()

Output:

Name: Deepak
Age: 21

# solution

class Student:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    def display(self):
        print("Name :" , self.name)
        print("Age :" , self.age)
d1 = Student("Deepak" , 21)
d1.display()
"""
"""Create a class Calculator.

Methods:

add()
subtract()

Create an object and print:

Sum = 80
Difference = 20

class Calculator:
    def __init__(self , num1 , num2):
        self.num1  = num1
        self.num2 = num2
    def add(self):
        print("Sum = " ,self.num1 + self.num2)
    def subtract(self):
        print("difference = " ,self.num1 - self.num2)
add1 =Calculator(50 , 30)
add1.add()
add1.subtract()"""

"""Q3

Create a file named attendance.txt.

Store:

Deepak
Rahul
Mohit

Now read the file and print all names one by one.

file =open("attendance.txt" , "w")
file.write("Deepak\n")
file.write("Rahul\n")
file.write("Mohit\n")
file.close()

file =open("attendance.txt" ,"r")
for line in file:
    print(line.strip())
file.close()"""

"""Q4

Read attendance.txt.

Count how many students are present.

Output:

Total Students = 3
"""

# count =0
# with open("attendance.txt" , "r") as file:
#     for line in file:
#         count+=1

# print("Total Students = " ,count)
"""Create students.csv

101,Deepak,90
102,Rahul,85
103,Mohit,95
Q5

Print:

Deepak scored 90
Rahul scored 85
Mohit scored 95
"""

# with open("students.csv" , "r") as file:
#     for line in file:
#         data = line.strip().split(",")
#         print(f"{data[1]}")

# for i in range(1,6):
#     print(i*2)
"""Q1

Print the following output:

Rahul works in HR
Deepak works in AI
Mohit works in Python
Aman works in Data Analyst
"""

"""
import csv
with open("employees.csv" , "r") as file:
    for line in file:
        data =line.strip().split(",")
        print(f"{data[1]} works in {data[2]}")
"""

