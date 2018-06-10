
# first schema
# after deleting outliers
# with k-means features
# with cosine distance as features
# after PCA
# all models

import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import math
from sklearn.decomposition import PCA
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsClassifier
import xgboost

k_file = "PairsWithKmeansFeatures.csv"
data = pd.read_csv(k_file)
def cosine_distance(data):
    #cosine distance
    start = 'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)_7:00 - 9:00'
    mid_st = 'k3_2'
    mid = 'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)_Сусід_1_7:00 - 9:00'
    x = data.loc[:, start:mid_st]
    y = data.loc[:, mid::]
    cos_sim = [cosine_similarity(x.loc[[i]].values, y.loc[[i]].values) for i in range(len(x))]
    simple_cos_sim = []
    for a in cos_sim:
        for b in a:
            for c in b:
                simple_cos_sim.append(c)
    degrees = []
    for i in simple_cos_sim:
        angle_in_radians = math.acos(i)
        degrees.append(round(math.degrees(angle_in_radians),2))
    return degrees
data["cosine_distance"] = cosine_distance(data) #data with features : cosine_distance and numbers of cluster(k-means clustering)
# print(data.columns.values)

y =  np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)#update
#PCA
neigh_pca = PCA(n_components=10)
neigh_pca.fit(x_train)
train_pca = neigh_pca.transform(x_train)
test_pca = neigh_pca.transform(x_test)


#KNN classifier
model = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
model.fit(train_pca, y_train)
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

#XGBoost classifier
model = xgboost.XGBRegressor()
model.fit(train_pca, y_train)
print(model.score(test_pca, y_test))





