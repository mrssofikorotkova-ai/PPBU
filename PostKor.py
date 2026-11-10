import smtplib
import mimetypes
from email.message import EmailMessage

password = 'bablkrkqozlyxkjp'
receipt_email = 'mikekorotkov@yandex.ru' #кому отправляем
sender_email = 'mrs.korelena@yandex.ru' #от кого отправляем
subject = 'Проверка связи'
body = 'Я отправила тебе сообщение из Python. Люблю))'

msg = EmailMessage()
#
msg.set_content(body)
msg['Subject'] = subject #заголовок сообщения
msg['From'] = sender_email #от кого сообщение
msg['To'] = receipt_email #кому сообщение

#---вложение




server = None
try:
    server = smtplib.SMTP_SSL('smtp.yandex.ru', 465)
    server.login(sender_email, password)
    server.send_message(msg)
    print('Письмо отправлено')
except Exception as e:
    print(f'Ошибка{e}')

finally:
