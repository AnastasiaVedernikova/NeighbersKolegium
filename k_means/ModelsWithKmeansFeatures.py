from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

from sklearn.decomposition import PCA

#reading csv
data = pd.read_csv("PairsWithKmeansFeatures.csv")

#creating X and Y
y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1, random_state=5)

neigh_pca = PCA(n_components=15)
neigh_pca.fit(x_train)
pca_train = neigh_pca.transform(x_train)
pca_test = neigh_pca.transform(x_test)


regr = LinearRegression().fit(pca_train, y_train)
print(regr.score(pca_test, y_test))

logistic = LogisticRegression()
logistic.fit(pca_train, y_train)
print(logistic.score(pca_test, y_test))

knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
knn.fit(x_train, y_train)
print(knn.score(pca_test, y_test))

rfc = RandomForestClassifier(max_depth=2, random_state=0)
rfc.fit(pca_train, y_train)
print(rfc.score(pca_test, y_test))


