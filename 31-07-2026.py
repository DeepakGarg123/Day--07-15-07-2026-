# BanK Cusotmer Churn Prediction

import pandas as pd
df = pd.read_csv("Churn_Modelling.csv")
print(df.head())
print(df.columns)
print(df["Geography"].unique())
print(df["Gender"].unique())
print(df.isnull().sum())
df.drop(["RowNumber" , "CustomerId" , "Surname"] ,axis=1 , inplace = True)
X = df[["CreditScore" , "Geography" , "Gender" , "Age" , "Tenure" , "Balance" , "NumOfProducts" ,"HasCrCard" , "IsActiveMember" , "EstimatedSalary"]]
y = df["Exited"]
X["Geography"]  =X["Geography"].map({"France":0 , "Spain":1 , "Germany":2})
X["Gender"] = X["Gender"].map({"Female":0 , "Male":1})
from sklearn.model_selection import train_test_split
X_train , X_test , y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(max_iter=10000 , class_weight="balanced" )
model.fit(X_train , y_train)
y_pred = model.predict(X_test)
new_customer = [[700 , 2 , 1 , 30 , 7 , 10000 , 4 , 0 , 1 , 20000]]
prediction  = model.predict(new_customer)
print("Customer Exited:" , prediction)
from sklearn.metrics import accuracy_score , precision_score , recall_score , f1_score
print("accuracy score:" , accuracy_score(y_test , y_pred))
print("precision score:" , precision_score(y_test , y_pred))
print("recall score:" , recall_score(y_test , y_pred))
print("f1 score:" , f1_score(y_test ,y_pred))