from tkinter import *

def tmr():
    time1 = sd1.get()
    time2 = sd2.get()

    h1 = int(time1[0:2])
    m1 = int(time1[3:5])
    h2 = int(time2[0:2])
    m2 = int(time2[3:5])

    if not (len(time1) == 5 and time1[2] == ':' and 0 <= h1 <= 23 and 0 <= m1 <= 59):
        Tk.messagebox.showerror("Ошибка", "Время нужно в формате ЧЧ:ММ")
    elif not (len(time2) == 5 and time2[2] == ':' and 0 <= h2 <= 23 and 0 <= m2 <= 59):
        Tk.messagebox.showerror("Ошибка", "Время нужно в формате ЧЧ:ММ")
    else:
        x = int()
        y = int()
        now = int(h1 * 60 + m1)
        alarm = int(time2[0:2]) * 60 + int(time2[3:5])
        if now == alarm:
            x = 0
            y = 0
        elif (alarm - now) < 0:
            x = (alarm - now) % 1440 // 60
            y = (alarm - now) % 1440 % 60
        else:
            x = (alarm - now) // 60
            y = (alarm - now) % 60
        lrz.config(text =f'Через {x} ч {y} мин')

root = Tk()
root.title('Напоминалка')
root.geometry('380x240')
frame = Frame(root)
frame.pack(pady=5)

L1 = Label(frame, text = 'Сейчас:')
L1.pack()
sd1= Entry(frame, width = 5)
sd1.config(font="Arial,15", width = 10)
sd1.pack(pady=5)

L2 = Label(frame, text = 'Напомнить в:')
L2.pack(pady=5)
#поле ввода
sd2= Entry(frame, width = 5)
sd2.config(font="Arial,15", width = 10)
sd2.pack(pady=5)

#кнопка запуска
b = Button(frame,text = 'Поставить', command = tmr)
b.config(font = 'Arial,15',width = 10)
b.pack(pady = 5)
#результат
lrz = Label(frame, text ='Напоминание не поставлено')
lrz.pack()

root.mainloop()
