import math
from tkinter import *

def validate_entry(value):
    #допустим пришло значение 12а
    entry_text = value.get().strip()
    #идет по символьная проверка, 12 есть записывается в corrected_text,
    # 'а' нет в перечне не записывается
    corrected_text = ''.join((b for b  in entry_text if b in '0123456789'))
    #сравнение 12а и 12
    if entry_text != corrected_text:
        value.delete(0, END)
        value.insert(0, corrected_text)

def validate_oper(values)

def add(n1,d1,n2,d2):
    n = n1 * d2 + n2 * d1
    d = d1 * d2
    return n, d





num3 = Label(frame, width = 2, bg = 'light gray')
num3.config(font = ('Arial', 15), justify = 'center')
num3.grid(row = 0, column = 5)
Label(frame, text = chr)

num1.bind('KeyRelease', lambda)
root.mainloop()