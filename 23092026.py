from tkinter import *
root = Tk()
root.title('Старт')
root.geometry("300x300+400+200")
prompt = Label(text = 'Введите значение')
prompt.pack()
num = Entry(width=5, font = 'arial 12')
num.pack()
root.mainloop()

result = Label(text=' ')
result.pack(pady =10)