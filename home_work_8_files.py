# # home_work 8
""" Напишите информационную систему «Сотрудники».
Программа должна обеспечивать ввод данных, редактирование данных сотрудника, удаление сотрудника,
поиск сотрудника по фамилии, вывод информации обо всех сотрудниках, указанного возраста, или фамилия которых
начинается на указанную букву. Организуйте возможность сохранения найденной информации в файл. 
Также весь список сотрудников сохраняется в файл (при выходе из программы — автоматически). 
При старте программы происходит загрузка списка сотрудников из указанного пользователем файла."""

import os
def add_info(file_name, family, age):
    with open(file_name, 'a', encoding='utf-8') as f:
        f.write(f'{family.upper()}:{age}\n')

def change_info(file_name, family, family_new, age_new):
    lines = []
    lines_redact = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith(family):
                lines.append(line)
            elif line.startswith(family):
                lines_red = f'{family_new}:{age_new}\n'
                lines_redact.append(lines_red)
    with open(file_name, 'w', encoding='utf-8') as f:
        print(f.writelines(lines + lines_redact))

def delete_info(file_name, family):
    lines = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if not line.startswith(family):
                lines.append(line)
    with open(file_name, 'w', encoding='utf-8') as f:
        f.writelines(lines)

def search_employee(file_name, family):
    lines = ''
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if line.startswith(family):
                lines += line
        return lines

def show_all_info(file_name, action):
    lines = []
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            if action == line[0]:
                lines.append(line)
            elif action.isdigit() and len(action) == 2 and action in line:
                lines.append(line)
        for line in lines:
            print(line)

def main():
    file_name = os.path.join(os.path.dirname(__file__), 'information_employees.txt')
    while True:
        choice = int(input("""Выберите действие:
                 1. ВВОД ДАННЫХ
                 2. РЕДАКТИРОВАНИЕ
                 3. УДАЛЕНИЕ
                 4. ПОИСК СОТРУДНИКА
                 5. ВЫВЕСТИ СПИСОК СОТРУДНИКОВ
                 6. ВЫХОД   """))
        if choice == 6:
            break
        elif choice == 1:
            fam = input('Введите фамилию и имя нового сотрудника: ')
            family = fam.upper()
            age = input('Укажите возраст нового сотрудника: ')
            add_info(file_name, family, age)
        elif choice == 2:
            fam = input('Введите фамилию, если хотите что-то изменить: ')
            family = fam.upper()
            print('Укажите новую фамилию и новый возраст сотрудника: ')
            fam = input('Введите фамилию, если хотите что-то изменить: ')
            family_new = fam.upper()
            age_new= input('новый возраст сотрудника: ')
            change_info(file_name, family, family_new, age_new)
        elif choice == 3:
            fam = input('Введите фамилию сотрудника, которого необходимо удалить из базы данных: ')
            family = fam.upper()
            if family == '':
                raise ValueError('Mistake! Input again!')
            else:
                delete_info(file_name, family)
        elif choice == 4:
            fam = input('Введите фамилию сотрудника, которого нужно найти: ')
            family = fam.upper()
            print(search_employee(file_name, family))
        elif choice == 5:
            action = input("Чтобы вывести список сотрудников напишите первую букву фамилии или возраст: ")
            if not action.isdigit():
                action = action.upper()
            print(show_all_info(file_name, action))
        else:
            print('Неверный выбор! Попробуйте снова')
main()
