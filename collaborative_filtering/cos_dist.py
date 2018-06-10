
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import math
def cos_dist():
    data = pd.read_csv("WithoutOneCollegium.csv")
    #pairs
    start = 'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)_7:00 - 9:00'
    mid_st = 'Спосіб відпочинку [Подорожі до інших міст]_Дуже часто'
    mid = 'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)_Сусід_1_7:00 - 9:00'
    x = data.loc[:, start:mid_st]
    y = data.loc[:, mid::]

    cos_sim = [cosine_similarity(x.loc[[i]].values, y.loc[[i]].values) for i in range(len(x))]
    #print(cos_sim)

    simple_cos_sim = []
    for a in cos_sim:
        for b in a:
            for c in b:
                simple_cos_sim.append(c)
    #print(simple_cos_sim)

    degrees = []
    for i in simple_cos_sim:
        angle_in_radians = math.acos(i)
        degrees.append(math.degrees(angle_in_radians))
    #print(degrees)

    # label = data['Oцінка задоволення сусідом']
    # #print(label)
    # comparison =[[label[i], degrees[i]] for i in range(len(degrees))]
    #print(comparison)
    #interpretatiion of degrees
    #0-50 - similar
    #50-90 - uncorrelated not similar
    #180 - opposite
    # two=[i for i in comparison if i[0] == 2]
    # three =[i for i in comparison if i[0] == 3]
    # four = [i for i in comparison if i[0] == 4]
    # five = [i for i in comparison if i[0] == 5]
    #
    # import numpy as np
    # print(np.mean([round(i[1],1) for i in five]))
    return degrees

