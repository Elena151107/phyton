# # home_work 5/1
""" Напишите программу, которая принимает на вход два списка
и возвращает множество из элементов, которые встречаются в обоих списках. """
list1 = [2, 8, 9, 55, 78, 2, 1, 0, 9, 22, 33]
list2 = [1, 0, 88, 999, 22, 44, 55, 44, 0, 3]
set1 = set(list1)
print(set1)
set2 = set(list2)
print(set2)
print(set1.intersection(set2))
## print(set(list1).intersection(set(list2)))


# # home_work 5/2
""" Создайте список кортежей, представляющих пары (страна, столица). Напишите программу, которая
принимает на вход название страны и выводит её столицу, если она есть в списке, или сообщение об
ошибке, если страна отсутствует. """
list_tuple = [('Россия', 'Москва'), ('Италия', 'Рим'), ('Франция', 'Париж'), ('Тайланд', 'Бангкок'),
              ('Япония', 'Токио'), ('Южная Корея', 'Сеул'), ('Китай', 'Пекин'), ('Греция', 'Афины'),
              ('Турция', 'Анкара'), ('Мексика', 'Мехико')]
list_tuple_2 = [i for elem in list_tuple for i in elem]
name_country = input('Country: ')
if name_country not in list_tuple_2:
    print('This country have not in this list of countries')
else:
    for elem in list_tuple:
        country = elem[0]
        capital = elem[1]
        if name_country == country:
            print(f'The capital of {name_country} is {capital}')



# # home_work 5/3
""" Создайте кортеж, содержащий несколько списков. Напишите программу,
 которая выводит все уникальные элементы из всех списков в кортеже.  """
tup_1 = ([4, 8, 4, 9, 2, 8, 2], [44, 'p', 44, 'l', 44], [1, 0, 1, 0, 't', 1, 0], [4, 8, 4, 8, 'p'])
print(tup_1)
## 1
list_unique = [i for elem in [list(set(elem)) for elem in tup_1] for i in elem]
print(list_unique)    #  [8, 9, 2, 4, 44, 'p', 'l', 0, 1, 't', 8, 4, 'p']
## 2
unique_elem = [list(set(elem)) for elem in tup_1]
list_unique = [i for elem in unique_elem for i in elem]
print(list_unique)    #  [8, 9, 2, 4, 'l', 44, 'p', 0, 1, 't', 8, 4, 'p']


# # home_work 5/4
""" Напишите программу, которая принимает строку и возвращает множество из всех уникальных символов в
этой строке.  """
str1 = 'Мир мир, мир / мир / мир = 5 = 55 = 555!'
list1 = [i for elem in str1.split() for i in elem]
print(set(list1))    #  {'р', '!', ',', 'и', 'М', 'м', '5', '/', '='}



# # home_work 5/5
""" Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод
на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных.
Используйте словарь для хранения информации.  """
dict_eng_franc = {}
while True:
    print()
    action = int(input('Выберите действие: \n1 - Добавить новое слово'
                       '\n2 - Удалить слово\n3 - Поиск слова\n4 - Изменить слово'
                       '\n5 - Показать весь словарь\n0 - Выход.  '))
    if action == 1:
        word = input('Input your word in english: ')
        translation = input('Input translation in french: ')
        dict_eng_franc[word] = {
            'translation': translation
        }
        print()
        print(f'Слово [{word}] было добавлено в словарь')
        print()
    elif action == 2:
        word = input('Input your word in english: ')
        if word in dict_eng_franc:
            del dict_eng_franc[word]
            print()
            print(f'Слово [{word}] удалено')
        else:
            print()
            print(f'Слово [{word}] не найдено')
    elif action == 3:
        word = input('Input your word in english: ')
        if word in dict_eng_franc:
            print()
            print(f'Вы искали слово: [{word}]  перевод: [{dict_eng_franc[word]['translation']}]')
        else:
            print()
            print(f'Слово [{word}] не найдено')
    elif action == 4:
        word = input('Input your word in english: ')
        if word in dict_eng_franc:
            print()
            print('Оставьте пустым, чтобы не менять')
            print()
            translation = input('Input translation in french: ')
            if translation:
                dict_eng_franc[word]['translation'] = translation
                print()
                print(f'Перевод [{translation}] обновлен')
        else:
            print()
            print(f'Слово [{word}] не найдено')
    elif action == 5:
        if dict_eng_franc:
            for word, translation in dict_eng_franc.items():
                print(f' Слово [{word}]: перевод [{dict_eng_franc[word]['translation']}]')
        else:
            print()
            print('Словарь пуст!')
    elif action == 0:
        break
    else:
        print()
        print('mistake')
