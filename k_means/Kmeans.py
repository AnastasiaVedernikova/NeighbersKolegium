import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv("Collegium.csv")
columns_to_del = ["Позначка часу", "Електронна адреса", "Прізвище та ім'я", "Вкажіть будь-ласка посилання на ваш facebook, для того щоб ваші потенційні сусіди могли зв'язатись з вами.",
           "Назвіть імена та прізвища ваших сусідів по кімнаті","Вкажіть номер кімнати в гуртожитку","Оцініть ваш рівень задоволення життя разом з ними "]
for i in range(len(columns_to_del)):
     data = data.drop(columns_to_del[i],1)

#creating dummies values
dummies_columns=list(data.columns.values)
data = pd.get_dummies(data, columns=dummies_columns, drop_first=True)

data.to_csv('SingleNeighbors.csv', encoding='utf-8', index=False)


X = pd.read_csv("SingleNeighbors.csv")
# k15 = KMeans(n_clusters=15,  precompute_distances = True, random_state=0)
# k15.fit(X)
# k7 = KMeans(n_clusters=7, precompute_distances = True, random_state=0)
# k7.fit(X)
k3 = KMeans(n_clusters=3, precompute_distances = True, random_state=0)
k3.fit(X)
# print(k15.labels_)
# print("============================")
# print(k7.labels_)
# print("=============================")
print(k3.labels_)
print("==============================")

result = pd.read_csv("Collegium.csv")
# result["k15"] = k15.labels_
# result["k7"] = k7.labels_
result["k3"] = k3.labels_
print(result.head())
result.to_csv('WithKmeansFeatures.csv', encoding='utf-8', index=False)





