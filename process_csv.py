import pandas as pd
data = pd.read_csv("Сусідство.csv")
#print(list(data.columns.values))
dummies_columns=['О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)',
                 'О котрій годині ви зазвичай лягаєте спати ввечері? ',
                 'Де ви надаєте перевагу харчуватись? [Трапезна УКУ]',
                 'Де ви надаєте перевагу харчуватись? [Готую на кухні в колегіумі]',
                 'Де ви надаєте перевагу харчуватись? [Кафе]',
                 'Як часто ви відвідуєте чи плануєте відвідувати  спортивний зал УКУ?',
                 'Вподобання у музиці [Рок]', 'Вподобання у музиці [Поп]', 'Вподобання у музиці [Реп]',
                 'Вподобання у музиці [Класика]', 'Вподобання у музиці [Джаз]',
                 'Вподобання у музиці [Контемп]', 'Вподобання у музиці [Латиноамериканська]',
                 'Вподобання у музиці [Електро/ Металіка]', 'Вподобання у фільмах [Комедія]',
                 'Вподобання у фільмах [Драма]', 'Вподобання у фільмах [Жахи]',
                 'Вподобання у фільмах [Історичні та біографія]', 'Вподобання у фільмах [Бойовики]',
                 'Вподобання у фільмах [Фантастика та пригоди]', 'Вподобання у фільмах [Детективи та кримінал]',
                 'Вподобання у фільмах [Мелодрами]', 'Вподобання у фільмах [Мюзикли]',
                 'Вподобання у фільмах [Мультики]', 'Вподобання у книгах [Роман]', 'Вподобання у книгах [Поезія]',
                 'Вподобання у книгах [Детектив]','Вподобання у книгах [Фантастика]', 'Вподобання у книгах [Психологія]',
                 'Вподобання у книгах [Пригоди]', 'Вподобання у книгах [Історичні]', 'Як часто ви приймаєте/ плануєте приймати гостей?',
                 'Релігія','Спосіб навчання [В компанії]', 'Спосіб навчання [З музикою]', 'Спосіб навчання [В кімнаті]',
                 'Спосіб навчання [Більше 5 годин на день]','Скільки часу протягом дня проводите у ванній кімнаті?',
                 'На скільки ви соціально активна людина?','Спосіб відпочинку [Вечірка в клубі]',
                 'Спосіб відпочинку [Пісні під гітару]', 'Спосіб відпочинку [Похід в гори]',
                 'Спосіб відпочинку [Прогулянка парком]','Спосіб відпочинку [Подорожі до інших міст]']
data = pd.get_dummies(data, columns=dummies_columns)

#changing first column from time stamp to ID
for i in range(len(data.index)):
    data.at[i, 'Позначка часу'] = i
data.rename(columns={'Позначка часу':'ID'}, inplace=True)

#clean numbers of rooms
data.at[79,'Вкажіть номер кімнати в гуртожитку'] = 203
data.at[92,'Вкажіть номер кімнати в гуртожитку'] = 4
data.at[31,'Вкажіть номер кімнати в гуртожитку'] = 5
data.at[34,'Вкажіть номер кімнати в гуртожитку'] = 5
data.at[37,'Вкажіть номер кімнати в гуртожитку'] = 5

def FindNeighbors(room):
    #return list of ids wih same room number
    neighbors = []
    for i in data['ID']:
        if data.at[room,'Вкажіть номер кімнати в гуртожитку'] == data.at[i,'Вкажіть номер кімнати в гуртожитку'] and room!=i:
            #add new row
            neighbors.append(i)
    return neighbors

def CreateDictionaryOfNeighbors():
    #creation of dictionary with neighbors
    d = {}
    for i in data['ID']:
        d[i] = FindNeighbors(i)
    return d
d = CreateDictionaryOfNeighbors()

def FirstNeighborsID():
    #fill first column with ids of neighbors
    list_of_first_neighbors=[]
    for i in data['ID']:
        if len(list(d.values())[i]) > 0:
            list_of_first_neighbors.append((list(d.values())[i])[0])
        else:
            list_of_first_neighbors.append("--no value--")
    data['ID Сусід_1'] = list_of_first_neighbors

FirstNeighborsID()

old_names_of_columns = list(data.columns.values)[1:-1]
def FirstNeighbor():
    #general filling for first neighbor
    #old_names_of_columns = list(data.columns.values)[1:-1] #old names of columns
    names_for_columns_neighbor_1 = []
    for i in old_names_of_columns:
        names_for_columns_neighbor_1.append(i+" Сусід_1")

    for i in range(len(names_for_columns_neighbor_1)):
        inf_of_neighbor = []
        for k in data['ID Сусід_1']:
            if k == "--no value--":
                inf_of_neighbor.append("--no value--")
            else:
                inf_of_neighbor.append(data[old_names_of_columns[i]][k])#email with id = k
        data[names_for_columns_neighbor_1[i]] = inf_of_neighbor

FirstNeighbor()

def SecondNeighborsID():
    #fill second column with ids of neighbors
    list_of_second_neighbors=[]
    for i in data['ID']:
        if len(list(d.values())[i]) > 1:
            list_of_second_neighbors.append((list(d.values())[i])[1])
        else:
            list_of_second_neighbors.append("--no value--")
    data['ID Сусід_2'] = list_of_second_neighbors

SecondNeighborsID()

def SecondNeighbor():
    #general filling for second neighbor
    names_for_columns_neighbor_2 = []
    for i in old_names_of_columns:
        names_for_columns_neighbor_2.append(i+" Сусід_2")

    for i in range(len(names_for_columns_neighbor_2)):
        inf_of_neighbor = []
        for k in data['ID Сусід_2']:
            if k == "--no value--":
                inf_of_neighbor.append("--no value--")
            else:
                inf_of_neighbor.append(data[old_names_of_columns[i]][k])#email with id = k
        data[names_for_columns_neighbor_2[i]] = inf_of_neighbor

SecondNeighbor()

def ThirdNeighborsID():
    #fill third column with ids of neighbors
    list_of_third_neighbors=[]
    for i in data['ID']:
        if len(list(d.values())[i]) > 2:
            list_of_third_neighbors.append((list(d.values())[i])[2])
        else:
            list_of_third_neighbors.append("--no value--")
    data['ID Сусід_3'] = list_of_third_neighbors

ThirdNeighborsID()

def ThirdNeighbor():
    #general filling for third neighbor
    names_for_columns_neighbor_3 = []
    for i in old_names_of_columns:
        names_for_columns_neighbor_3.append(i+" Сусід_3")

    for i in range(len(names_for_columns_neighbor_3)):
        inf_of_neighbor = []
        for k in data['ID Сусід_3']:
            if k == "--no value--":
                inf_of_neighbor.append("--no value--")
            else:
                inf_of_neighbor.append(data[old_names_of_columns[i]][k])#email with id = k
        data[names_for_columns_neighbor_3[i]] = inf_of_neighbor

ThirdNeighbor()

def AverageLevelOfSatisfying():
    general_levels_of_satisfying = []
    for i in data['ID']:
        levels_of_satisfying=[]#id=1
        levels_of_satisfying.append(list(data['Оцініть ваш рівень задоволення життя разом з ними '])[i])
        levels_of_satisfying.append(list(data['Оцініть ваш рівень задоволення життя разом з ними  Сусід_1'])[i])
        levels_of_satisfying.append(list(data['Оцініть ваш рівень задоволення життя разом з ними  Сусід_2'])[i])
        levels_of_satisfying.append(list(data['Оцініть ваш рівень задоволення життя разом з ними  Сусід_3'])[i])
        num=0
        sum=0
        for k in levels_of_satisfying:
            if k!='--no value--':
                num+=1
                sum+=k
        if num>1:
            general_levels_of_satisfying.append(sum/num)
        else:
            general_levels_of_satisfying.append('--no value--')
    data['Середня оцінка задоволення сусідом'] = general_levels_of_satisfying

AverageLevelOfSatisfying()
print(data)
data.to_csv(r'D:\MachineLearning\ProcessedKolegium.csv')

#print(data.head())





