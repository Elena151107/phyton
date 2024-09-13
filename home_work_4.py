# home_work 4/1
""" Напишите программу, которая принимает список, содержащий вложенные списки,
 и возвращает новый список, содержащий все элементы из вложенных списков, без вложенности."""

list1 = [[1, 2, 0], [3, 4], [5, 2, 4, 10], [7, 8]]
print(list1)

# # 1
list2 = [ i for elem in list1 for i in elem]
print(list2)    #   [1, 2, 0, 3, 4, 5, 2, 4, 10, 7, 8]

# # 2
# list2 = []
# for el in list1:
#     for i in el:
#         list2.append(i)
# print(list2)   #   [1, 2, 0, 3, 4, 5, 2, 4, 10, 7, 8]



# home_work 4/2
""" Напишите программу, которая принимает список и значение,
и удаляет все вхождения этого значения из списка."""

list1 = [1, 2, 0, 3, '4', 5, 2, 4, 10, 7, 8]
print(list1)
target = 4
list2 = [ i for i in list1 if int(i) != target]
print(list2)    #   [1, 2, 0, 3, 5, 2, 10, 7, 8]



# home_work 4/3
""" Напишите программу, которая принимает два списка и возвращает True,
если первый список является подмножеством второго списка, и False в противном случае."""

list1 = [4, 9, 8,'t']
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 7]
flag = True
for elem in list2:
    for i in list1:
        if i not in list2:
            flag = False
            break
if flag == False:
    print('False')
else:
    print('True')

# intersect_list = list(set(list2).intersection(list1))   # метод пересечения
# if intersect_list:
#     print('True')
# else:
#     print('False')



# home_work 4/4
""" На входе имеем список строк разной длины. Необходимо написать программу,
которая вернет новый список из строк одинаковой длины. Длину итоговой строки
определяем исходя из самой большой из них. Если конкретная строка короче самой длинной,
дополнить ее нижними подчеркиваниями с правого края до требуемого количества символов.
Расположение элементов начального списка не менять."""

list1 = ['ab', 'a', 'abcdef', 'a', 'abcde', 'abc', 'abcd']

# # 1
max_len_word = len(max(list1))
list2 = [word + '_' * (max_len_word - len(word)) for word in list1]
print(list2)         #   ['ab____', 'a_____', 'abcdef', 'a_____', 'abcde_', 'abc___', 'abcd__']

# # 2
max_len = 1
for elem in range(len(list1)):
    if len(list1[elem]) > max_len:
        max_len = len(list1[elem])
list2 = [word + '_' * (max_len - len(word)) for word in list1]
print(list2)        #    ['ab____', 'a_____', 'abcdef', 'a_____', 'abcde_', 'abc___', 'abcd__']
