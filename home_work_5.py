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
#print(set(list1).intersection(set(list2)))


# # home_work 5/2
""" Создайте список кортежей, представляющих пары (страна, столица). Напишите программу, которая
принимает на вход название страны и выводит её столицу, если она есть в списке, или сообщение об
ошибке, если страна отсутствует. """





# # home_work 5/3
""" Создайте кортеж, содержащий несколько списков. Напишите программу,
 которая выводит все уникальные элементы из всех списков в кортеже.  """
tup_1 = ([4, 8, 4, 9, 2, 8, 2], [44, 'p', 44, 'l', 44], [1, 0, 1, 0, 't', 1, 0], [4, 8, 4, 8, 'p'])
# tup_1 = ((4, 8, 4, 9, 2, 8, 2), (44, 'p', 44, 'l', 44), (1, 0, 1, 0, 't', 1, 0), (4, 8, 4, 8, 'p'))
print(tup_1)
unique_elem = [list(set(elem)) for elem in tup_1]
print(unique_elem)    # [[8, 9, 2, 4], ['p', 44, 'l'], [0, 1, 't'], [8, 4, 'p']]



# # home_work 5/4
""" Напишите программу, которая принимает строку и возвращает множество из всех уникальных символов в
этой строке.  """
str1 = 'Мир мир, мир / мир / мир = 5 = 55 = 555!'
list1 = [i for elem in str1.split() for i in elem]
print(set(list1))



# # home_work 5/5
""" Создайте программу «Англо-французский словарь». Нужно хранить слово на английском языке и его перевод
на французский. Требуется реализовать возможность добавления, удаления, поиска, замены данных.
Используйте словарь для хранения информации.  """

