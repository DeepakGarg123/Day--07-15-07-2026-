"""Exercise 1 – Cricket Scores Analysis
Create a NumPy array containing the runs scored by a batsman in 10 matches.
Tasks:

Display the array.
Find the highest score.
Find the lowest score.
Find the average score.
Find the total runs scored.

import numpy as np
arr = np.array(
[45,78,86,15,92,58,78,56,89,21])
print(arr)
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.sum(arr))
"""

"""Exercise 2 – Cinema Seat Numbers
Using NumPy, create seat numbers from 1 to 100.
Tasks:

Display seat numbers.
Reshape into 10 × 10.
Display the first row.
Display the last row.

import numpy as np
arr = np.arange(1,101)
print(arr)
arr1= arr.reshape(10,10)
print(arr1)
print(arr1[0])
print(arr1[-1])"""


"""Exercise 3 – Planet Distance Series
Create a Pandas Series containing distances (in million km) of planets from the Sun.
Use custom indexes:
Mercury
Venus
Earth
Mars
JupiterTasks:

Print the complete Series.
Print Earth's distance.
Print the first three planets.

import pandas as pd
distance = pd.Series([55,100,150,187,140],  
index = ["Mercury" , "Venus" , "Earth" , "Mars" , "Jupiter"])
print(distance)
print(distance["Earth"])
print(distance[:3])
"""



"""

Exercise 4 – Daily Water Intake
Create a text file named:
water_log.txtStore the daily water intake (in liters) for 7 days.
Read the file and display each day's intake.

with open("water_log.txt" , "r") as file:
    for line in file:
        print(line)
"""


"""Exercise 5 – Random Number Grid
Using NumPy:
Generate numbers from 1 to 36.
Convert them into a 6 × 6 matrix.
Display:

Shape
Size
Dimensions 

import numpy as np
arr = np.arange(1,37)
print(arr)
arr1 = arr.reshape(6,6)
print(arr1)
print(arr.shape)
print(arr.size)
print(arr.ndim)
"""


"""Exercise 6 – Mobile Store Price Analysis
Create an array containing prices of 12 smartphones.
Find:

Most expensive phone
Cheapest phone
Average price
Standard deviation
Phones costing more than ₹30,000

import numpy as np
arr = np.array([15000 , 31000 , 45000 , 58000 , 60000 , 
46000 , 47000 , 48000 , 49000 , 50000 , 51000 , 59000 ])
print(np.max(arr))
print(np.min(arr))
print(np.mean(arr))
print(np.std(arr))
print(arr[arr>30000])"""

"""Exercise 7 – Library Book IDs
Generate book IDs from 1001 to 1100.
Tasks:

Reshape into 10 × 10
Display every alternate row.
Display every alternate column.
Flatten the matrix.


import numpy as np
arr = np.arange(1001,1101)
print(arr)
arr1 = arr.reshape(10,10)
print(arr1)
print(arr1[::2])
print(arr1[: , ::2])

print(arr1.flatten())"""

"""
Exercise 8 – Hospital Bed Status
Create a Boolean NumPy array representing occupied (True) and vacant (False) beds.
Tasks:

Count occupied beds.
Count vacant beds.
Display only vacant beds using Boolean indexing.

import numpy as np
beds = np.array([True , False , True , True , False])
print(np.sum(beds))
print(np.sum(beds==False))
print(beds[beds==False])
"""


"""Exercise 9 – Online Course Ratings
Create a Series containing ratings of 10 online courses.
Tasks:

Highest rating
Lowest rating
Average rating
Courses with rating greater than 4

import pandas as pd
s = pd.Series([1,2,3,4,5,6,7,8,9,10])
print(s.max())
print(s.min())
print(s.mean())
print(s[s>4])
"""


"""Exercise 10 – Electricity Consumption
Create a CSV file:
electricity.csv
Columns:

House No
Units Consumed
Read the CSV.
Calculate:

Total units
Average units
Maximum units
Minimum units

import pandas as pd
df = pd.read_csv("electricity.csv")
print(df["Units Consumed"].sum())
print(df["Units Consumed"].mean())
print(df["Units Consumed"].max())
print(df["Units Consumed"].min())
"""

"""Exercise 11 – Airport Passenger Analysis
Create an array representing passengers traveling each day for one week.
Tasks:

Total passengers
Busiest day
Least busy day
Average passengers
Days with passengers above average

import numpy as np
arr = np.array([120, 150, 180, 140, 210, 195, 160])
print(arr)
print(arr.sum())
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr[arr > arr.mean()])"""

"""Exercise 12 – Fitness Tracker
Store daily step counts for one month (30 days).
Using NumPy:
Display:

Maximum steps
Minimum steps
Mean
Median
Standard deviation
Days with more than 10,000 steps
import numpy as np
arr =np.array([8200, 9500, 11000, 7600, 12500,
9800, 10200, 8700, 13400, 9100,
15000, 7800, 11800, 9600, 10500,
8900, 12100, 14300, 9900, 10800,
11200, 8500, 13700, 9400, 10100,
11900, 8800, 15500, 9700, 12300])
print(arr.max())
print(arr.min())
print(arr.mean())
print(np.median(arr))
print(arr.std())
print(arr[arr>10000])"""

"""Exercise 13 – Hotel Room Prices
Create a 5 × 6 matrix representing room prices.
Tasks:

Total revenue if all rooms are booked.
Most expensive room.
Cheapest room.
Revenue per floor (axis=1).
Revenue per room type (axis=0).

import numpy as np
arr = np.array([
    [2500, 2800, 3000, 3500, 4000, 4500],
    [2600, 2900, 3100, 3600, 4100, 4600],
    [2700, 3000, 3200, 3700, 4200, 4700],
    [2800, 3100, 3300, 3800, 4300, 4800],
    [2900, 3200, 3400, 3900, 4400, 4900]
])
print(arr.sum())
print(arr.max())
print(arr.min())
print(arr.sum(axis = 1))
print(arr.sum(axis=0))"""



"""Exercise 14 – Weather Monitoring
Create daily temperatures for 15 days.
Using Boolean indexing:
Display:

Days above 35°C
Days below 20°C
Temperatures between 25°C and 30°C

import numpy as np
arr =np.array([18, 22, 27, 30, 36,
39, 25, 19, 28, 33,
37, 24, 29, 41, 20])
print(arr[arr>35])
print(arr[arr<20])
print(arr[(arr>=25)&(arr<=30)])"""

"""Exercise 15 – Olympic Medal Table
Create a CSV:
Columns:

Country
Gold
Silver
Bronze
Read the file.
Calculate:

Total medals for each country.
Country with maximum gold medals.
Country with highest total medals.

import pandas as pd
df = pd.read_csv("medals.csv")
df["Total"] = df["Gold"] + df["Silver"] + df["Bronze"]
print(df["Total"])
print(df["Gold"].max())"""

"""Exercise 16 – IPL Team Performance Dashboard
Create arrays for one IPL team's performance in 14 matches.
Store:

Runs Scored
Runs Conceded
Calculate:

Highest score
Lowest score
Average score
Net Run Difference (Runs Scored − Runs Conceded)
Matches where team scored above average


import numpy as np
arr  = np.array([ 180, 165, 210, 145, 190, 175, 160,
200, 155, 185, 170, 195, 205, 178])
arr_1 = np.array([ 170, 180, 195, 150, 185, 165, 170,
190, 160, 175, 180, 200, 198, 172])
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr-arr_1)
print(arr[arr>np.mean(arr)])"""


"""Exercise 17 – Air Quality Monitoring System
Create AQI values for 30 days.
Categorize using Boolean indexing:

Good (<50)
Moderate (50–100)
Poor (>100)
Display the number of days in each category.

import numpy as np
arr =np.array([ 35, 48, 52, 67, 89, 110, 125, 45, 38, 72,
    95, 101, 56, 43, 28, 130, 78, 84, 49, 62,
    140, 33, 58, 97, 115, 41, 88, 105, 46, 55])
print(arr[arr<50])
print(arr[(arr>=50) & (arr<=100)])
print(arr[arr>100])
print(len(arr[arr<50]))
print(len(arr[arr>100]))
print(len(arr[(arr>=50) & (arr<=100)]))
"""

"""Exercise 18 – University Exam Analytics
Create marks for 50 students in one subject.
Calculate:

Class average
Median
Standard deviation
Students above average
Students below average
Top 10 students
Bottom 10 students

import numpy as np
arr = np.array([78, 65, 89, 92, 55, 71, 84, 69, 95, 88,
    76, 81, 67, 73, 90, 58, 62, 85, 79, 94,
    68, 74, 87, 91, 60, 72, 83, 77, 96, 64,
    70, 82, 59, 75, 86, 93, 66, 80, 97, 61,
    63, 98, 57, 69, 88, 79, 84, 90, 71, 95])
print(np.mean(arr))
print(np.median(arr))
print(np.std(arr))
print(arr[arr>np.mean(arr)])
print(arr[arr<np.mean(arr)])
bottom_10 = np.sort(arr)[:10]
print(bottom_10)
top_10 = np.sort(arr)[-10:]
print(top_10)"""


"""Exercise 19 – Fuel Station Sales Report
Create a CSV containing:

Date
Petrol Sold
Diesel Sold
Read the CSV.
Using NumPy:
Calculate:

Total petrol sold
Total diesel sold
Highest sales day
Lowest sales day
Average daily sales


import pandas as pd
df  = pd.read_csv("fuels.csv")
print(df)
print(df["Petrol Sold"].sum())
print(df["Diesel Sold"].sum())
total_sales = df["Petrol Sold"] + df["Diesel Sold"]
print(total_sales)
print(total_sales.mean())"""



"""Exercise 20 – Space Mission Telemetry Analyzer
A satellite records temperature every hour for 24 hours.
Create a NumPy array representing these temperatures.
Tasks:

Find maximum and minimum temperature.
Find average temperature.
Display temperatures above average.
Display temperatures below average.
Reshape the data into 6 × 4.
Calculate average temperature for each row (axis=1).
Calculate average temperature for each column (axis=0).
Flatten the array.
Round all temperatures to one decimal place.
Display unique temperature values.

import numpy as np
arr  = np.array([0 , -1 , -2 , 8 , 4 , 5 ,
                 31 , 32 , 33 ,34 ,35 , 
                 41 , 42 , 43 ,44 ,45 ,
                 21 , 22 , 23 ,24 ,25 ,
                 11 , 12 , 13 ,14 ,15 ,])
print(arr.max())
print(arr.min())
print(arr.mean())
print(arr.reshape(2,13))
print(arr[arr>arr.mean()])
print(arr[arr<arr.mean()])
print(arr.mean(axis=1))
print(arr.mean(axis=0))
"""
