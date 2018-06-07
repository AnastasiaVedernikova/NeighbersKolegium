
import xgboost
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split

data = pd.read_csv("WithoutOneCollegium.csv")
y = np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values

#deviding for train and test data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.1)

model = xgboost.XGBClassifier()
model.fit(x_train, y_train)
print(model.score(x_test, y_test))
#0.45 - 0.3
#0.28 - 0.1
#without startify - 0.1- 0.571
#0.3 - 0.45
#before deleting outlier 0.3 - 0.095

neigh_pca = PCA(n_components=10)
neigh_pca.fit(x_train)
train_pca = neigh_pca.transform(x_train)
test_pca = neigh_pca.transform(x_test)
afterPCA = xgboost.XGBClassifier()
afterPCA.fit(train_pca, y_train)
print(afterPCA.score(test_pca, y_test))
## 0.4 - 0.3
#0.428 - 0.1
#without startify - 0.1- 0.28
#0.3 - 0.35
#before deleting outlier 0.3 - 0.38






