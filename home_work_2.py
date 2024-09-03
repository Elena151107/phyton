

"""  Домашнее задание 2.2.
     Пользователь вводит с клавиатуры арифметическое выражение. 
     Например, 23+12.Необходимо вывести на экран результат выражения.
     В нашем примере это 35. Арифметическое выражение может состоять только из
     трёх частей: число, операция, число. Возможные операции: +, -, *, /.
"""

while True:
    s = input('Введите арифметическое выражение (0 - выход):  ')
    if s == '0':
        break
    else:
        list_s = []
        for i in range(len(s)):
            list_s.append(s[i])
        print()

        num1 = []
        math = []
        count = 0
         
        for elem in list_s:
            if elem.isdigit():
                num1.append(elem)
                count+=1
            if elem == '+' or elem == '-' or elem == '*' or elem == '/':
                math.append(elem)
                break
                 
    n = count + 1
    num2 = int(s[n:])
    num1 = int(''.join(num1))
    math = ''.join(math)
    print(num1)
    print(math)
    print(num2)

    if math == '+':
        result = num1 + num2
        print(f'Сумма чисел: {result}')
    elif math == '-':
        result = num1 - num2
        print(f'Разность чисел: {result}')
    elif math == '*':
        result = num1 * num2
        print(f'Сумма операции умножения чисел: {result}')
    elif math == '/':
        result = num1 / num2
        print(f'Сумма операции деления чисел: {result}')
    else:
        print('Неверная запись арифметического выражения')




"""  Домашнее задание 2.3. 
     Создайте программу, которая будет принимать на вход
     строку и выводить на экран все подстроки этой строки.
"""
s = 'Сидел барсук в своей норе и ел картошечку пюре'
list_s = s.split()
print(list_s)
print()
for char in list_s:
    print(char)



"""  Домашнее задание 2.4.
     Создайте программу, которая будет принимать на вход
     строку и выводить количество букв, цифр и специальных
     символов в этой строке.
"""
s = 'Сидел барсук 5 часов и ел 3 кг пюре + 200 гр моркови за 900 $'
list_s = s.split()
print(list_s)
letter = []
dig = []

for elem in list_s:
    for i in range(len(elem)):
        if elem[i].isdigit():
           dig.append(elem[i])
        elif elem[i].isalpha():
            letter.append(elem[i])
        else:
            print('And have another simbols in this string')
print(dig)
print(letter)
simbols = len(s) - len(dig) - len(letter)
print(f'Длина строки: {len(s)}')
print(f'Количество цифр в строке: {len(dig)}')
print(f'Количество букв в строке: {len(letter)}')
print(f'Количество символов в строке: {simbols}')


