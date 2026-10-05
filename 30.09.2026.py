from math import *
from tkinter import *

def add(n1, n2, n3):
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    n = n1+n2+n3
    num4.config(text=n)
    return n

def mult(n1, n2, n3):
    n1 = int(num1.get())
    n2 = int(num2.get())
    n3 = int(num3.get())
    n = n1 * n2 * n3
    num4.config(text = n)
    return n


root = Tk()
root.title("Введите три числа и нажмите на кнопку для вычисления суммы")
root.geometry("500x300+600+150")

frame = Frame(root)
frame.pack(pady=10)

num1 = Entry(frame, width=15)
num1.config(font=("Arial", 15), justify="center")
num1.grid(row=0, column=0)
num2 = Entry(frame, width=15)
num2.config(font=("Arial", 15), justify="center")
num2.grid(row=1, column=0)
num3 = Entry(frame, width=15)
num3.config(font=("Arial", 15), justify="center")
num3.grid(row=2, column=0)

btn = Button(frame, text='Сложить три числа', command=add(n))
btn.config(font=("Arial", 15), justify="center", width=20)
btn.grid(row=3, column=0)

btn1 = Button(frame, text='Умножить три числа', command=mult(n))
btn1.config(font=("Arial", 15), justify="center", width=20)
btn1.grid(row=6, column=0)

num4 = Label(frame, width=15, bg="light gray")
num4.config(font=("Arial", 15), justify="center", text = n))
num4.grid(row=7, column=0)

root.mainloop()

