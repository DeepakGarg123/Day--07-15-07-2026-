"""Exercise 1 – IPL Performance Dashboard
Create a CSV file named ipl_stats.csv with the following columns:

Player Name
Team
Matches
Runs
Strike Rate
Tasks
1. Read the CSV into a DataFrame.
2. Display:
Top 5 players by runs.
Players with Strike Rate > 140.
Average runs scored.
Player with maximum runs.
3. Create:
Bar Chart → Player vs Runs
Scatter Plot → Matches vs Runs
Histogram → Strike Rate Distribution

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("ipl_stats.csv")
print(df)
print(df.sort_values(by="Runs" , ascending=False).head(5))
print(df[df["StrikeRate"]>140])
print(df["Runs"].mean())
print(df.sort_values(by="Runs" , ascending=False).head(1))
plt.bar(df["PlayerName"] , df["Runs"])
plt.xlabel("player name")
plt.ylabel("Runs Scored")
plt.title("Player Vs Runs")
plt.grid(True)
plt.show()

plt.scatter(df["Matches"] , df["Runs"])
plt.xlabel("Matches")
plt.ylabel("Runs")
plt.title("Matches vs Runs")
plt.grid(True)
plt.show()

plt.hist(df["StrikeRate"] , bins= 3 ,color = "green" , edgecolor = "black")
plt.xlabel("Strike Rate")
plt.ylabel("Frequency")
plt.title("Strike Rate Distribution")
plt.show()
"""



"""Exercise 2 – Flight Ticket Analytics
Create a DataFrame containing:

Flight Number
Source
Destination
Ticket Price
Seats Available
Tasks

Display flights costing more than ₹7000.
Display flights with seats less than 25.
Find:
Highest ticket price
Lowest ticket price
Average ticket price

Create:
Pie Chart → Destination Distribution
Bar Chart → Ticket Price

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "Flight number":[101 , 102 , 103],
    "Source" :["Delhi" ,"Mumbai" , "Pune"],
    "Destination":["Mumbai" , "Delhi" , "Chandigarh"],
    "Ticket price":[10000 , 15000 , 8000], 
    "Seats Available":[20 , 21 , 1 ]
}
df = pd.DataFrame(data)
print(df["Ticket price"].max())
print(df["Ticket price"].min())
print(df["Ticket price"].mean())

plt.bar(df["Flight number"] ,df["Ticket price"] , color = "skyblue" ,edgecolor = "black")
plt.xlabel("Flight  number")
plt.ylabel("Price Ticket")
plt.title("Flight vs Tickets")
plt.grid(True)
plt.show()
"""


"""Exercise 3 – Smartphone Market Analysis
Create a CSV file:
Columns

Brand
Model
RAM
Storage
Battery
Price
Tasks

Phones with RAM ≥ 8GB
Phones with Price < ₹30,000
Highest battery capacity
Average price
Visualization

Scatter Plot → RAM vs Price
Histogram → Battery Capacity
Bar Chart → Brand vs Price

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("phones.csv")
print(df[(df["Ram"]>=8)])
print(df[(df["Price"]<30000)])
print(df["Battery"].max)
print(df["Price"].mean())
plt.scatter(df["Ram"] , df["Price"] )
plt.xlabel("Ram")
plt.ylabel("Price")
plt.grid(True)
plt.title("Ram vs Price")
plt.show()
"""


"""Exercise 4 – Online Shopping Orders
Create orders.csv
Columns

Order ID
Customer
Product
Quantity
Price
Tasks
Create a new column

Total = Quantity × PriceDisplay

Highest order value
Lowest order value
Average order value
Orders above ₹5000
Visualization

Line Plot → Order Value
Pie Chart → Product Distribution

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("orders.csv")
df["Total"] = df["Quantity"]*df["Price"]
print(df["Total"])
print(df["Total"].max())
print(df["Total"].min())
print(df["Total"].mean())
print(df[df["Total"]>5000])
plt.plot(df["Order ID"] ,df["Total"])
plt.xlabel("Order")
plt.ylabel("order value")
plt.title("order value")
plt.grid(True)
plt.show()
"""


"""Exercise 5 – Weather Monitoring System
Create a DataFrame
Columns

City
Temperature
Humidity
Rainfall
Tasks
Display

Temperature > 35°C
Humidity > 70%
Average Rainfall
Visualization

Scatter Plot → Temperature vs Humidity
Line Plot → Rainfall
Histogram → Temperature

import pandas as pd
import matplotlib.pyplot as plt
data = {
    "City": ["Mumbai", "Delhi", "Chennai", "Kolkata", "Bengaluru", "Hyderabad"],
    "Temperature": [32.5, 41.2, 36.8, 34.0, 28.5, 38.0],
    "Humidity": [85, 40, 75, 80, 55, 45],
    "Rainfall": [12.4, 2.1, 8.5, 15.0, 5.2, 1.8]
}
df = pd.DataFrame(data)
print(df[(df["Temperature"])>35])
print(df[(df["Humidity"])>70])
print(df["Rainfall"].mean())
plt.scatter(df["Temperature"] , df["Humidity"])
plt.xlabel("Temperature")
plt.ylabel("Humidity")
plt.title("Temperature vs Humidity")
plt.grid(True)
plt.show()
"""


"""Exercise 6 – Movie Streaming Analytics
Create
Columns

Movie
Genre
Duration
Rating
Release Year
Tasks
Display

Movies after 2020
Rating greater than 8
Longest movie
Shortest movie
Average duration
Visualization

Pie Chart → Genre Distribution
Histogram → Ratings
Bar Chart → Movie Ratings


import pandas as pd
import matplotlib.pyplot as plt
data = {
'Movie': ['Inception Prime', 'Sci-Fi Nexus', 'Retro Comedy', 'Cyber Thriller', 'Midnight Drama', 'The Final Quest'],
'Genre': ['Sci-Fi', 'Sci-Fi', 'Comedy', 'Thriller', 'Drama', 'Action'],
'Duration':[148, 115, 95, 120, 88, 162],
'Rating': [8.8, 6.2, 7.5, 8.1, 5.9, 8.4],
'Release Year': [2010, 2021, 2019, 2023, 2022, 2025]
}
df = pd.DataFrame(data)
print(df[(df["Release Year"])>2020])
print(df[(df["Rating"])>8])
# Doubt
# Doubt
print(df["Duration"].mean())
plt.hist(df["Rating"] , bins=3 , edgecolor = "black" )
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.title("Rating vs Frequency")
plt.grid(True)
plt.show()
"""

"""Exercise 7 – Gym Membership Analysis
Create
Columns

Member Name
Age
Weight
Membership Plan
Monthly Fee
Tasks
Display

Members above 30 years
Premium members only
Average fee
Maximum fee
Visualization

Scatter Plot → Age vs Weight
Pie Chart → Membership Plan
Bar Chart → Monthly Fee

import pandas as pd
import matplotlib.pyplot as plt
data = {
    'Member Name': ['Rahul', 'Ananya', 'Vikram', 'Sneha', 'Kabir', 'Diya'],
    'Age': [20 , 21 , 23 , 32 , 34 , 35],
    'Weight': [68.5, 62.0, 81.2, 58.4, 76.0, 54.8],
    'Membership Plan': ['Basic', 'Premium', 'Standard', 'Premium', 'Basic', 'Premium'],
    'Monthly Fee': [1200, 2500, 1800, 2500, 1200, 2500]
}
df = pd.DataFrame(data)
print(df[(df["Age"])>30])
print(df[(df["Membership Plan"])=="Premium"])
print(df["Monthly Fee"].mean())
print(df["Monthly Fee"].max())
plt.scatter(df["Age"] , df["Weight"] , color = "skyblue" , edgecolors="black")
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.grid()
plt.show()
plt.bar(df["Member Name"] ,df["Monthly Fee"])
plt.xlabel("Member Name")
plt.ylabel("Monthly Fee")
plt.title("Gym Fees")
plt.grid(True)
plt.show()
"""



"""Exercise 8 – University Admission Report
Create CSV
Columns

Student Name
Course
Percentage
City
Tasks
Display

Percentage above 80
Students from Delhi
Average percentage
Number of students per course
Visualization

Pie Chart → Course Distribution
Bar Chart → Student Percentage

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Admissions.csv")
print(df[(df["Percentage"])>80])
print(df[(df["City"])=="Delhi"])
print(df["Percentage"].mean())
# Doubt
plt.bar(df["Student Name"] , df["Percentage"])
plt.xlabel("Student Name")
plt.ylabel("Percentage")
plt.title("Student Percentage")
plt.grid(True)
plt.show()
"""


"""Exercise 9 – Restaurant Sales Dashboard
Create CSV
Columns

Order ID
Food Item
Quantity
Price
Payment Mode
Tasks
Create

Total = Quantity × PriceDisplay

Total Revenue
Most Ordered Item
Highest Bill
Lowest Bill
Average Bill
Visualization

Pie Chart → Payment Mode
Bar Chart → Food Sales
Histogram → Bill Distribution

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("Sales.csv")
df["Total"] = df["Quantity"]*df["Price"]
print(df["Total"].sum())
#Doubt
print(df["Total"].max())
print(df["Total"].min())
print(df["Total"].mean())
food_sales = df.groupby("Food Item")["Quantity"].sum()
plt.hist(df["Total"], bins = 3 , edgecolor = "black")
plt.xlabel("bill")
plt.ylabel("Frequency")
plt.title("Bill distribution")
plt.grid(True)
plt.show()
"""

"""Exercise 10 – World Population Analytics (Mini Project)
Create a DataFrame
Columns

Country
Population
Literacy Rate
GDP
Continent
Tasks
1. Display countries with population greater than 100 million.
2. Display countries with literacy greater than 90%.
3. Find:
Highest GDP
Lowest GDP
Average GDP
4. Handle missing values using:
fillna()
dropna()
5. Export the cleaned data to:

world_population_cleaned.csv6. Create:

Bar Chart → Country vs GDP
Pie Chart → Continent Distribution
Scatter Plot → Population vs GDP
Histogram → Literacy Rate


import pandas as pd
import matplotlib.pyplot as plt
data = {
     'Country': ['India', 'USA', 'Brazil', 'Nigeria', 'Germany', 'Japan', 'Egypt', 'Australia'],
    'Population' : [ 1430,1412,340,216,84,123,40,27,],
    'Literacy Rate': [77.7, 99.0, 93.5, 62.0, 99.0, None, 73.1, 99.0], 
    'GDP': [3.73, 26.95, 2.13, 0.36, 4.43, 4.23, None, 1.69],         
    'Continent': ['Asia', 'North America', 'South America', 'Africa', 'Europe', 'Asia', 'Africa', 'Oceania']
}
df  = pd.DataFrame(data)
print(df["GDP"].max())
print(df["GDP"].min())
print(df["GDP"].mean())
plt.bar(df["Country"] ,df["GDP"])
plt.xlabel("Country")
plt.ylabel("GDP")
plt.title("Country vs GDP")
plt.grid(True)
plt.show()
plt.scatter(df["Population"] , df["GDP"])
plt.xlabel("Population")
plt.ylabel("GDP")
plt.title("Country vs GDP")
plt.grid(True)
plt.show()
plt.hist(df["Literacy Rate"] , bins = 4 , edgecolor = "black" , color = "skyblue")
plt.xlabel("Literacy Rate")
plt.ylabel("Frequency")
plt.title("Literacy Rate")
plt.grid(True)
plt.show()
"""

"""Final Challenge (Interview Level)
Netflix Analytics Dashboard
Create a dataset with at least 25 movies.
Columns:

Movie Name
Genre
Rating
Duration
Release Year
Language
Views (Millions)
Perform:

Clean missing values.
Filter movies:
Rating > 8
Released after 2020
Views > 100 million

Generate statistics using describe().
Export filtered movies to top_movies.csv.
Create:
Line Plot → Views
Bar Chart → Ratings
Pie Chart → Genre Distribution
Scatter Plot → Duration vs Rating
Histogram → Views Distribution

import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("netflix.csv")
print(df[(df["Rating"])>8])
print(df[(df["Release Year"])>2020])
print(df[(df["Views"])>100])
df.to_csv("top_movies.csv" , index=False) 
plt.plot(df["Movie Name"] , df["Views"])
plt.xlabel("Movie name")
plt.ylabel("Views")
plt.grid(True)
plt.show()
plt.bar(df["Movie Name"] , df["Rating"])
plt.xlabel("Movie name")
plt.ylabel("Rating")
plt.title("Rating Distribution")
plt.grid(True)
plt.show()
plt.scatter(df["Duration"] , df["Rating"])
plt.xlabel("duration")
plt.ylabel("Rating")
plt.title("duration vs Rating")
plt.grid(True)
plt.show()
plt.hist(df["Views"] , bins=12 , edgecolor = "black" , color="green")
plt.xlabel("Views")
plt.ylabel("Frequency")
plt.title("Views distribution")
plt.grid(True)
plt.show()"""