import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression

#deleting rate 1

data = pd.read_csv("ProcessedCollegium.csv")
data = data[data['Oцінка задоволення сусідом'] != 1]
data.to_csv('D:\MachineLearning\\first_neigh_rate\WithoutOneCollegium.csv', encoding='utf-8', index=False)


data = pd.read_csv("WithoutOneCollegium.csv")
y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1,random_state=5)# stratify=y)


neigh_pca = PCA(n_components=10)
neigh_pca.fit(x_train)
train_pca = neigh_pca.transform(x_train)
test_pca = neigh_pca.transform(x_test)


#KNN classifier
model = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
model.fit(train_pca, y_train)
predicition = model.predict(test_pca)
print(model.score(test_pca, y_test))

#LogisticRegression
neigh = LogisticRegression()
neigh.fit(train_pca, y_train)
print(neigh.score(test_pca, y_test))

#RandomForest
clf = RandomForestClassifier(max_depth=2, random_state=0)
clf.fit(train_pca, y_train)
print(clf.score(test_pca, y_test))

#LinearRegression
regr = LinearRegression()
regr.fit(train_pca, y_train)
print(regr.score(test_pca, y_test))


