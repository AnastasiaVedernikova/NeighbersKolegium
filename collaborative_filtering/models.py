from  collaborative_filtering.cos_dist import cos_dist
import pandas as pd
import numpy as np
from sklearn.cross_validation import train_test_split
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import xgboost

data = pd.read_csv("WithoutOneCollegium.csv")
data["cos_dist"] = cos_dist()

y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)#update
#PCA
neigh_pca = PCA(n_components=15)
neigh_pca.fit(x_train)
train_pca = neigh_pca.transform(x_train)
test_pca = neigh_pca.transform(x_test)


#KNN classifier
model = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
model.fit(x_train, y_train)
print(model.score(x_test, y_test))

#LogisticRegression
neigh = LogisticRegression()
neigh.fit(x_train, y_train)
print(neigh.score(x_test, y_test))

#RandomForest
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(x_train, y_train)
print(clf.score(x_test, y_test))

#LinearRegression
regr = LinearRegression()
regr.fit(x_train, y_train)
print(regr.score(x_test, y_test))

#XGBoost classifier
model = xgboost.XGBRegressor()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
