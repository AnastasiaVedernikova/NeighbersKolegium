from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

data = pd.read_csv("WithoutOneCollegium.csv")
y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, stratify=y)

clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))
#0.4 - 0.5
#0.3 - 0.35

