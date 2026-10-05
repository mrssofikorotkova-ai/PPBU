a = 26
b = 36
c = a > b
print(c)

# if a > b:
#     print('A > B')
#     print('A > B')
# else:
#     if a < b:
#         print('A < B')
#     else:
#         print('A = B')
# print('end')
# if a > b:
#     print('A > B')
#     print('A > B')
# elif a < b:
#     print('A < B')
# else:
#     print('A = B')
# print('end')

# h = float(input('Введите время суток:'))
#
# if h >= 4 and h < 12:
#     print ('morning')
# elif h >= 12 and h < 17:
#     print ('day')
# elif h >= 17 and h < 24:
#     print ('evening')
# elif h >= 0 and h < 4 or h==24:
#     print('night')
# else:
#     print('Время введено не корректно!')

color = input('Цвет светофора:')
match color:
    case 'red': print('stop')
    case 'green': print('go')
    case 'yellow': print('ready')
    case 'yellow'|'blue': print('good')
    case _:print('цвет',color)
    