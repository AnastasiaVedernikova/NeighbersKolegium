
import xgboost
from sklearn.decomposition import PCA
import numpy as np
import pandas as pd
from sklearn.cross_validation import train_test_split
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import StratifiedKFold


data = pd.read_csv("WithoutOneCollegium.csv")
y = np.array(data['Oцінка задоволення сусідом'])
data = data.drop('Oцінка задоволення сусідом',1)
x = data.values
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3)

# model = xgboost.XGBClassifier()
# n_estimators = [5, 8, 9, 11, 12, 15, 10]
# max_depth = [1, 2, 4, 6]
# learning_rate = [ 0.1101, 0.1, 0.5, 1, 2]
# param_grid = dict(max_depth=max_depth, n_estimators=n_estimators, learning_rate=learning_rate)
# kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=7)
# grid_search = GridSearchCV(model, param_grid, scoring="neg_log_loss", n_jobs=-1, cv=3, verbose=1)
# result = grid_search.fit(x_train, y_train)
# print("Best parameters set found on development set:")
# print(grid_search.best_params_)
#'n_estimators': 11, 'max_depth': 1, 'learning_rate': 0.1101} - 0.1
#{'n_estimators': 5, 'max_depth': 4, 'learning_rate': 0.1} - 0.3


model = xgboost.XGBClassifier(learning_rate =0.01,n_estimators=100,max_depth=2)
model.fit(x_train, y_train)
print(model.score(x_test, y_test))#0.2857142857142857
