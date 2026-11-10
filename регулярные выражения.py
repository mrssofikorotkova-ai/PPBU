# регулярные выражения представляют собой маску,
# которую можем одеть на текст и соответствует текст "трафарету"-маске
#re - библиотека регулярных выражений
#search - метод библиотеки re

"""Match    match = re.search(regex, string)"""
#regex -  маска
#string - строка
import re
#match - ф-ция обрабатывает если сначала совпадение,
#если нет возвращает где, если нет. то возвращает None
res = re.match(r'AV', 'A1V_avia')
#search - ф-ция ищет совпадение в любом месте строки первое которое попало
res = re.search(r'AV', 'regAV_avia')
#findall - ф-ция показывает все совпадения в строке
res = re.findall(r'AV', 'regAV_AV_avia')
#finditer - будет выдавать каждое совпадение по очереди
res = re.finditer(r'AV', 'regAV_AV_avia')
#fullmatch - обеспечивает полное совпадение строки с регулярным выражением
res = re.fullmatch(r'AV', 'AV')
print(res)
res = re.sub(r'что меняем', 'на что меняем', 'где меняем')
res = re.split(r'p','PerspectivePe', maxsplit = 2, flags = re.IGNORECASE)
print(res)
#
pattern = re.compile(r'AV')
res = pattern.findall('fsedfAV')

#""" Спецсимволы
#\d - любая цифра
#\D - любое не числовое значение

#\s - символы пробелов
#\S - все кроме пробела

#\w - буква, цифра и нижнее подчеркивание
#\W - все кроме: буквы, цифры и нижнего подчеркивания

#.  - любой символ кроме переноса строки
#^  - начало строки
#$  - конец строки

#[abc] - любой символ в скобках
#[^abc] - любой символ кроме тех, которые в скобке
#a|b   - a или b
#(ab)   - определяем одним элементом
#\bслово\b - выбираем отдельное слово
#"""
res = re.findall(r'[(al)c]', 'aligoewrrweruuiewr')


""" квантификаторы
regex+ - встречается один или более раз
regex* - встречается ноль или более раз
regex? - встречается ноль или один раз
regex{n} - встречается n раз
regex{n, } - встречается n или более раз
regex{nб m} - встречается от n до m раз
"""

regex = re.compile(r'^.+#')
print(regex.findall('d_r56#'))
print(regex.findall('\nd_r56#12weerrttyu'))
regex = re.compile(r'\S+$')
print(regex.findall('\nd_r56#12weerrttyu'))