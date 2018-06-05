from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics import accuracy_score

#reading csv
data = pd.read_csv("ProcessedCollegium.csv")
# data = pd.read_csv("WithoutOneCollegium.csv")

#creating X and Y
y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=5)

#building regression
regr = LinearRegression()
regr.fit(x_train, y_train)
y_pred = regr.predict(x_test)
print(y_pred,y_test)
# print(accuracy_score(y_test, y_pred))
score = regr.score(x_test, y_test)

print(score)#-0.563838862615
