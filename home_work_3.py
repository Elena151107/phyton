"""  Домашнее задание 3.1.
     Напишите программу, которая извлекает из текста все слова,
     начинающиеся с буквы "а" или "А". Используйте регулярные
     выражения для поиска слов.
        Требования:
     - Программа должна извлекать слова, начинающиеся с
     буквы "а" или "А", независимо от регистра.
     - Программа должна игнорировать пробелы и знаки препинания.
"""
import re
text = 'Andru and Anna, are very happy mamma and papa ... happyAND!'
print(text)
pattern = r"[^\s]^|\b[aA]\w*"     # result   ['Andru', 'and', 'Anna', 'are', 'and']
#pattern = r" ^|\b[aA]\w*"        # result   ['Andru', 'and', 'Anna', 'are', 'and']
print(re.findall(pattern, text))



"""  Домашнее задание 3.2.
     Напишите программу, которая заменяет все вхождения
     слова "old" на слово "new" в тексте. Используйте регулярные
     выражения для замены текста.
        Требования:
     - Программа должна заменять все вхождения слова "old", независимо от регистра.
     - Программа должна игнорировать пробелы и знаки препинания.  
"""
import re
text = 'Old my words: OLDer, old, Old! oLD and OLd and hold old women is very good olD oldnew newold olLdd'
print(text)
pattern = r"[^\s]^|\b[oO][lL]([dD]\b)"    # result  (new my words: OLDer, new, new! new and new and hold new women is very good new oldnew newold olLdd)
#pattern = r" ^|\b[oO][lL]([dD]\b)"       # result  (new my words: OLDer, new, new! new and new and hold new women is very good new oldnew newold olLdd)
new_text = re.sub(pattern, 'new', text)
print(new_text)



"""  Домашнее задание 3.3.
     Напишите программу, которая извлекает из текста все целые числа.
     Используйте регулярные выражения для поиска чисел.
        Требования:
     - Программа должна извлекать целые числа, независимо от регистра.
     - Программа должна игнорировать пробелы и знаки препинания.  
"""
import re
text = 'my digits 15 in this 2 string = 23.899 but is not and 7/8'
print(text)
pattern = r"\d{1,}"       ## result  ['15', '2', '23', '899', '7', '8']
#pattern = r" \d{1,}"     ## result  [' 15', ' 2', ' 23', ' 7']
list_dig = re.findall(pattern, text)
print(list_dig)



"""  Домашнее задание 3.4.
     Напишите программу, которая проверяет, является ли введенная строка
     действительным телефонным номером в формате "+X (XXX) XXX-XXXX". Используйте регулярные
     выражения для проверки формата телефонного номера.
       Требования:
     - Телефонный номер должен содержать символ "+" в начале.
     - Телефонный номер должен содержать символы "()" и "-" в соответствующих местах.
     - Телефонный номер должен содержать ровно 12 цифр. 
"""
import re
phone_number = input('Input your phone number (example: +X (XXX) XXX-XXXX): ')
pattern = r"^\+\d{1}\s\(\d{3}\)\s\d{3}\-\d{4}$"
if re.match(pattern, phone_number):
    print('right format phone number')
else:
    print('mistake')



"""  Домашнее задание 3.5.
     Напишите программу, которая проверяет, является ли введенная строка
     действительным временем в формате "ЧЧ:ММ:СС". 
     Используйте регулярные выражения для проверки формата времени.
       Требования:
     - Время должно содержать ровно 8 символов.
     - Время должно содержать символы ":" в качестве разделителей.
     - Часы должны быть в диапазоне от 00 до 23.
     - Минуты и секунды должны быть в диапазоне от 00 до 59.
"""
import re
time = input('Input your time, please: ')
pattern = r"^(0[1-9]|1\d{1}|2[0123]):(0[1-9]|[12345]\d{1}):(0[1-9]|[12345]\d{1})$"
if re.match(pattern, time):
    print('right format time')
else:
    print('mistake')
