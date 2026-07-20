"""# Exercise 1 – Company Details using **kwargs
 Create a function

 company_details(**kwargs)Accept:

 Company Name
 Location
 Employees
 CEO
 Founded Year
 Display all details using a loop.

 def company_details(**kwargs):
     for key,value in kwargs.items():
         print(key,":",value)
 company_details(company_name ="NetSquareSoftwares" , Location ="Mohali" , Employees = 6 , CEO = "Inderpal Sir" , Founded_Year=2025 )"""



"""Exercise 2 – Animal Inheritance
Create
Parent
Animal
Method

eat()
Child Classes

Dog
Cat
Elephant
Each child should have its own method.
Dog
bark()
Cat
meow()
Elephant
trumpet()
class Animal:
    def eat(self):
        print("animal is eating")
class Dog(Animal):
    def bark(self):
        print("the dog barks")
class Cat(Animal):
    def meow(self):
        print("the cat is meow")
class Elephant(Animal):
    def trumpet(self):
        print("the elephant trumpets")
d1 = Dog()
d1.bark()
d1.eat()
c1 = Cat()
c1.meow()
c1.eat()
e1 = Elephant()
e1.trumpet()
c1.eat()"""

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


"""Exercise 3 – Payment System (Polymorphism)
Create three classes.
CreditCard

UPI

Cash
Each class contains

pay()
Output
Paid using Credit Card

Paid using UPI

Paid using Cash
Call all methods using objects.

class CreditCard:
    def pay(self):
        print("paid using credit card")
class UPI:
    def pay(self):
        print("Paid using upi")
class Cash:
    def pay(self):
        print("paid using cash")
cc1 =CreditCard()
cc1.pay()
up1=UPI()
up1.pay()
cs1=Cash()
cs1.pay() """

"""Exercise 4 – Smart TV (Encapsulation)
Create class

SmartTV
Private Variable

__volumeInitially
20Methods

increase_volume()

decrease_volume()

show_volume()Volume should never become

Negative
Greater than 100

class SmartTV:
    def __init__(self):
        self.__volume = 20

    def increase_volume(self):
        if self.__volume < 100:
            self.__volume += 1
        else:
            print("Volume is already at maximum (100).")

    def decrease_volume(self):
        if self.__volume > 0:
            self.__volume -= 1
        else:
            print("Volume is already at minimum (0).")

    def show_volume(self):
        print("Current Volume:", self.__volume)"""


# Object Creation
tv = SmartTV()

tv.show_volume()

tv.increase_volume()
tv.increase_volume()
tv.show_volume()

tv.decrease_volume()
tv.show_volume()

"""Exercise 5 – Attendance Register (TXT)
Take names of 5 students.
Save them into
attendance.txtThen
Read the file.
Display all student names.

file =open("attendance.txt" , "r")
print(file.read())
file.close"""

"""Exercise 6 – Product CSV
Create
products.csv
Store
Product ID
Product Name
Price
Quantity
Read the CSV.
Calculate
Total Stock Value

Price × Quantity 

file =open("products.csv" , "r")
for line in file:
    data = line.strip().split(",")
    price = int(data[2])
    quantity = int(data[3])
    total_stock_value = price*quantity
    print(total_stock_value)
file.close()"""







"""Exercise 7 – Hospital Record System
Create class

Patient
Attributes

Patient ID
Name
Disease
Age
Method
display()
Create
5 patients
Save into
patients.csv
Read again and display.

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
file.close """




"""Exercise 8 – Movie Management System
Create class

Movie
Attributes

Movie ID
Movie Name
Rating
Language
Methods

display()

is_hit()
Rule
Rating >= 8

Hit Movie

Else

Average MovieStore
5 movies
Write to
movies.csvRead again and display all records.

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
file.close()"""
        


