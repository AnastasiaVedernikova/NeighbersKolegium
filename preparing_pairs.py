import pandas as pd

#reading csv
data = pd.read_csv("Сусідство.csv")

#creating ID column
for i in range(len(data.index)):
    data.at[i, 'Позначка часу'] = i
data.rename(columns={'Позначка часу':'ID'}, inplace=True)

#deleting inf that does not influence on satisfying level of living together
columns_to_del = ["Електронна адреса", "Прізвище та ім'я", "Вкажіть будь-ласка посилання на ваш facebook, для того щоб ваші потенційні сусіди могли зв'язатись з вами.",
           "Назвіть імена та прізвища ваших сусідів по кімнаті"]
for i in range(len(columns_to_del)):
    data = data.drop(columns_to_del[i],1)

#clean numbers of rooms
data.at[79,'Вкажіть номер кімнати в гуртожитку'] = 203
data.at[92,'Вкажіть номер кімнати в гуртожитку'] = 4
data.at[31,'Вкажіть номер кімнати в гуртожитку'] = 5
data.at[34,'Вкажіть номер кімнати в гуртожитку'] = 5
data.at[37,'Вкажіть номер кімнати в гуртожитку'] = 5

def find_neighbors(room):
    #return list of ids wih same room number
    neighbors = []
    for i in data['ID']:
        if data.at[room,'Вкажіть номер кімнати в гуртожитку'] == data.at[i,'Вкажіть номер кімнати в гуртожитку'] and room!=i:
            neighbors.append(i)
    return neighbors

def create_dictionary_of_neighbors():
    #creation of dictionary with neighbors
    d = {}
    for i in data['ID']:
        d[i] = find_neighbors(i)
    return d
d = create_dictionary_of_neighbors()

def first_neighbors_id():
    #fill first column with ids of neighbors
    list_of_first_neighbors=[]
    for i in data['ID']:
        if len(list(d.values())[i]) > 0:
            list_of_first_neighbors.append((list(d.values())[i])[0])
        else:
            list_of_first_neighbors.append(0)
    data['ID_Сусід_1'] = list_of_first_neighbors

first_neighbors_id()

#deleting rows that does not have a neighbor
data = data[data.ID_Сусід_1 !=0]

old_names_of_columns = list(data.columns.values)[1:-1]
def first_neighbor():
    #general filling for first neighbor
    names_for_columns_neighbor_1 = []
    for i in old_names_of_columns:
        names_for_columns_neighbor_1.append(i+"_Сусід_1")

    for i in range(len(names_for_columns_neighbor_1)):
        inf_of_neighbor = []
        for k in data['ID_Сусід_1']:
                inf_of_neighbor.append(data[old_names_of_columns[i]][k])#email with id = k
        data[names_for_columns_neighbor_1[i]] = inf_of_neighbor

first_neighbor()

#calculating average level of satisfying living together
def average_level_of_satisfying():
    general_levels_of_satisfying = []
    for i in range(len(data)):
        sum=0
        sum+=(list(data['Оцініть ваш рівень задоволення життя разом з ними '])[i])
        sum+=(list(data['Оцініть ваш рівень задоволення життя разом з ними _Сусід_1'])[i])
        general_levels_of_satisfying.append(sum/2)
    data['Середня оцінка задоволення сусідом'] = general_levels_of_satisfying
average_level_of_satisfying()

#deleting ID, Number of room, Level of satisfying for each

to_del = ["ID","Вкажіть номер кімнати в гуртожитку","Оцініть ваш рівень задоволення життя разом з ними ","ID_Сусід_1","Вкажіть номер кімнати в гуртожитку_Сусід_1", "Оцініть ваш рівень задоволення життя разом з ними _Сусід_1"]
for i in range(len(to_del)):
     data = data.drop(to_del[i],1)

#creating dummies values
dummies_columns=list(data.columns.values)[:-1]
data = pd.get_dummies(data, columns=dummies_columns, drop_first=True)

print(data.head())
#Y - first column
#X - all others
data.to_csv('D:\MachineLearning\ProcessedKolegium.csv', encoding='utf-8', index=False)
