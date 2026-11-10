import socket

#1 параметры подключения
ip = '127.0.0.1'
port = 9001 #первые 1024 портов трогать нельзя, от 8000 можно брать порты
end_point = (ip, port) #точка подключения

# сокет сервера
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#IP имеет вид "127.0.0.1"
#sock_stream  -  будем работать по протоколу TSP
server.bind(end_point)

server.listen(10) #обязательно!!!  

#режим ожидания запросов
print(f'Сервер запущен на IP-{ip}:{port}')
print('Ожидание запросов на соединение')
connection, client_address = server.accept()
#server.accept - ожидает запрос, формирует коннект и адрес того, кто обратился

#обмен данных с клиентом
try:
    print(f'Установлено соединение с клиентом: {client_address}')
    while True:
        #принимаем сообщение
        client_message = connection.recv(1024).decode(encoding='utf-8')
        if not client_message or client_message == 'stop_server':
            break
        print(f'Сообщение от клиента: [{client_message}]')
        #отправка сообщения
        server_message =  input('Ответ сервера:')
        connection.send(server_message.encode(encoding='utf-8'))
        print('Сообщение отправлено!')

except BaseException as e:
    print(e)
finally: #нужен для того, чтобы в случае ошибки закрыть все соединения
    connection.close()
    print('Сервер остановлен')