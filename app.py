# Exercise 10 – Bank Account
# Create class
# BankAccount
# Attributes

# Account Holder
# Balance
# Methods
# deposit(amount)

# withdraw(amount)

# show_balance()If withdrawal amount exceeds balance
# Display
# Insufficient Balance

# class bankaccount:
#     def __init__(self , accountholder , balance):
#         self.accountholder = accountholder
#         self.balance = balance
#     def deposit(self , amount):
#         self.balance+=amount
#         print(f"deposit:{self.balance}")
#     def withdraw(self ,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"withdraw:{self.balance}")
#         else:
#             print("insufficeint balance")
#     def show_balance(self):
#         print(f"balance:{self.balance}")
# b1 =bankaccount("Deepak" , 5000)
# b1.show_balance()
# b1.deposit(2000)
# b1.show_balance()
# b1.withdraw(500)
# b1.show_balance()
        





# Exercise 11 – Student Management System
# Create class
# Student

# Store
# Name
# Roll Number
# Course
# Marks
# Create 5 student objects.
# Store all objects inside a list.
# Display every student's information using a loop.

# class student:
#     def __init__(self , name , rollnumber , course , marks):
#         self.name =name
#         self.rollnumber =rollnumber
#         self.course=course
#         self.marks=marks
#     def display(self):
#         print(f"name :{self.name}")
#         print(f"roll number :{self.rollnumber}")
#         print(f"course:{self.course}")
#         print(f"marks:{self.marks}")
#         print("---------------------------")
# s1 = student("Deepak" ,925 , "Gen ai" , 90)
# s2 = student("rahul" , 905 , "Gen ai" , 85)
# s3 = student("Mohit" , 965 , "gen ai" , 95)
# s4 = student("rohit" , 945 , "gen ai" , 93)
# s5 = student("somit" , 955 , "gen ai" , 91)
# students = [s1,s2,s3,s4,s5]
# for student in students:
#     student.display()



# Exercise 12 – Library Management System
# Create class
# Book
# Attributes

# Book ID
# Title
# Author
# Price
# Store 5 books in a list.
# Display all books.
# Search a book using its ID.

# class Book:
#     def __init__(self , book_id , title , author  , price):
#         self.book__id =book_id
#         self.title =title
#         self.author=author
#         self.price=price
#     def display(self):
#         print(f"book:{self.book__id}")
#         print(f"title:{self.title}")
#         print(f"author:{self.author}")
#         print(f"price:{self.price}")
#         print("-----------------------------")
# b1=Book(12345 , "fnkwsnfk" , "smfkm" , 2000)
# b2=Book(6789 , "ajcbj" , "sbvsh" , 9000)
# b3=Book(101112 , "ndvkjnkja" , "sndbcvjbsnj" , 1000)
# b4=Book(1314 , "adsksankv" , "swhfu" , 7000)
# b5=Book(1516 , "dnjsn" , "sjfnjb" , 5000)
# books =[b1,b2,b3,b4,b5]
# for book in books:
#     book.display()


# Exercise 13 – Employee Management System
# Create class
# EmployeeAttributes

# ID
# Name
# Department
# Salary
# Store 5 employees in a list.
# Display only employees whose salary is greater than ₹50,000.

# Exercise 14 – Inventory System
# Create class
# ProductAttributes

# Product ID
# Product Name
# Quantity
# Price
# Methods
# display()

# stock_value()stock_value() should calculate:
# Quantity × PriceStore multiple products and calculate the total inventory value.

# Exercise 15 – School Management System 
# Create class
# Student
# Attributes

# Roll Number
# Name
# Course
# Marks
# Methods
# display()

# grade()Grade Rules
# 90+  → A
# 75–89 → B
# 50–74 → C
# Below 50 → FailCreate 5 students.
# Store all objects in a list.
# Display

# Student Details
# Grade
# Highest Marks Student
# Average Marks of all Students

# class Student:
#     def __init__(self , name , course , marks):
#         self.name = name
#         self.course =course
#         self.marks = marks
#     def display(self):
#         print(f"name : {self.name}")
#         print(f"course : {self.course}")
#         print(f"marks :{self.marks}")
#     def grade(self):
#         if self.marks>=90:
#             print("Grade A")
#         elif self.marks>=75 and self.marks<=89:
#             print("grade B")
#         elif self.marks>=50 and self.marks<=74:
#             print("Grade C")
#         else:
#             print("Fail")
# s1 =Student("Deepak" ,"Gen ai" ,89)
# s2 =Student("rahul" ,"Gen ai" ,39)
# s3 =Student("bahrat" ,"Gen ai" ,59)
# s4 =Student("arman" ,"Gen ai" ,69)
# s5 =Student("dabid" ,"Gen ai" ,79)
# students =[s1,s2,s3,s4,s5]
# for student in students:
#     student.display()
#     student.grade()

# Exercise 1 – Company Details using **kwargs
# Create a function

# company_details(**kwargs)Accept:

# Company Name
# Location
# Employees
# CEO
# Founded Year
# Display all details using a loop.

# def company_details(**kwargs):
#     for key,value in kwargs.items():
#         print(key,":",value)
# company_details(company_name ="NetSquareSoftwares" , Location ="Mohali" , Employees = 6 , CEO = "Inderpal Sir" , Founded_Year=2025 )



# Exercise 2 – Animal Inheritance
# Create
# Parent
# Animal
# Method

# eat()
# Child Classes

# Dog
# Cat
# Elephant
# Each child should have its own method.
# Dog
# bark()
# Cat
# meow()
# Elephant
# trumpet()
# class Animal:
#     def eat(self):
#         print("animal is eating")
# class Dog(Animal):
#     def bark(self):
#         print("the dog barks")
# class Cat(Animal):
#     def meow(self):
#         print("the cat is meow")
# class Elephant(Animal):
#     def trumpet(self):
#         print("the elephant trumpets")
# d1 = Dog()
# d1.bark()
# d1.eat()
# c1 = Cat()
# c1.meow()
# c1.eat()
# e1 = Elephant()
# e1.trumpet()
# c1.eat()

# class vehicle:
#     def start(self):
#         print("vehicle started")
# class car(vehicle):
#     def drive(self):
#         print("car is driving")
# class bike(vehicle):
#     def ride(self):
#         print("bike is riding")
# class Truck(vehicle):
#     def load(self):
#         print("the truck is loading goods")
# c1=car()
# c1.start()
# c1.drive()
# b1=bike()
# b1.start()
# b1.ride()
# t1=Truck()
# t1.start()
# t1.load()


# Exercise 3 – Payment System (Polymorphism)
# Create three classes.
# CreditCard

# UPI

# Cash
# Each class contains

# pay()
# Output
# Paid using Credit Card

# Paid using UPI

# Paid using Cash
# Call all methods using objects.

# class CreditCard:
#     def pay(self):
#         print("paid using credit card")
# class UPI:
#     def pay(self):
#         print("Paid using upi")
# class Cash:
#     def pay(self):
#         print("paid using cash")
# cc1 =CreditCard()
# cc1.pay()
# up1=UPI()
# up1.pay()
# cs1=Cash()
# cs1.pay() 

# Exercise 4 – Smart TV (Encapsulation)
# Create class

# SmartTV
# Private Variable

# __volumeInitially
# 20Methods

# increase_volume()

# decrease_volume()

# show_volume()Volume should never become

# Negative
# Greater than 100


# Exercise 5 – Attendance Register (TXT)
# Take names of 5 students.
# Save them into
# attendance.txtThen
# Read the file.
# Display all student names.
# file =open("attendance.txt" , "r")
# print(file.read())
# file.close
# Exercise 6 – Product CSV
# Create
# products.csv
# Store
# Product ID
# Product Name
# Price
# Quantity
# Read the CSV.
# Calculate
# Total Stock Value

# Price × Quantity




# Exercise 7 – Hospital Record System
# Create class

# Patient
# Attributes

# Patient ID
# Name
# Disease
# Age
# Method
# display()
# Create
# 5 patients
# Save into
# patients.csv
# Read again and display.

class Patient:
    def __init__(self , patient_id  , name , disease , age):
        self.patient_id = patient_id
        self.name =name
        self.disease = disease
        self.age =age
    def display(self):
        print(f"patient_id:{self.patient_id}")
        print(f"name:{self.name}")
        print(f"disease:{self.disease}")
        print(f'age:{self.age}')
p1=Patient(101 , "Deepak" , "all ok" , 22)
file =open("patients.csv" ,"r")
print(file.read())
file.close 




# Exercise 8 – Movie Management System
# Create class

# Movie
# Attributes

# Movie ID
# Movie Name
# Rating
# Language
# Methods

# display()

# is_hit()
# Rule
# Rating >= 8

# Hit Movie

# Else

# Average MovieStore
# 5 movies
# Write to
# movies.csvRead again and display all records.

class Movie:
    def __init__(self , movie_id , movie_name , rating , language):
        self.movie_id=movie_id
        self.movie_name=movie_name
        self.rating=rating
        self.Language =language
    def display(self):
        print(f"movieid:{self.movie_id}")
        print(f"moviename :{self.movie_name}")
        print(f"rating:{self.rating}")
        print(f'languae:{self.Language}')
    def is_hit(self):
        if self.rating>=8:
            print("Hit movie")
        else:
            print("avergae movie")
m1 =Movie(101 , "goat" , 9 , "hindi")
file = open("movies.csv" ,"r")
print(file.read())
file.close


