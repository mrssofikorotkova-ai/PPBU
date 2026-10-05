import tkinter as tk
def sm():
    try:
        e1 = int(ent1.get())
        e2 = int(ent2.get())
        e3 = int(ent3.get())
        rez = e1 + e2 + e3
        r = f'Результат сложения: {rez}'
        msg.config(text= r)
    except ValueError:
        msg.config(text='Ошибка: введите целые числа')

def ymn():
    try:
        e1 = int(ent1.get())
        e2 = int(ent2.get())
        e3 = int(ent3.get())
        rez = e1 * e2 * e3
        r = f'Результат умножения: {rez}'
        msg.config(text=r)
    except ValueError:
        msg.config(text = 'Ошибка: введите целые числа')


root = tk.Tk() #создание окна
root.title("Калькулятор")
root.geometry('420x320')
msg1 = tk.Label(root,text = f'Введите три числа и нажмите на кнопку для вычисления', font = ('Arial',12), justify='center')
msg1.pack(pady = 1) #внешний отступ по вертикали
ent1 = tk.Entry(root,font=('Arial',15), justify='center')
ent1.pack(pady = 1)
ent2 = tk.Entry(root,font=('Arial',15), justify='center')
ent2.pack(pady = 1)
ent3 = tk.Entry(root,font=('Arial',15), justify='center')
ent3.pack(pady = 1)
btn1 = (tk.Button(root, text='Сложить три числа', command = sm, justify='center'))
btn1.pack(pady = 1)
btn2 = (tk.Button(root, text='Умножить три числа', command = ymn, justify='center'))
btn2.pack(pady = 1)
msg = tk.Label(root,text = f'Результат: {chr(8212)}', font = ('Arial',18), justify='center')
msg.pack(pady = 1) #внешний отступ по вертикали

root.mainloop()