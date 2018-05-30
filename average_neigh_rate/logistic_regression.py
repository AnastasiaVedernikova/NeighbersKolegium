from sklearn.linear_model import LogisticRegression
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn import metrics

#reading csv
data = pd.read_csv("ProcessedCollegium.csv")

#creating X and Y
y =  np.array(data['Середня оцінка задоволення сусідом']) # shape - 67,
data = data.drop('Середня оцінка задоволення сусідом',1)
x = data.values #shape - 67,197

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=5)
classes =[]
for i in y_train:
    if i not in classes:
        classes.append(i)
print(classes)
#6 classes - [4.0, 4.5, 3.5, 3.0, 5.0, 2.5]
#class 1 - 2.5, class 2 - 3, class 3 - 3.5, class 4 - 4, class 5 - 4.5, class 6 - 5

def classification_of_labels(y):
    y_classes=[]
    for i in y:
        if i == 2.5:
            y_classes.append(1)
        elif i == 3.0:
            y_classes.append(1)
        elif i == 3.5:
            y_classes.append(2)
        elif i == 4.0:
            y_classes.append(2)
        elif i == 4.5:
            y_classes.append(3)
        else:
            y_classes.append(3)
    return y_classes
y_train_classes=classification_of_labels(y_train)
y_test_classes=classification_of_labels(y_test)

#print(y_train_classes, y_test_classes)

neigh = LogisticRegression()
neigh.fit(x_train, y_train_classes)
y_pred = neigh.predict(x_test)

print(neigh.score(x_test, y_test_classes))
#0.571428571429





