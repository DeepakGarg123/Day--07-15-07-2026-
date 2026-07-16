""" Day -08
try:
    a =10
    b =int(input("enter b:"))
    print(a/b)
except ValueError:
    print("enter numbers only")
except ZeroDivisionError:
    print("can't divide by zero")
else:
    print("Execution successfully")
finally:
    print("Program finished")

    file handling
file =open("attendance.txt" , "r")
print(file.read())
file.close

file =open("patients.csv" , "r")
for line in file:
    data = line.strip().split(",")
    print(data)
file.close()


file =open("students.txt" , "w")
file.write("Deepak")
file.close()
file =open("students.txt" , "a")
file.write("\nMohali")
file.close()
file =open("students.txt" , "a")
file.write("\nGEN AI")
file.close()
file =open("students.txt" , "r")
print(file.read())
file.close()


file =open("students.csv" , "r")
for line in file:
    data =line.strip().split(",")
    print(f"{data[1]} scored {data[2]} marks")
file.close()"""


# student ={
#     "name" :"Deepak",
#     "age" : 21 , 
#     "city" : "Sangrur",
#     "course": "gen ai"
# }
# print(student["name"])
# print(student["city"])
# print(student["age"])
# print(student["course"])
# student["age"]=22
# print([student])
# del student["age"]
# print([student])


