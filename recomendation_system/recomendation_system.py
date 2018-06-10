import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
import dummies.create_dummies

data = pd.read_csv("C:/Users/cs.ucu.edu.ua/Desktop/MLProject/recomendation_system/КолегіумУКУ.csv")
#processing data
columns_to_del = ["Ім'я користувача", "Позначка часу", "Прізвище та ім'я", "Вкажіть будь-ласка посилання на ваш facebook, для того щоб ваші потенційні сусіди могли зв'язатись з вами.",]
for i in range(len(columns_to_del)):
    data = data.drop(columns_to_del[i],1)
#data = pd.get_dummies(data, columns=data.columns.values, drop_first=True)
dummy_data = dummies.create_dummies.create_dummies_single(data)
data = dummy_data
#k-means clustering
if len(data)>14:
    k15 = KMeans(n_clusters=15,  precompute_distances = True, random_state=0)
    k15.fit(data)
    data["k15"] = k15.labels_
if len(data)>6:
    k7 = KMeans(n_clusters=7, precompute_distances = True, random_state=0)
    k7.fit(data)
    data["k7"] = k7.labels_
if len(data)>2:
    k3 = KMeans(n_clusters=3, precompute_distances = True, random_state=0)
    k3.fit(data)
    data["k3"] = k3.labels_
    meaning = [0,1,2]
    list_k3 = data["k3"]
    for j in meaning:
        list_for_one_meaning=[]
        for i in list_k3:
            if i==j:
                list_for_one_meaning.append(1)
            else:
                list_for_one_meaning.append(0)
        col_name = "k3_"+str(j)
        data[col_name] = list_for_one_meaning
    data = data.drop("k3",1)

#fitting model with history data
history_data = pd.read_csv("PairsWithKmeansFeatures.csv")
y = np.array(history_data['Oцінка задоволення сусідом'])
history_data = history_data.drop('Oцінка задоволення сусідом',1)
x = history_data.values
knn = KNeighborsClassifier(n_neighbors=5, algorithm='auto')
knn.fit(x, y)

def construct_user_dataframe(id_user, data):
    new_columns = []
    all_st = data.columns.values
    for i in all_st:
        new_columns.append(i+"_ME")
    for i in range(len(new_columns)):
        data[new_columns[i]] = [data.get_value(id_user, all_st[i]) for i in range(len(data))]
    return data
result = construct_user_dataframe(1, data)

scores = knn.predict(result)
scores_with_ids = []
for i in range(len(scores)):
    scores_with_ids.append([i, scores[i]])
sorted_scores = sorted(scores_with_ids, key=lambda x: int(x[1]),reverse=True)
ids = [sorted_scores[i][0] for i in range(2)]#ids of students (facebook links)

collegium = pd.read_csv("C:/Users/cs.ucu.edu.ua/Desktop/MLProject/recomendation_system/КолегіумУКУ.csv")
for i in range(2):
     print(collegium.at[ids[i], "Вкажіть будь-ласка посилання на ваш facebook, для того щоб ваші потенційні сусіди могли зв'язатись з вами."])

