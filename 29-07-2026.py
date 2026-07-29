# # Linear Regression(Practice)



# import pandas as pd
# df = pd.read_csv("insurance.csv")
# print(df.head())
# X = df[["age" , "sex" , "bmi" , "children" , "smoker" , "region"]]   # features
# y=df["charges"] # target
# X["sex"] = X["sex"].map({"female":1 , "male":0})  # Encoding
# X["smoker"] = X["smoker"].map({"yes":1 , "no":0}) # Encoding
# X["region"] = X["region"].map({"southeast":0 , "southwest":1 ,"northwest":2 , "northeast":3}) # Encoding
# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(
#     X,
#     y,
#     test_size=0.2, # 20% data is tested
#     random_state=42
# )
# from sklearn.linear_model import LinearRegression  # model selection
# model = LinearRegression()
# model.fit(X_train,y_train)  # training data
# y_pred = model.predict(X_test)
# new_patient = [[21 , 0 , 29.7 , 0 , 1 , 3 ]]
# predictin = model.predict(new_patient)
# charges = print("charges:" , predictin)
# from sklearn.metrics import r2_score
# r2 = r2_score(y_test , y_pred)
# print("r2 score:" , r2)

# import pandas as pd
# df = pd.read_csv("diabetes_prediction_dataset.csv")
# print(df.head())
# print(df["gender"].drop_duplicates())
# X = df[["gender" , "age" , "hypertension" , "heart_disease" ,  "smoking_history" , "bmi" , "HbA1c_level" , "blood_glucose_level" ]]
# y = df["diabetes"]
# X["gender"] = X["gender"].map({"Female":1 , "Male":0 })
# X["smoking_history"] =X["smoking_history"].map({"former":0 , "never":1 , "No Info":2 , "current":3 , "not current":4 , "ever":5})
# from sklearn.model_selection import train_test_split
# X_train,X_test,y_train,y_test = train_test_split(
#     X,
#     y,
#     test_size=0.3,
#     random_state=42
# )
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_patient = [[0 , 22 , 1 , 0 , 3 , 29.7 , 7.2 , 100 ]]
# prediction  = model.predict(new_patient)
# diabetes = print("diabetes:" ,prediction)
# from sklearn.metrics import r2_score
# r2 = r2_score(y_test , y_pred)
# print("r2 score:",r2)

# import pandas as pd
# df = pd.read_csv("House Price Prediction Dataset.csv")
# print(df.head())
# print(df["Location"].unique())
# print(df["Condition"].unique())
# print(df["Garage"].unique())
# X  = df[[ "Area" , "Bedrooms" , "Bathrooms" , "Floors" , "YearBuilt" , "Location" , "Condition" , "Garage"]]
# y = df["Price"]
# X["Location"] = X["Location"].map({"Downtown":0 , "Suburban":1 , "Urban":2 , "Rural":3})
# X["Condition"] = X["Condition"].map({"Excellent":0 , "Good":1 , "Fair":2 , "Poor":3})
# X["Garage"] = X["Garage"].map({"No":0 , "Yes":1})
# from sklearn.model_selection import train_test_split
# X_train , X_test , y_train , y_test = train_test_split(
#     X,
#     y,
#     test_size=0.3,
#     random_state=42
# )
# from sklearn.linear_model import LinearRegression
# model = LinearRegression()
# model.fit(X_train , y_train)
# y_pred = model.predict(X_test)
# new_House = [[ 5000 , 6 , 5 , 4 , 2004 , 3 , 0 , 0 ]]
# prediction = model.predict(new_House)
# Price = print("price is:" ,prediction)
# from sklearn.metrics import r2_score
# r2 = r2_score(y_test , y_pred)
# print("r2 score:",r2)

import pandas as pd
df = pd.read_csv("heart_disease_dataset.csv")
print(df.head())
print(df.isnull().sum())
df["Alcohol Intake"] = df["Alcohol Intake"].fillna(df["Alcohol Intake"].mode()[0])
print(df.isnull().sum())
print(df.columns)
print(df["Gender"].unique())
print(df["Smoking"].unique())
print(df["Alcohol Intake"].unique())
print(df["Family History"].unique())
print(df["Diabetes"].unique())
print(df["Obesity"].unique())
print(df["Exercise Induced Angina"].unique())
print(df["Chest Pain Type"].unique())
X = df[["Age" , "Gender" ,"Cholesterol" , "Blood Pressure" ,"Heart Rate" , "Smoking" , "Alcohol Intake" , "Exercise Hours" ,'Family History',
       'Diabetes', 'Obesity', 'Stress Level', 'Blood Sugar', 'Exercise Induced Angina', 'Chest Pain Type']]
y= df["Heart Disease"]
X["Gender"]  = X["Gender"].map({"Female":0 , "Male":1})
X["Smoking"] = X["Smoking"].map({"Current":0 , "Never":1 , "Former":2})
X["Alcohol Intake"] = X["Alcohol Intake"].map({"Heavy":0 , "Moderate":1 , "No":2})
X["Family History"] = X["Family History"].map({"Yes":0 , "No":1})
X["Diabetes"] = X["Diabetes"].map({"Yes":0 , "No":1})
X["Obesity"] = X["Obesity"].map({"Yes":0 , "No":1})
X["Exercise Induced Angina"] = X["Exercise Induced Angina"].map({"Yes":0 , "No":1})
X["Chest Pain Type"] = X["Chest Pain Type"].map({'Atypical Angina':0 ,  'Typical Angina':1 ,'Non-anginal Pain':2 ,'Asymptomatic':3})
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test  = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LinearRegression
model  = LinearRegression()
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_patient = [[21 , 1 , 250 , 140 , 71 , 2 , 0 , 4 , 0 , 0  , 0 , 5 , 190 , 0 , 3 ]]
prediction = model.predict(new_patient)
Disease = print("having Disease:" , prediction)
from sklearn.metrics import r2_score
r2 = r2_score(y_test , y_pred)
print("R2 is:" , r2)