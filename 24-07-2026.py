"""Exercise 1 – Airport Passenger Analytics
Create a dataset airport_traffic.csv with 120 records.
Columns

Passenger_ID
Airline
Source_City
Destination_City
Ticket_Price
Flight_Duration
Travel_Class
Delay_Minutes
Tasks

Perform complete EDA.
Check missing values and duplicates.
Create the following Seaborn plots:
Scatter Plot → Ticket Price vs Flight Duration (hue=Travel_Class)
Line Plot → Average Ticket Price by Airline
Bar Plot → Average Delay by Airline
Box Plot → Delay Distribution by Travel Class
Histogram → Ticket Price

Answer:
Which airline charges the highest average ticket price?
Which travel class has the longest delays?
Which destination city receives the most passengers?

Write 5 airline management insights.


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("airport_traffic.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())
df["Ticket_Price"] = df["Ticket_Price"].fillna(df["Ticket_Price"].mean())
print(df.isnull().sum())
df["Delay_Minutes"] = df["Delay_Minutes"].fillna(df["Delay_Minutes"].mean())
print(df.isnull().sum())
df["Travel_Class"]  =df["Travel_Class"].fillna(df["Travel_Class"].mode()[0])
print(df.isnull().sum())
print(df.duplicated().sum())

sns.scatterplot(
    data = df,
    x="Ticket_Price",
    y="Flight_Duration",
    hue = "Travel_Class"
)
plt.title("Ticket Price vs Flight duration")
plt.xlabel("Ticket_Price")
plt.ylabel("Flight_Duration")
plt.show()
Average_Ticket = df.groupby("Airline")["Ticket_Price"].mean()
sns.lineplot(
    x=Average_Ticket.index,
    y = Average_Ticket.values,
    marker = "o"
)
plt.title("Average Ticket Price by airline")
plt.xlabel("Average_Ticket")
plt.ylabel("Airline")
plt.show()
Average_Delay = df.groupby("Airline")["Delay_Minutes"].mean()
sns.barplot(
    x= Average_Delay.index,
    y = Average_Delay.values
)
plt.title("Average Delay by airline")
plt.xlabel("Average_Delay")
plt.ylabel("Airline")
plt.show()
sns.histplot(
    data =df,
    x="Ticket_Price",
    bins = 20
)
plt.xlabel("Ticket_Price")
plt.ylabel("Frquency")
plt.title("Ticket Price of FLight")
plt.show()
sns.boxplot(
    data =df,
    x="Travel_Class",
    y="Delay_Minutes"
)
plt.title("Delay Distribution by Travel Class")
plt.xlabel("Travel_Class")
plt.ylabel("Delay_Minutes")
plt.show()
"""





"""Exercise 2 – Electric Vehicle Charging Station Analysis
Create ev_charging.csv with 100 charging sessions.
Columns

Station_ID
City
Vehicle_Type
Charging_Time
Energy_Consumed
Cost
Charging_Type (Fast/Normal)
Tasks

Clean the dataset.
Find missing values.
Create:
Scatter Plot → Charging Time vs Energy Consumed (hue=Charging_Type)
Line Plot → Average Energy Consumed by City
Bar Plot → Total Revenue by City
Box Plot → Cost Distribution by Charging Type
Histogram → Charging Time

Use groupby() to determine:
City generating maximum revenue.
Average charging time by vehicle type.
Most common charging type.

Suggest 5 improvements for the charging network.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("ev_charging.csv")
print(df.head())
print(df.tail())
print(df.describe())
print(df.info())
print(df.isnull().sum())
df["Charging_Time"] = df["Charging_Time"].fillna(df["Charging_Time"].mean())
df["Cost"] = df["Cost"].fillna(df["Cost"].mean())
df["Charging_Type"] = df["Charging_Type"].fillna(df["Charging_Type"].mode()[0])
print(df.isnull().sum())
sns.scatterplot(
    data = df,
    x="Charging_Time",
    y="Energy_Consumed",
    hue = "Charging_Type"
)
plt.xlabel("Charging_Time")
plt.ylabel("Energy_Consumed")
plt.title("Charging Time Vs Energy Consumed")
plt.show()
Average_Energy = df.groupby("City")["Energy_Consumed"].mean()
sns.lineplot(
    x=Average_Energy.index,
    y = Average_Energy.values,
    marker = "o"
)
plt.title("Average Enerhy Consumed by city")
plt.xlabel("Average Energy")
plt.ylabel("City")
plt.show()
total_revenue = df.groupby("City")["Cost"].sum().reset_index()
sns.barplot(
    data = total_revenue,
    x = "City",
    y="Cost"
)
plt.title("Total revenue by city")
plt.xlabel("City")
plt.ylabel("Cost")
plt.show()
sns.boxplot(
    data =df,
    x="Charging_Type",
    y="Cost"
)
plt.title("Cost distribution by charging type")
plt.xlabel("cost")
plt.ylabel("charging type")
plt.show()
sns.histplot(
    data =df,
    x= "Charging_Time",
    bins=20
)
plt.title("Charging time")
plt.xlabel("Charging time")
plt.ylabel("Frequency")
plt.show()

city_revenue = df.groupby("City")["Cost"].sum()
print(city_revenue)
charging_time = df.groupby("Vehicle_Type")["Charging_Time"].mean()
print(charging_time)
charging_type = df["Charging_Type"].mode()[0]
print(charging_type)
"""






"""Exercise 3 – Smart Farming Analytics
Create farm_data.csv with 150 records.
Columns

Farm_ID
Crop
State
Rainfall
Fertilizer_Used
Yield
Temperature
Tasks

Perform EDA.
Handle missing values.
Create:
Scatter Plot → Rainfall vs Yield (hue=Crop)
Line Plot → Average Yield by State
Bar Plot → Average Yield by Crop
Box Plot → Yield Distribution by Crop
Histogram → Rainfall

Analyze:
Which crop gives the highest yield?
Which state has the highest average production?
Does higher rainfall always mean higher yield?

Write 5 recommendations for farmers.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("farm_data.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.isnull().sum())
df["Crop"] = df["Crop"].fillna(df["Crop"].mode()[0])
df["Rainfall"] = df["Rainfall"].fillna(df["Rainfall"].mean())
df["Yield"] =df["Yield"].fillna(df["Yield"].mean())
print(df.isnull().sum())
sns.scatterplot(
    data = df,
    x="Rainfall",
    y="Yield",
    hue="Crop"
)
plt.title("Rainfall vs Yield")
plt.xlabel("Rainfall")
plt.ylabel("Yield")
plt.show()
Average_Yield = df.groupby("State")["Yield"].mean()
sns.lineplot(
    x=Average_Yield.index,
    y=Average_Yield.values,
    marker = "o"
)
plt.title("Average yield by state")
plt.xlabel("Average yield")
plt.ylabel("State")
plt.show()
Average_Crop = df.groupby("Crop")["Yield"].mean()
sns.barplot(
    x=Average_Crop.index,
    y=Average_Crop.values
)
plt.title("Average Yield by crop")
plt.xlabel("Average Yield")
plt.ylabel("Crop")
plt.show()
sns.boxplot(
    data = df,
    x="Crop", 
    y="Yield"
)
plt.title("Yield distribution by crop")
plt.xlabel("Crop")
plt.ylabel("Yield")
plt.show()
sns.histplot(
    data = df,
    x="Rainfall",
    bins=20
)
plt.title("Rainfall")
plt.xlabel("Rainfall")
plt.ylabel("Frequency")
plt.show()
"""






"""Exercise 4 – Online Learning Platform Analytics
Create online_courses.csv with 200 student records.
Columns

Student_ID
Course
Hours_Studied
Quiz_Score
Completion_Percentage
Device (Laptop/Mobile/Tablet)
Country
Tasks

Clean the dataset.
Remove duplicates.
Create:
Scatter Plot → Hours Studied vs Quiz Score (hue=Device)
Line Plot → Average Quiz Score by Course
Bar Plot → Completion Percentage by Course
Box Plot → Quiz Score Distribution by Device
Histogram → Hours Studied

Answer:
Which course has the highest completion rate?
Which device is used the most?
Which country has the highest average quiz score?

Write 5 suggestions to improve student performance.


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("online_courses.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.shape)
print(df.columns)
print(df.describe())
print(df.isnull().sum())
df["Hours_Studied"] = df["Hours_Studied"].fillna(df["Hours_Studied"].mean())
df["Quiz_Score"] = df["Quiz_Score"].fillna(df["Quiz_Score"].mean())
df["Device"] =df["Device"].fillna(df["Device"].mode()[0])
print(df.isnull().sum())
print(df.drop_duplicates())
sns.scatterplot(
    data = df,
    x="Hours_Studied",
    y="Quiz_Score",
    hue = "Device"
)
plt.title("Hours Studied vs Quiz Score")
plt.xlabel("Hours Studied")
plt.ylabel("Quiz Score")
plt.show()
Average_Score = df.groupby("Course")["Quiz_Score"].mean()
sns.lineplot(
    x=Average_Score.index,
    y=Average_Score.values,
    marker = "o"
)
plt.title("Average Quiz score by course")
plt.xlabel("Quiz score")
plt.ylabel("Course")
plt.show()
sns.barplot(
    data =df,
    x="Course",
    y="Completion_Percentage"
)
plt.title("Completion Percentage by course")
plt.xlabel("Course")
plt.ylabel("Completion percentage")
plt.show()
sns.boxplot(
    data=df,
    x="Course",
    y="Quiz_Score"

)
plt.title("Quiz Score distribution by course")
plt.xlabel("Course")
plt.ylabel("Quiz Score")
plt.show()
sns.histplot(
    data =df,
    x="Hours_Studied",
    bins=20
)
plt.title("Hours studied")
plt.xlabel("Hours_Studied")
plt.ylabel("Frequency")
plt.show()
"""





"""Exercise 5 – Space Mission Analytics (Capstone)





Create space_missions.csv with 100 missions.
Columns

Mission_Name
Country
Rocket_Type
Launch_Year
Mission_Cost
Payload_Weight
Success (Yes/No)
Tasks

Perform complete EDA.
Handle missing values and duplicates.
Create:
Scatter Plot → Mission Cost vs Payload Weight (hue=Success)
Line Plot → Missions Launched Per Year
Bar Plot → Average Mission Cost by Country
Box Plot → Payload Distribution by Rocket Type
Histogram → Mission Cost

Analyze:
Which country has the highest average mission cost?
Which rocket type carries the heaviest payload?
What is the mission success rate for each country?

Write 5 recommendations for a space agency based on your findings.

import pandas as pd
import seaborn as sns
import matplotlib.pyplot  as plt
df = pd.read_csv("space_missions.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
print(df.shape)
print(df.columns)
print(df.isnull().sum())
df["Rocket_Type"] =df["Rocket_Type"].fillna(df["Rocket_Type"].mode()[0])
df["Mission_Cost"] =df["Mission_Cost"].fillna(df["Mission_Cost"].mean())
df["Payload_Weight"] = df["Payload_Weight"].fillna(df["Payload_Weight"].mode()[0])
print(df.isnull().sum())
print(df.duplicated())
print(df.drop_duplicates())
sns.scatterplot(
    data=df,
    x="Mission_Cost",
    y="Payload_Weight",
    hue="Success"    
)
plt.title("Mission Cost vs Payload Weight")
plt.xlabel("Mission Cost")
plt.ylabel("Payload Weight")
plt.show()
result = df.groupby("Launch_Year")["Mission_Name"].count()
sns.lineplot(
    x=result.index,
    y=result.values,
    marker="o"
)
plt.title("Mission Launch per year")
plt.xlabel("Launch Year")
plt.ylabel("Mission name")
plt.show()
Average_cost = df.groupby("Country")["Mission_Cost"].mean()
sns.barplot(
    x=Average_cost.index,
    y=Average_cost.values
)
plt.title("Average mission cost by country")
plt.xlabel("Country")
plt.ylabel("Mission cost")
plt.show()
sns.boxplot(
    data = df,
    x="Rocket_Type",
    y="Payload_Weight",
)
plt.title("Payload distribution by rocket type")
plt.xlabel("Rocket_Type")
plt.ylabel("Payload_Weight")
plt.show()
sns.histplot(
    data=df,
    x="Mission_Cost",
    bins=20
)
plt.title("Mission_Cost")
plt.xlabel("Mission_Cost")
plt.ylabel("Frequency")
plt.show()"""