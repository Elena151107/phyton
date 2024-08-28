# Задание 1. Пользователь вводит с клавиатуры три числа. Необходимо найти сумму чисел, произведение чисел. Результат вычислений вывести на экран.

number_1 = int(input('Введите первое число: '))
number_2 = int(input('Введите второе число: '))
number_3 = int(input('Введите третье число: '))
amount = number_1 + number_2 + number_3
product_numbers = number_1 * number_2 * number_3
print(f'Сумма трех чисел: {amount}')
print(f'Произведение трех чисел: {product_numbers}')

