from tkinter import *
from tkinter import messagebox as mb
from tkinter import ttk
import requests
import json

from bottle import response


def update_base_label(event):
    code = base_combobox.get()
    name = currencies[code]
    base_label.config(text=name)

def update_sec_base_label(event):
    code = sec_base_combobox.get()
    name = currencies[code]
    sec_base_label.config(text=name)

def update_currency_label(event):
    code = target_combobox.get()
    name = currencies[code]
    target_label.config(text=name)

def exchange():
    base_code = base_combobox.get().strip()
    sec_base_code = sec_base_combobox.get().strip()
    target_code = target_combobox.get().strip()
    if target_code and base_code and sec_base_code:
        try:
            response = requests.get(f'https://open.er-api.com/v6/latest/{base_code}')
            response.raise_for_status()
            response1 = requests.get(f'https://open.er-api.com/v6/latest/{sec_base_code}')
            response1.raise_for_status()
            data = response.json()
            data1 = response1.json()
            if target_code in data['rates'] and target_code in data1['rates']:
                exchange_rate = data['rates'][target_code]
                exchange_rate1 = data1['rates'][target_code]
                base = currencies[base_code]
                sec_base = currencies[sec_base_code]
                target = currencies[target_code]
                mb.showinfo('Курс обмена',
                            f'Курс: \n {exchange_rate:.1f} {target} за 1 {base}'
                            f'\n {exchange_rate1:.1f} {target} за 1 {sec_base}')
            else:
                mb.showerror('Ошибка',
                            f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)

    else:
        mb.showwarning('Внимание', 'Введите код валюты')



currencies = {
    'EUR': 'Евро',
    'USD': 'Доллар США',
    'JPY': 'Японская йена',
    'GBP': 'Фунт стерлингов',
    'AUD': 'Австралийский доллар',
    'CAD': 'Канадский доллар',
    'CHF': 'Швейцарский франк',
    'CNY': 'Китайский юань',
    'RUB': 'Российский рубль',
    'KZT': 'Казахстанский тенге',
    'UZS': 'Узбекский сум'
}

root = Tk()
root.title('Курс обмена валют')
root.geometry('360x250')

Label(root, text='Базовая валюта').pack()
base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
base_combobox.pack(pady=3, padx=10)
base_combobox.bind('<<ComboboxSelected>>', update_base_label)
base_label = ttk.Label()
base_label.pack()

Label(root, text='Вторая базовая валюта').pack()
sec_base_combobox = ttk.Combobox(root, values=list(currencies.keys()))
sec_base_combobox.pack(pady=3, padx=10)
sec_base_combobox.bind('<<ComboboxSelected>>', update_sec_base_label)
sec_base_label = ttk.Label()
sec_base_label.pack()

Label(root, text='Целевая валюта' ).pack(padx=10)
target_combobox = ttk.Combobox(root, values=list(currencies.keys()))
target_combobox.pack(pady=3, padx=10)
target_combobox.bind('<<ComboboxSelected>>', update_currency_label)

target_label = ttk.Label()
target_label.pack()
Button(text='Получить курс обмена к доллару',
       command=exchange).pack(pady=10, padx=10)
root.mainloop()