from tkinter  import *
from tkinter import ttk
from tkinter import messagebox as mb
import requests
from datetime import date, timedelta
from tkcalendar import DateEntry # календарь

#функция обновления названия (текста) криптовалюты
def update_coin_label(*args):
    code = coin_var.get().strip()
    coin_label.config(text = coin_currencies.get(code,''))
    lblrez.config(text=txt0)

#функция обновления названия (текста) валюты
def update_target_label(*args):
    code = target_combobox.get()
    target_label.config(text=currencies.get(code,''))
    lblrez.config(text=txt0)

#функция для расчета курса
def exchange():
    coin_code = coin_combobox.get().strip()
    target_code = target_combobox.get().strip()
    dtt = cal.get_date()
    if coin_code and target_code:
        #если в переменной не пустая строка, то будет выполняться следующее условие
        #если нет, то на шаг else
        try:
            if dtt == date.today(): #если дата = сегодня
                response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={coin_code},ethereum,solana&vs_currencies={target_code}")
                response.raise_for_status()
                data = response.json()
                data = data[coin_code]
            else:
                response = requests.get(f'https://api.coingecko.com/api/v3/coins/{coin_code}/history?date={dtt.strftime('%d-%m-%Y')}')
                response.raise_for_status()
                data = response.json().get("market_data") #json библиотеки response
                data = data['current_price']
            if target_code in data:
                exchange_rate = data[target_code]
                coin = coin_currencies[coin_code]
                target = currencies[target_code]
                rez = f'Курс на дату {dtt.strftime('%d.%m.%Y')}: \n\n За 1 {coin}\n\n{exchange_rate:.1f} {target}  '
                lblrez.config(
                text=f' Курс: \n За 1 {coin}\n{exchange_rate:.1f} {target}  ')
                mb.showinfo('Курс обмена на дату',rez)
            else:
                mb.showerror('Ошибка',f'Валюта {target_code} не найдена')
        except Exception as er:
            mb.showerror('Ошибка', er)
    else:
        mb.showwarning('Внимание', 'Введите код валюты')


#создание справочника кодов криптовалют
coin_currencies = {
    'bitcoin': 'Bitcoin',
    'ethereum': 'Ethereum',
    'tether': 'Tether',
    'the-open-network': 'TON'
}
#создание справочника кодов валют
currencies = {
    'rub': 'Рубль',
    'usd': 'Доллар США',
    'jpy': 'Японская йена',
    'chf': 'Швейцарский франк',
    'cny': 'Китайский юань',
    'cad': 'Канадский доллар'
}

root = Tk()
root.title('Курс обмена криптовалют к валюте')
root.geometry('600x250')

#создаем фрейм для размещения в нем элементов выбора
frame = ttk.Frame(root, padding = 20)
frame.pack()

ttk.Label(frame, text = 'Дата').grid(row = 0, column = 0)
cal = DateEntry(
    frame,
    date_pattern = 'dd.mm.yyyy',
    maxdate = date.today(),
    mindate = date.today() - timedelta(days=364)
)
cal.grid(row = 1, column = 0)

Label(frame, text = 'Криптовалюта').grid( row = 0, column = 1, padx = 5, pady =0)
#создаем переменную по умолчанию пустая строка
coin_var = StringVar()
#textvariable нужен для привязывания значения в комбобоксе к переменной coin_var
coin_combobox = ttk.Combobox(frame, textvariable=coin_var, values = list(coin_currencies.keys()))
coin_combobox.grid(row = 1, column = 1, padx = 5, pady =0)
#при изменение значения в поле coin_combobox будет вызываться функция
coin_var.trace_add('write', update_coin_label)

coin_label = ttk.Label(frame)
coin_label.grid(row = 2, column = 1)

Label(frame, text = 'Целевая валюта').grid(row = 0, column = 2, padx = 5, pady =0)
#создаем переменную по умолчанию пустая строка
target_var = StringVar()
target_combobox = ttk.Combobox(frame, textvariable=target_var, values = list(currencies.keys()))
target_combobox.grid(row = 1,  column = 2, padx = 5, pady =0)
#при изменение значения в поле target_combobox будет вызываться функция
target_var.trace_add('write', update_target_label)
target_label = ttk.Label(frame)
target_label.grid(row = 2, column = 2, padx = 5, pady =0)

#создаем фрейм для размещения в нем кнопок
framebt = ttk.Frame(root, padding = 20)
framebt.pack()

btn1= Button(framebt, text = 'Получить курс обмена к валюте',
       command = exchange)
btn1.grid(row = 0, column = 0, padx = 5, pady =0)

btn2 = Button(framebt, text = 'Записать результат в файл')
btn2.grid(row = 0, column = 1, padx = 5, pady =0)

btn3 = Button(framebt, text = 'Отправить результат на почту')
btn3.grid(row = 0, column = 2, padx = 5, pady =0)

txt0 = 'Здесь отобразится результат действия'
lblrez = Label(root, text = txt0)
lblrez.pack()
root.mainloop()