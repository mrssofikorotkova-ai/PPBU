from tkinter import *

def tmr():
    try:
        s = int(sd.get())
    except ValueError:
        lrz.config(text = "Это не число")
    else:
        if 1 <= s <= 120:
            lrz.config(text = f'Таймер: {s} мин')
        else:
            lrz.config(text= 'Нужно от 1 до 120 минут')

root = Tk()
root.title('Таймер корма')
root.geometry('360x200')
frame = Frame(root)
frame.pack(pady=5)
L = Label(frame, text = 'Сколько минут варить?')
L.pack()

#поле ввода
sd= Entry(frame, width = 5)
sd.config(font="Arial,15", width = 10)
sd.pack(pady=5)

#кнопка запуска
b = Button(frame,text = 'Запустить', command = tmr)
b.config(font = 'Arial,15',width = 10)
b.pack(pady = 5)
#результат
lrz = Label(frame, text ='Таймер не запущен')
lrz.pack()

root.mainloop()

