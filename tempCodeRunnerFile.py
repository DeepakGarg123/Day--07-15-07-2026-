X = df[["gender" , "age" , "hypertension" , "heart_disease" ,  "smoking_history" , "bmi" , "HbA1c_level" , "blood_glucose_level" ]]
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
