print('Задание 1 от 09.09.2026')
print('Пример 1.')
i = 3
print(i)
while i<40:
    i += 10
    print(i)

print()
print('Пример 2.')
print('Введите пароль:')
p = input()
while len(p)<8:
    print('Длина пароля менее 8 символов!!')
    p = input()
print('Пароль принят!')
print()

print('Пример 3.')
print('Введите параметры автомобиля по шаблону\nLADA 2010г 205000км 450000руб')
car = input()
mod = car[:car.index(' ')]
y = car[car.index(' ')+1:]
km = y
y = y[:y.index(' ')]
km = km[km.index(' ')+1:]
rub = km
km = km[:km.index(' ')]
rub = rub[rub.index(' ')+1:]
print(f'Продается автомобиль \nМарка: {mod}\nГод выпуска: {y}\nПробег: {km}\nЦена: {rub}')

