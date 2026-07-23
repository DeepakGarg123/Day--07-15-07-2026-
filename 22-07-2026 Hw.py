# line plot

# import matplotlib.pyplot as plt
# days = [1,2,3,4,5]
# temperature = [32,35,34,36,38]
# plt.plot(days , temperature , color = "red" , marker = "o" , linestyle = "--" , markersize = 2 , linewidth = 3)
# plt.xlabel("Days")
# plt.ylabel("Temperature")
# plt.title("Temperature Report")
# plt.grid(True)
# plt.show()

# import matplotlib.pyplot as plt
# months = ["Jan","Feb","Mar","Apr","May"]
# iphone = [50,60,55,70,75]
# samsung = [45,58,60,68,72]
# plt.plot(months , iphone , label = "iphone")
# plt.plot(months , samsung , label = "samsung")
# plt.xlabel("iphone data")
# plt.ylabel("samsung data")
# plt.title("iphone vs samsung")
# plt.grid(True)
# plt.legend()
# plt.show()

# bar graph
# 2
# 🎯 Practice 1

# Khud ye code likh.

# Data:

# players = ["Virat", "Rohit", "Gill", "Rahul"]

# runs = [741, 510, 890, 520]

# Requirements:

# plt.bar()
# X Label → "Players"
# Y Label → "Runs"
# Title → "IPL Runs"
# Grid → True
# Color → "orange"
# Edge Color → "black"
# Width → 0.5

# import matplotlib.pyplot as plt

# players = ["Virat", "Rohit", "Gill", "Rahul"]

# runs = [741, 510, 890, 520]

# plt.bar(players , runs , color = "red" , edgecolor ="black" , width = 0.5 )
# plt.xlabel("Players")
# plt.ylabel("Runs")
# plt.title("IPL RUNS")
# plt.grid(True)
# plt.show()



# import matplotlib.pyplot as plt

# players = ["Virat", "Rohit", "Gill", "Rahul"]

# runs = [741, 510, 890, 520]

# plt.barh(players , runs , color = "purple" , edgecolor ="black" )
# plt.xlabel("runs")
# plt.ylabel("players")
# plt.title(" Horizontal IPL RUNS")
# plt.grid(True)
# plt.show()


# scatter plot


# 🎯 Practice

# Ye code khud likh:

# age = [18,20,22,24,26]

# weight = [55,60,65,70,75]

# Requirements:

# plt.scatter()
# X Label = "Age"
# Y Label = "Weight"
# Title = "Age vs Weight"
# Grid = True

# import matplotlib.pyplot as plt

# age =[18 , 20 , 22 , 24 , 26]
# weight = [55 , 60 , 65 , 70 , 75]
# plt.scatter(age , weight)
# plt.xlabel("Age")
# plt.ylabel("Weight")
# plt.title("Age vs weight")
# plt.grid(True)
# plt.show()

# 🎯 Mini Practice

# Ye khud likh:

# experience = [1,2,3,4,5]

# salary = [25000,35000,45000,55000,70000]

# Requirements

# Scatter Plot
# Color = "blue"
# Size = 150
# X Label = "Experience"
# Y Label = "Salary"
# Title = "Experience vs Salary"

# import matplotlib.pyplot as plt
# experience = [1,2,3,4,5]
# salary = [25000 , 35000 , 45000 , 55000 , 70000]
# plt.scatter(experience , salary , color = "blue" , s=150)
# plt.xlabel("experience")
# plt.ylabel("salary")
# plt.title("Experience vs salary")
# plt.grid(True)
# plt.show()

# pie chart

# 🎯 Practice

# Khud ye banao.

# payment = [
#     "UPI",
#     "Cash",
#     "Card",
#     "Net Banking"
# ]

# transactions = [
#     45,
#     25,
#     20,
#     10
# ]

# Requirements:

# Pie Chart
# Labels
# Colors (apni choice)
# Percentage dikhana
# Shadow = True
# Start Angle = 90
# Title = "Payment Mode Distribution"

# import matplotlib.pyplot as plt
# payment = ["cash" , "upi" ,"card" , "net banking"]
# transactions = [45,25,20,10]
# colors = ["green" ,"white" , "black" , "orange" ]
# plt.pie(transactions , labels = payment ,    colors = colors , autopct="%1.1f%%" , shadow=True , startangle=90)
# plt.title("Payment mode distribution")
# plt.show()



# import matplotlib.pyplot as plt

# payment = ["Cash", "UPI", "Card", "Net Banking"]
# transactions = [45, 25, 20, 10]

# colors = ["green", "yellow", "blue", "orange"]

# plt.pie(
#     transactions,
#     labels=payment,
#     colors=colors,
#     autopct="%1.1f%%",
#     shadow=True,
#     startangle=90
# )

# plt.title("Payment Mode Distribution")

# plt.show()

# 🥧 Practice Question - Pie Chart

# Ek coaching institute me students ne alag-alag courses join kiye hain.

# Data:

# courses = [
#     "Python",
#     "Gen AI",
#     "Data Science",
#     "Web Development",
#     "Java"
# ]

# students = [
#     50,
#     30,
#     20,
#     15,
#     10
# ]
# Requirements
# Pie Chart banao.
# Labels dikhne chahiye.
# Percentage dikhna chahiye.
# Colors apni choice ke use karo.
# Shadow add karo.
# Pie ko 90° se start karo.
# Title do:
# Course Distribution

# import matplotlib.pyplot as plt
# courses = ["Python" , "Gen AI" , "Data Science" , "Web Development" ,"Java"]
# students = [50 , 30 , 20 , 15 , 10]
# colors = ["green" , "yellow" , "blue" , "orange"]
# plt.pie(students , labels=courses , autopct="%1.1f%%" , shadow=True , startangle=90)
# plt.title("Course distribution")
# plt.show()

# histogram

import matplotlib.pyplot as plt
ages = [
18,
19,
20,
21,
22,
22,
23,
24,
25,
26,
27,
28,
29,
30,
31,
32,
33
]
plt.hist(ages , bins = 6 , color = "green" , edgecolor = "black")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.title("Age distribution")
plt.grid(axis="y")
plt.show()
