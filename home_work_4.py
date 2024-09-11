# # home_work 4/1
""" Напишите программу, которая принимает список, содержащий вложенные списки,
 и возвращает новый список, содержащий все элементы из вложенных списков, без вложенности."""

list1 = [(1, 2, 0), (3, 4), (5, 2, 4, 10), (7, 8)]
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

list1 = [1, 2, 0, 3, '4', 5, 2, 4, 10, 7, 8]
print(list1)
target = 4
list2 = [i for i in list1 if int(i) != target]
print(list2)



# home_work 4/3

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = [17, 18, 11]
intersect_list = list(set(list1).intersection(list2))   # метод пересечения
if intersect_list:
    print(intersect_list)
else:
    print('no intersection')



# home_work 4/4

list1 = ['ab', 'a', 'abcdef', 'a', 'abcde', 'abc', 'abcd']
# 1
max_len_word = len(max(list1))
list2 = [word + '_' * (max_len_word - len(word)) for word in list1]
print(list2)
# 2
max_len = 1
for elem in range(len(list1)):
    if len(list1[elem]) > max_len:
        max_len = len(list1[elem])
list2 = [word + '_' * (max_len - len(word)) for word in list1]
print(list2)
