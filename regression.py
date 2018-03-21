from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
import sklearn
import matplotlib.pyplot as plt
from sklearn.cross_validation import train_test_split

#reading csv
data = pd.read_csv("ProcessedKolegium.csv")

#creating X and Y
y =  np.array(data['Середня оцінка задоволення сусідом']) # shape - 67,
data = data.drop('Середня оцінка задоволення сусідом',1)
x = data.values #shape - 67,197

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=5)

# print(x_train.shape)
# print(x_test.shape)
# print(y_train.shape)
# print(y_test.shape)

#building regression
regr = LinearRegression()
regr.fit(x_train, y_train)

#coeficients
#print(regr.coef_)

#The mean square error
predicts = regr.predict(x_test)
mean = np.mean((predicts - y_test)**2)
#print(mean)

score = regr.score(x_test, y_test)
print(score)

#ploting data
plt.scatter(regr.predict(x_train), regr.predict(x_train)- y_train, c='b', s=40, alpha=0.5)
plt.scatter(regr.predict(x_test), regr.predict(x_test)- y_test, c='g', s=40)
plt.hlines(y=0, xmin=0, xmax=5)
plt.show()
