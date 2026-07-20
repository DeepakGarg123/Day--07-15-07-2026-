"""import json
student = {
    "name" :"Deepak" ,
    "course" : "Gen ai" , 
    "duration" :"6 months"
}
with open("students.json" , "w") as file:
    json.dump(student , file , indent=4)

with open("students.json" , "r") as file:
    data = json.load(file)
    print(data)
    print(f"{data["name"]} is learning {data["course"]}")
    print(f"duration : {data["duration"]}")

import json
employee = {
    "id":101,
    "name":"Rahul",
    "salary":50000
}
with open("employees.json" , "w") as file:
    json.dump(employee , file , indent=4)

with open("employees.json" ,"r") as file:
    data = json.load(file)
    updated_salary = print(data["salary" + 10000])
    print(updated_salary)
"""
# create a function :
"""def even_odd(num):
    if num%2==0:
        print("the number is even")
    else :
        print("the number is odd")

even_odd(10)
even_odd(7)"""

"""def largest(a,b,c):
    if a>b and a>c:
        print(a)
    elif b>a and b>c:
        print(b)
    elif c>a and c>b:
        print(c)

largest(5,10,15) """

# for loops

# Print numbers from 1 to 20.
# for i in range(1,21):
#     print(i)

# Print even numbers from 1 to 50.
# for i in range(1,51):
#     if i%2==0:
#         print(i)

# # Print odd numbers from 1 to 50.
# for i in range(1,51):
#     if i%2!=0:
#         print(i)

# Print the multiplication table of 7.
# for i in range(1,11):
#     print(i*7)
# Find the sum of numbers from 1 to 100.

# Question 2

# # 1 se 50 tak sirf wo numbers print kar jo 5 se divide hote hain.


# for i in range(1,51):
#     if i%5==0:
#         print(i)

# Question 3 (Thoda Sochna Padega)

# 1 se 100 tak sirf wo numbers print karo jo:

# 3 se divisible ho
# Aur 5 se bhi divisible ho.

# Example output:

# 15
# 30
# 45
# 60
# 75
# 90


# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)



# # Question 4

# # 1 se 50 tak sirf wo numbers print karo jo:

# # Even ho
# # Aur 10 se chhote ho.

# # Expected Output:

# # 2
# # 4
# # 6
# # 8

# for i in range(1,51):
#     if i%2==0 and i<10:
#         print(i)

# # Question 5

# # 1 se 30 tak wo numbers print karo jo:

# # 2 se divisible ya (or) 3 se divisible ho.

# for i in range(1,31):
#     if i%2==0 or i%3==0:
#         print(i)

# Question 6 ⭐

# 1 se 100 tak jitne bhi numbers hain...

# Unka sum nikalo.

# Expected Output

# 5050

# Hint

# sum = 0

# sum = 0
# for i in range(1,101):
#     sum = sum+i
# print(sum)

# Ye code khud likh.

# 1 se 10 tak sirf even numbers ka sum nikal.

# Expected Output:

# 30

# (2 + 4 + 6 + 8 + 10 = 30)

# sum  = 0
# for i in range(1,11):
#     if i%2==0:
#         sum = sum+i
# print(sum)

# name = "Deepak Garg"
# for i in name:
#     if i!="a" and i!="e" and i!="i" and i!="o" and i!="u":
#         print(i)

# count =0
# name = "Deeepak"
# vowels ="aeiou"
# for i in name:
#         if i in vowels:
#                 count=count+1
# print(count)

# Ab is string ke liye code likh:

# name = "Deepak Garg"

# Question:

# Vowels kitne hain?
# Consonants kitne hain?

# Expected:

# Vowel Count = 4
# Consonant Count = 7

# ⚠️ Space (" ") ko consonant mat count karna.

# count =0
# name ="Deepak Garg"
# vowels ="aeiou"
# for i in name:
#     if i not in vowels and i!=" ":
#         count =count+1
# print(count)

# 🟢 Level 1 (Easy)
# Q1

# Print numbers from 1 to 20.
# for i in range(1,21):
#     print(i)

# Q2

# Print numbers from 20 to 1.
# for i in range (20,0,-1):
#     print(i)

# Q3

# Print only even numbers from 1 to 50.
# for i in range(1,51):
#     if i%2==0:
#         print(i)

# Q4

# Print only odd numbers from 1 to 50.
# for i in range(1,51):
#     if i%2!=0:
#          print(i)
     
# Q5

# Print numbers from 1 to 100 that are divisible by 5.
# for i in range(1,101):
#     if i%5==0:
#         print(i)
# Q6

# Print numbers from 1 to 100 divisible by both 3 and 5.
# for i in range(1,101):
#     if i%3==0 and i%5==0:
#         print(i)
# 🟡 Level 2 (Sum)
# Q7

# Find the sum of numbers from 1 to 10.
# total =0
# for i in range(1,11):
#     total=total+i
# print(total)
# Expected Output:

# 55
# Q8

# Find the sum of even numbers from 1 to 20.
# total =0
# for i in range(1,21):
#     if i%2==0:
#         total = total +i
# print(total)
# Q9

# Find the sum of odd numbers from 1 to 20.
# total =0
# for i in range(1,21):
#     if i%2!=0:
#         total = total+i
# print(total)
# Q10

# Find the sum of numbers divisible by 5 from 1 to 100.
total = 0
for i in range(1,101):
    if i%5==0:
        

# 🟠 Level 3 (Count)
# Q11

# Count even numbers between 1 and 100.

# Q12

# Count odd numbers between 1 and 100.

# Q13

# Count numbers divisible by 7 between 1 and 100.

# Q14

# Count numbers divisible by 3 and 5 between 1 and 100.

# 🔵 Level 4 (Strings)
# name = "Deepak"
# Q15

# Print every character.

# Q16

# Print only vowels.

# Expected Output:

# e
# e
# a
# Q17

# Print only consonants.

# Expected Output:

# D
# p
# k
# Q18

# Count vowels.

# Expected Output:

# 3
# Q19

# Count consonants.

# Expected Output:

# 3
# 🟣 Level 5 (Real Logic)
# name = "Python Programming"
# Q20

# Count vowels.

# Q21

# Count consonants.

# Q22

# Count spaces.

# Expected Output:

# 1
# Q23

# Count how many times the letter "a" appears.

# Q24 ⭐⭐⭐

# Count uppercase letters.

# Example:

# name = "Deepak GARG"

# Expected Output:

# 5

# (D, G, A, R, G)

# Q25 ⭐⭐⭐⭐ (Interview Favourite)
# name = "Deepak123"

# Count:

# Letters
# Digits

# Expected Output:

# Letters = 7
# Digits = 3