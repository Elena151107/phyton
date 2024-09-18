# # home_work 6/1
""" Напишите функцию, которая возвращает минимальное из пяти чисел. Числа передаются в качестве параметров"""
   # 1
def min_numbers(list_numbers):
    return  min(list_numbers)
list_numbers = []
print(min_numbers([54, 118, 1118, 19, 66]))
   # 2
def min_numbers(*args):   # распаковка списка
    return min(args)
print(min_numbers(6, 40, 11, 5, 10))


# # home_work 6/2
""" Напишите функцию, высчитывающую степень каждого элемента списка целых. Значение для степени
передаётся в качестве параметра, список тоже передаётся в качестве параметра. Функция возвращает
новый список, содержащий полученные результаты."""
def power_nums(n,list_numbers):
    list_nums_new = [i ** n  for i in list_numbers]
    return list_nums_new
list_numbers = []
print(power_nums(3, [2, 4, 3, 5, 10, 6]))


# # home_work 6/3
""" Дата некоторого дня характеризуется тремя натуральными числами: g (год), m (порядковый номер
месяца) и n (число). По заданным g, n и m определить: 
а) дату предыдущего дня;
б) дату следующего дня.
Определить функцию, подсчитывающую количество дней в том или ином месяце. В обеих задачах рассмотреть два
случая:
1) заданный год не является високосным;
2) заданный год может быть високосным. """

def isleap_year(g):           # проверка на високосный год
    if (g % 4 == 0 and g % 100 != 0) or g % 400 == 0:
        return True
def show_date_before(n, m, g):
    print(f'Текущая дата: {"0" if n < 10 else ""}{n}:{"0" if m < 10 else ""}{m}:{g}')   
    if n == 1 and m != 1:      # для февраля (високосного/невисокосного года) и первого числа месяца
        if (m - 1) == 2:
            if isleap_year(g):
                list_dates = range(1, 30)
            else:
                list_dates = range(1, 29)
        elif (m - 1) == 4 or (m - 1) == 6 or (m - 1) == 9 or (m - 1) == 11:
            list_dates = range(1, 31)
        else:
            list_dates = range(1, 32)
        m = m - 1
        n = list_dates[-1]
    elif n == 1 and m == 1:    # если дата 01.01.20,,,
        m = 12
        n = 31
        g = g - 1
    else:
        if n != 1:
            n = n - 1
    print(f'Дата предыдущего дня: {"0" if n < 10 else ""}{n}:{"0" if m < 10 else ""}{m}:{g}\n')
def show_date_after(n, m, g):
    print(f'Текущая дата: {"0" if n < 10 else ""}{n}:{"0" if m < 10 else ""}{m}:{g}')
    if m == 2 and n == 28:
        if isleap_year(g):     # для февраля (високосного/невисокосного года)
            n = n + 1
        else:
            n = 1
            m = m + 1
    elif m == 2 and n == 29:
        n = 1
        m = m + 1
    elif m == 12 and n == 31:
        n = 1
        m = 1
        g = g + 1
    elif m == 4 or m == 6 or m == 9 or m == 11:
        if n == 30:
            n = 1
            m = m + 1
        else:
            n = n + 1
    else:
        if n == 31:
            n = 1
            m = m + 1
        else:
            n = n + 1
    print(f'Дата следующего дня: {"0" if n < 10 else ""}{n}:{"0" if m < 10 else ""}{m}:{g}')

show_date_before(1, 3, 2023 )
show_date_after(28, 2, 2023 )


