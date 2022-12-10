# #use finalcleaned.csv as input and output the decision tree

# import pandas as pd
# import numpy as np

# from sklearn import tree
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# from sklearn.metrics import confusion_matrix
# from sklearn.metrics import classification_report

# from sklearn.tree import DecisionTreeClassifier
# # random forest
# from sklearn.ensemble import RandomForestClassifier


# #read the csv file
# df = pd.read_csv('finaldf.csv')
# df_train_x = df.drop('Gear No._DBSCAN',axis=1)


# df_train_y = df['Gear No._DBSCAN']

# #split the data into train and test
# X_train, X_test, y_train, y_test = train_test_split(df_train_x, df_train_y, test_size=0.2, random_state=42)


# X_train

# #train the model using random forest
# model = RandomForestClassifier(n_estimators=100, max_depth=2, random_state=42)
# model.fit(X_train, y_train)
# X_test = pd.DataFrame(X_test)
# #predict the test data
# y_pred = model.predict(X_test)
# print(y_pred)
# # give  a user input for the input data and predict the output
# speed = float(input("Enter the speed: "))
# rpm = float(input("Enter the rpm: "))
# engine_load = float(input("Enter the engine load: "))

# #predict the output
# y_pred = model.predict([[speed,rpm,engine_load]])
# print(y_pred)

import pickle
# save the model to disk
filename = 'finalized_model.sav'
#use model to predict the output
loaded_model = pickle.load(open(filename, 'rb'))
# take the input from the user
speed = float(input("Enter the speed: "))
rpm = float(input("Enter the rpm: "))
slope = int(input("Enter the slope: "))
#predict the output
y_pred = loaded_model.predict([[speed,rpm, slope]])
print(y_pred)