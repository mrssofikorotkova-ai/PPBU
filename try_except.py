try:
    n = int(input('> '))
    if n == 200:
        raise TypeError ('Число 100 запрещно')
    print(n)

except (ValueError, ZeroDivisionError):
    print('Please enter a number')
except NameError:
    print('Please enter a name')
except Exception as err: #остальные другие ошибки
    print(err)
else: # ветка срабатывает, когда нет ошибки
    print('Когда нет ошибки')
finally:
    print('ВыполнЯется в любом случае')