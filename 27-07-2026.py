"""Exercise 1 – Housing Price Statistics
A real estate company collected details of 150 houses.
Columns

House_ID
City
Area (sq ft)
Bedrooms
Price
Age_of_House
Tasks

Identify the type of each column (Continuous, Discrete, Nominal, Ordinal).
Calculate:
Mean price
Median price
Mode of bedrooms

Calculate:
Range
Variance
Standard Deviation of house prices.

Calculate:
Q1
Q2
Q3
IQR

Detect price outliers using the IQR method.
Explain whether the mean or median is a better measure of central tendency for house prices.
import numpy as np
import pandas as pd
df = pd.read_csv("housing_price_statistics.csv")
# print(df.dtypes)
# print(df["Price"].mean())
# print(df["Price"].median())
# print(df["Bedrooms"].mode())
# Range = df["Price"].max()-df["Price"].min()
# print(Range)
print(df["Price"].var())
print(df["Price"].std())
print(df["Price"].quantile(0.25))
print(df["Price"].quantile(0.50))
print(df["Price"].quantile(0.75))
Q1 = df["Price"].quantile(0.25)
Q3 = df["Price"].quantile(0.75)
IQR  =Q3-Q1
print(IQR)
"""




"""Exercise 2 – Mobile App Usage Analysis
A mobile company tracks 200 users.
Columns

User_ID
Daily_Screen_Time (hours)
Number_of_Apps
Age
Subscription_Type
City
Tasks

Classify every column into the correct data type.
Calculate:
Mean screen time
Median screen time
Mode of subscription type

Calculate:
Variance
Standard deviation

Find:
10th percentile
25th percentile
75th percentile
95th percentile

Detect users with unusually high screen time.
import numpy as np
import pandas as pd
df = pd.read_csv("mobile_app_usage.csv")
print(df.isnull().sum())
df["Daily_Screen_Time"]  =df["Daily_Screen_Time"].fillna(df["Daily_Screen_Time"].mean())
df["Subscription_Type"]  =df["Subscription_Type"].fillna(df["Subscription_Type"].mode()[0])
print(df.isnull().sum())
print(df["Daily_Screen_Time"].mean())
print(df["Daily_Screen_Time"].median())
print(df["Subscription_Type"].mode())
print(df["Daily_Screen_Time"].var())
print(df["Daily_Screen_Time"].std())
print(np.percentile(df["Daily_Screen_Time"],10))
print(np.percentile(df["Daily_Screen_Time"],25))
print(np.percentile(df["Daily_Screen_Time"],75))
print(np.percentile(df["Daily_Screen_Time"],95))
"""




"""Exercise 3 – Olympic Athlete Performance
Create a dataset of 120 athletes.
Columns

Athlete
Country
Sport
Age
Height
Weight
Gold_Medals
Tasks

Identify data types.
Calculate:
Mean age
Median height
Mode of sport

Find:
Range of weights
Variance of heights
Standard deviation of ages

Calculate Q1, Q2, Q3 and IQR for medals.
Detect athletes with unusually high medal counts.
import numpy as np
import pandas as pd
df = pd.read_csv("olympic_athletes.csv")
print(df.dtypes)
print(df["Age"].mean())
print(df["Height"].median())
print(df["Sport"].mode())
Range = df["Weight"].max()-df["Weight"].min()
print(Range)
print(df["Height"].var())
print(df["Age"].std())
Q1 = df["Gold_Medals"].quantile(0.25)
print(Q1)
Q2 = df["Gold_Medals"].quantile(0.50)
print(Q2)
Q3 = df["Gold_Medals"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
# outliers
"""




"""Exercise 4 – Music Streaming Statistics
Create a dataset with 250 songs.
Columns

Song
Artist
Genre
Duration
Streams
Release_Year
Tasks

Find:
Mean streams
Median duration
Mode genre

Calculate:
Range
Variance
Standard deviation of streams.

Calculate:
5th percentile
25th percentile
50th percentile
90th percentile

Find songs considered outliers based on stream count.

import numpy as np
import pandas as pd
df = pd.read_csv("music_streaming.csv")
print(df.isnull().sum())
df["Genre"] = df["Genre"].fillna(df["Genre"].mode()[0])
df["Duration"] = df["Duration"].fillna(df["Duration"].mean())
df["Release_Year"] = df["Release_Year"].fillna(df["Release_Year"].mean())
df["Streams"] = df["Streams"].fillna(df["Streams"].mean())
print(df.isnull().sum())
print(df["Streams"].mean())
print(df["Duration"].median())
print(df["Genre"].mode())
Range = df["Streams"].max()-df["Streams"].min()
print(Range)
print(df["Streams"].var())
print(df["Streams"].std())
print(np.percentile(df["Streams"],5))
print(np.percentile(df["Streams"],25))
print(np.percentile(df["Streams"],50))
print(np.percentile(df["Streams"],90))

#outliers
"""





"""Exercise 5 – Water Consumption Study
A city records water usage from 180 households.
Columns

House_ID
Family_Size
Daily_Water_Usage
Area
Income_Group
Tasks

Identify the data type of every column.
Calculate central tendency for water usage.
Calculate measures of dispersion.
Find quartiles and IQR.
Detect households wasting unusually high amounts of water.

import numpy as np
import pandas as pd
df= pd.read_csv("water_consumption.csv")
print(df["Daily_Water_Usage"].mean())
print(df["Daily_Water_Usage"].mode())
print(df["Daily_Water_Usage"].median())
Range = df["Daily_Water_Usage"].max()-df["Daily_Water_Usage"].min()
print(Range)
print(df["Daily_Water_Usage"].var())
print(df["Daily_Water_Usage"].std())
Q1 = df["Daily_Water_Usage"].quantile(0.25)
print(Q1)
Q2 = df["Daily_Water_Usage"].quantile(0.50)
print(Q2)
Q3 = df["Daily_Water_Usage"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
"""




"""Exercise 6 – University Placement Statistics
Dataset contains 150 students.
Columns

Student
Branch
CGPA
Interview_Score
Package
Company
Tasks

Identify continuous and discrete variables.
Find:
Mean package
Median package
Mode company

Calculate:
Variance
Standard deviation

Find 80th percentile of salary package.
Detect unusually high salary packages.

import numpy as np
import pandas as pd
df= pd.read_csv("university_placement.csv")
print(df.isnull().sum())
df["CGPA"] = df["CGPA"].fillna(df["CGPA"].mean())
df["Package"] = df["Package"].fillna(df["Package"].mean())
df["Company"] = df["Company"].fillna(df["Company"].mode()[0])
print(df.isnull().sum())
print(df["Package"].mean())
print(df["Package"].median())
print(df["Company"].mode())
print(df["Package"].var())
print(df["Package"].std())
print(np.percentile(df["Package"],80))
"""




"""Exercise 7 – Movie Ticket Booking Analysis
Dataset contains 300 bookings.
Columns

Booking_ID
Movie
Seat_Type
Ticket_Price
Number_of_Tickets
Booking_Day
Tasks

Categorize every variable.
Calculate:
Mean ticket price
Median ticket price
Mode seat type

Calculate:
Variance
Standard deviation

Find:
Q1
Q3
IQR

Detect premium-priced outliers.
import numpy as np
import pandas as pd
df = pd.read_csv("movie_ticket_booking.csv")
print(df["Ticket_Price"].mean())
print(df["Ticket_Price"].median())
print(df["Seat_Type"].mode())
print(df["Ticket_Price"].var())
print(df["Ticket_Price"].std())
Q1  = df["Ticket_Price"].quantile(0.25)
print(Q1)
Q2 = df["Ticket_Price"].quantile(0.50)
print(Q2)
Q3 = df["Ticket_Price"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
"""



"""Exercise 8 – Food Delivery Time Analysis
Dataset contains 250 deliveries.
Columns

Delivery_ID
Restaurant
Distance
Delivery_Time
Delivery_Partner
Rating
Tasks

Classify variables.
Calculate:
Mean delivery time
Median distance
Mode restaurant

Calculate dispersion.
Detect unusually slow deliveries using IQR.
Explain why median may be better than mean.
import numpy as np
import pandas as pd
df = pd.read_csv("food_delivery_analysis.csv")
print(df["Delivery_Time"].mean())
print(df["Distance"].mean())
print(df["Restaurant"].mode())
print(df["Delivery_Time"].var())
print(df["Delivery_Time"].std())
Range = df["Delivery_Time"].max()-df["Delivery_Time"].min()
print(Range)
"""



"""Exercise 9 – Hotel Booking Statistics
Dataset contains 180 hotel bookings.
Columns

Booking_ID
Hotel_Type
Stay_Days
Room_Price
Guests
City
Tasks

Calculate all measures of central tendency.
Calculate all measures of dispersion.
Find:
20th percentile
50th percentile
95th percentile

Detect expensive room outliers.
Recommend whether mean or median should be used for pricing analysis.
import numpy as np
import pandas as pd
df = pd.read_csv("hotel_booking_statistics.csv")
print(df.isnull().sum())
df["Hotel_Type"] = df["Hotel_Type"].fillna(df["Hotel_Type"].mode()[0])
df["Room_Price"] = df["Room_Price"].fillna(df["Room_Price"].mean())
print(df.isnull().sum())
print(df["Room_Price"].mean())
print(df["Hotel_Type"].mode())
print(df["Room_Price"].median())
Range = df["Room_Price"].max()-df["Room_Price"].min()
print(Range)
print(df["Room_Price"].var())
print(df["Room_Price"].std())
print(np.percentile(df["Room_Price"],20))
print(np.percentile(df["Room_Price"],50))
print(np.percentile(df["Room_Price"],95))
"""



"""Exercise 10 – Electricity Consumption Analysis
Dataset contains 365 daily records.
Columns

Day
Units_Consumed
Temperature
City
Tasks

Calculate:
Mean units consumed
Median units consumed
Mode city

Calculate:
Range
Variance
Standard deviation

Detect abnormal electricity usage using IQR.
Explain seasonal variations based on statistics.
import numpy as np
import pandas as pd
df = pd.read_csv("electricity_consumption.csv")
print(df["Units_Consumed"].mean())
print(df["Units_Consumed"].median())
print(df["City"].mode())
Range = df["Units_Consumed"].max()-df["Units_Consumed"].min()
print(Range)
print(df["Units_Consumed"].var())
print(df["Units_Consumed"].std())
"""



"""Exercise 11 – Airline Delay Statistics
Dataset contains 250 flights.
Columns

Flight
Airline
Delay_Minutes
Destination
Ticket_Class
Tasks

Calculate all central tendency measures.
Calculate dispersion measures.
Find quartiles.
Find 95th percentile of delays.
Detect extremely delayed flights.
import numpy as np
import pandas as pd
df = pd.read_csv("airline_delay_statistics.csv")
print(df.isnull().sum())
df["Delay_Minutes"] = df["Delay_Minutes"].fillna(df["Delay_Minutes"].mean())
df["Ticket_Class"] = df["Ticket_Class"].fillna(df["Ticket_Class"].mode()[0])
print(df.isnull().sum())
print(df["Delay_Minutes"].mean())
print(df["Airline"].mode())
print(df["Delay_Minutes"].median())
Range = df["Delay_Minutes"].max()-df["Delay_Minutes"].min()
print(Range)
print(df["Delay_Minutes"].var())
print(df["Delay_Minutes"].std())
Q1  = df["Delay_Minutes"].quantile(0.25)
print(Q1)
Q2 = df["Delay_Minutes"].quantile(0.50)
print(Q2)
Q3 = df["Delay_Minutes"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
print(np.percentile(df["Delay_Minutes"] , 95))
"""



"""Exercise 12 – Cryptocurrency Market Analysis
Dataset contains 150 cryptocurrencies.
Columns

Coin
Market_Cap
Daily_Return
Trading_Volume
Category
Tasks

Classify variables.
Calculate:
Mean return
Median market cap
Mode category

Calculate variance and standard deviation.
Detect outlier cryptocurrencies based on daily returns.
Explain whether returns are highly volatile.

import numpy as np
import pandas as pd
df = pd.read_csv("cryptocurrency_market_analysis.csv")
print(df["Daily_Return"].mean())
print(df["Market_Cap"].median())
print(df["Category"].mode())
print(df["Market_Cap"].var())
print(df["Market_Cap"].std())
"""


"""Exercise 13 – Forest Wildlife Survey
Dataset contains 200 animals.
Columns

Animal
Species
Weight
Age
Forest
Tasks

Identify data types.
Calculate central tendency.
Calculate dispersion.
Calculate quartiles.
Identify unusually heavy animals.


import numpy as np
import pandas as pd
df = pd.read_csv("forest_wildlife_survey.csv")
print(df.dtypes)
print(df["Weight"].mean())
print(df["Weight"].median())
print(df["Animal"].mode())
Range = df["Weight"].max()-df["Weight"].min()
print(Range)
print(df["Weight"].var())
print(df["Weight"].std())
Q1 = df["Weight"].quantile(0.25)
print(Q1)
Q2 = df["Weight"].quantile(0.50)
print(Q2)
Q3 = df["Weight"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
"""



"""Exercise 14 – Social Media Influencer Analytics
Dataset contains 180 influencers.
Columns

Influencer
Platform
Followers
Engagement_Rate
Category
Tasks

Calculate:
Mean followers
Median engagement
Mode platform

Calculate:
Variance
Standard deviation

Find:
Top 10% influencer threshold using the 90th percentile.

Detect follower outliers.
Explain whether follower count is normally distributed.

import numpy as np
import pandas as pd
df = pd.read_csv("social_media_influencer_analytics.csv")
print(df.isnull().sum())
df["Platform"] = df["Platform"].fillna(df["Platform"].mode())
df["Followers"] = df["Followers"].fillna(df["Followers"].mean())
print(df["Followers"].mean())
print(df["Engagement_Rate"].median())
print(df["Platform"].mode())
print(df["Followers"].var())
print(df["Followers"].std())
Range  =df["Followers"].max()-df["Followers"].min()
print(Range)
print(np.percentile(df["Followers"], 90))
"""




"""Exercise 15 – Mars Rover Sensor Analysis (Capstone)
NASA provides 500 sensor readings.
Columns

Reading_ID
Temperature
Pressure
Battery_Level
Terrain_Type
Signal_Strength
Tasks

Classify every column.
Calculate all measures of central tendency.
Calculate all measures of dispersion.
Find:
Q1
Q2
Q3
IQR
10th percentile
90th percentile

Detect outliers using:
Box Plot
IQR Method

Prepare a technical report answering:
Which variable is the most stable?
Which variable is the most volatile?
Which variable contains abnormal readings?
Should NASA investigate any sensor based on your statistical analysis?

import numpy as np
import pandas as pd
df = pd.read_csv("mars_rover_sensor_analysis.csv")
print(df.isnull().sum())
df["Temperature"] = df["Temperature"].fillna(df["Temperature"].mean())
df["Pressure"] = df["Pressure"].fillna(df["Pressure"].mean())
df["Battery_Level"]  = df["Battery_Level"].fillna(df["Battery_Level"].median())
df["Terrain_Type"] = df["Terrain_Type"].fillna(df["Terrain_Type"].mode()[0])

print(df.dtypes)
print(df["Pressure"].mean())
print(df["Pressure"].median())
print(df["Terrain_Type"].mode())
Range = df["Pressure"].max()-df["Pressure"].min()
print(Range)
print(df["Pressure"].var())
print(df["Pressure"].std())
Q1  =df["Pressure"].quantile(0.25)
print(Q1)
Q2  =df["Pressure"].quantile(0.50)
print(Q2)
Q3  =df["Pressure"].quantile(0.75)
print(Q3)
IQR = Q3-Q1
print(IQR)
print(np.percentile(df["Pressure"], 10))
print(np.percentile(df["Pressure"], 90))
"""