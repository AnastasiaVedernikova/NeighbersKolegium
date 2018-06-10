import pandas as pd
def create_dummies_for_pairs_dataframe(data):
    dict_dum={'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)': ["5:00  - 7:00", "7:00 - 9:00", "9:00 - 12:00"],
      'О котрій годині ви зазвичай лягаєте спати ввечері? ': ["21:00 - 22:00","22:00 - 23:00", "23:00 - 00:00", "після 00:00"],
    'Де ви надаєте перевагу харчуватись? [Трапезна УКУ]': ["Рідко", "Зазвичай", "Дуже часто"],
     'Де ви надаєте перевагу харчуватись? [Готую на кухні в колегіумі]': ["Рідко", "Зазвичай", "Дуже часто"],
      'Де ви надаєте перевагу харчуватись? [Кафе]' : ["Рідко", "Зазвичай", "Дуже часто"],
      'Чи займаєтесь ви спортом?': ["так", "ні"],
       'Як часто ви відвідуєте чи плануєте відвідувати  спортивний зал УКУ?':["Ніколи", "Час від часу", "Раз на тиждень",
                                                                              "Як мінімум двічі на тиждень"],
      'Вподобання у музиці [Рок]' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Поп]': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Реп]' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Класика]': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Джаз]' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Контемп]': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Латиноамериканська]': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Електро/ Металіка]': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Комедія]' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Драма]':["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Жахи]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Історичні та біографія]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Бойовики]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Фантастика та пригоди]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Детективи та кримінал]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мелодрами]': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мюзикли]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мультики]' : ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Роман]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Поезія]': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Детектив]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Фантастика]': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Психологія]':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Пригоди]': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Історичні]':["Ніколи", "Інколи", "Дуже часто"],
 'Як часто ви прибираєте?': ["Раз на місяць","Раз на тиждень", "Двічі на тиждень", "Кожного дня"],
 'Як часто ви приймаєте/ плануєте приймати гостей?':["Раз на рік","Раз на місяць", "Раз на тиждень", "Декілька разів протягом тижня"],
 'Релігія':["Християнство","Іслам","Юдаїзм","Буддизм","Атеїзм","Інше"],
 'Чи ви палите?':["так", "ні"],
 'Спосіб навчання [В компанії]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [З музикою]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [В кімнаті]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [Більше 5 годин на день]':["Ніколи", "Інколи", "Дуже часто"],
 'Скільки часу протягом дня проводите у ванній кімнаті?':["до 30 хв","до 1 год", "до 3 год"],
 'На скільки ви соціально активна людина?':["Надаю перевагу тиші та самотності",
                                            "Люблю спілкуватись та інколи хочу побути на самоті",
                                            "Завжди за нові знайомства та цікаві розмови"],
 'Чи відноситесь ви до вегетаріанців?':["так", "ні"],
 'Спосіб відпочинку [Вечірка в клубі]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Пісні під гітару]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Похід в гори]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Прогулянка парком]':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Подорожі до інших міст]':["Ніколи", "Інколи", "Дуже часто"],'k3':[0,1,2],
 'О котрій годині ви зазвичай прокидаєтесь зранку? (якщо це не залежить від розкладу пар, наприклад у вихідні)_Сусід_1': ["5:00  - 7:00", "7:00 - 9:00", "9:00 - 12:00"],
      'О котрій годині ви зазвичай лягаєте спати ввечері? _Сусід_1': ["21:00 - 22:00","22:00 - 23:00", "23:00 - 00:00", "після 00:00"],
    'Де ви надаєте перевагу харчуватись? [Трапезна УКУ]_Сусід_1': ["Рідко", "Зазвичай", "Дуже часто"],
     'Де ви надаєте перевагу харчуватись? [Готую на кухні в колегіумі]_Сусід_1': ["Рідко", "Зазвичай", "Дуже часто"],
      'Де ви надаєте перевагу харчуватись? [Кафе]_Сусід_1' : ["Рідко", "Зазвичай", "Дуже часто"],
      'Чи займаєтесь ви спортом?_Сусід_1': ["так", "ні"],
       'Як часто ви відвідуєте чи плануєте відвідувати  спортивний зал УКУ?_Сусід_1':["Ніколи", "Час від часу", "Раз на тиждень",
                                                                              "Як мінімум двічі на тиждень"],
      'Вподобання у музиці [Рок]_Сусід_1' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Поп]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Реп]_Сусід_1' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Класика]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Джаз]_Сусід_1' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Контемп]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Латиноамериканська]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у музиці [Електро/ Металіка]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Комедія]_Сусід_1' : ["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Драма]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
      'Вподобання у фільмах [Жахи]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Історичні та біографія]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Бойовики]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Фантастика та пригоди]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Детективи та кримінал]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мелодрами]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мюзикли]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у фільмах [Мультики]_Сусід_1' : ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Роман]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Поезія]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Детектив]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Фантастика]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Психологія]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Пригоди]_Сусід_1': ["Ніколи", "Інколи", "Дуже часто"],
 'Вподобання у книгах [Історичні]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Як часто ви прибираєте?_Сусід_1': ["Раз на місяць","Раз на тиждень", "Двічі на тиждень", "Кожного дня"],
 'Як часто ви приймаєте/ плануєте приймати гостей?_Сусід_1':["Раз на рік","Раз на місяць", "Раз на тиждень", "Декілька разів протягом тижня"],
 'Релігія_Сусід_1':["Християнство","Іслам","Юдаїзм","Буддизм","Атеїзм","Інше"],
 'Чи ви палите?_Сусід_1':["так", "ні"],
 'Спосіб навчання [В компанії]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [З музикою]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [В кімнаті]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб навчання [Більше 5 годин на день]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Скільки часу протягом дня проводите у ванній кімнаті?_Сусід_1':["до 30 хв","до 1 год", "до 3 год"],
 'На скільки ви соціально активна людина?_Сусід_1':["Надаю перевагу тиші та самотності",
                                            "Люблю спілкуватись та інколи хочу побути на самоті",
                                            "Завжди за нові знайомства та цікаві розмови"],
 'Чи відноситесь ви до вегетаріанців?_Сусід_1':["так", "ні"],
 'Спосіб відпочинку [Вечірка в клубі]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Пісні під гітару]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Похід в гори]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Прогулянка парком]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],
 'Спосіб відпочинку [Подорожі до інших міст]_Сусід_1':["Ніколи", "Інколи", "Дуже часто"],'k3_Сусід_1':[0,1,2]}
    columns = data.columns.values
    for i in columns:
     list_of_values_in_column = data[i]
     for j in dict_dum[i]:
      list_of_new_values_in_new_column = []
      for k in list_of_values_in_column:
       if k == j:
        list_of_new_values_in_new_column.append(1)
       else:
        list_of_new_values_in_new_column.append(0)
      col_name = str(i)+"_"+str(j)
      data[col_name] = list_of_new_values_in_new_column
     data = data.drop(i,1)
    #print(len(data.columns.values))
    return data




