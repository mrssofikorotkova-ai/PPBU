from tkinter import ttk
from io import BytesIO
from PIL import Image, ImageTk
import requests

def load_image(url):
    try:
        resp = requests.get(url)
        resp.raise_for_status() #выдаст ошибку, если ответ на запрос коды не 200 и 300
        image_data = BytesIO(resp.content) #полученные  данные не текст
        #переменная содержит бинарные данные
        img = Image.open(image_data) #получает картинк, переменная содержит картинку
        img.thumbnail((600,400),Image.Resampling.LANCZOS) #оформления уменьшения картинки,
        # а метод Image.Resampling.LANCZOS позволяет не терять качество
        return ImageTk.PhotoImage(img)

    except Exception as er:
        print('Ошибка', er)
        return None

def set_image():
    img = load_image(url)
    if img:
        label.configure(image=img)
        label.image =img

def open_new_window():
    #tag = tag_entry.get()
    url_with_tag = f'https://cataas.com/cat/{tag}' if tag else
                    'https'
    img = load_image(url_with_tag)
    if img:
        new_window = TopLevel(root)
        new_window.title('Картинка с котиком')
        new_window.geometry('620x520')
        label = Label(new_window, image = img)
        label.image = img
        label.pack()

def exit():
    root.destroy() #метод, который обеспечивает выход

ALLOWED_TAGS =['sleep','jump','smile','fight',
               'red','white','black','siamese','bengal']
root = Tk()
root.title('Cats')
root.geometry('600x480')
label = Label(root)
label.pack()
#создание меню
menu_bar = Menu(root) #определеяем где будет меню
root.config(menu = menu_bar)
file_menu = Menu(menu_bar, tearoff=0)#определяем какое меню
menu_bar.add_cascade(label='Файл', menu = file_menu) #добавление пункта менб
file_menu.add_command(label = 'Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = exit)
tag_entry = Entry(root)
tag_entry.pack()

tag_label = Label('Выбери тег')
tag_label.pack()
tag_combobox = ttk.Combobox(values = ALLOWED_TAGS)
tag_combobox.pack()

load_button = Button(text = 'Загрузка по тегу', command = open_new_window)
load_button.pack()

update_btn = Button(text='Следующая', command = set_image)
update_btn.pack(pady = 5)


url = 'https://cataas.com/cat'

img  = load_image(url)
if img: #если картинка есть, мы ее получим
    label.configure(image = img)
    label.image = img

set_image()
root.mainloop()