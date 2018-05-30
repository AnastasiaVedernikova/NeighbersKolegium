import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

#reading csv
data = pd.read_csv("WithoutOneCollegium.csv")

#creating X and Y
y =  np.array(data['Oцінка задоволення сусідом'])
#print(y)
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=5)#, stratify=y

neigh = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
neigh.fit(x_train, y_train)
y_pred = neigh.predict(x_test)
# print(accuracy_score(y_test, y_pred))
#print(y_pred, y_test)
print(neigh.score(x_test, y_test))





