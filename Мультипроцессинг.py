import multiprocessing
import time
import random #библиотека случайных чисел

def producer(queue, n_items): #функция производителя, которая генерирует числа и отправляет их в очередь,
# далее отправляя в другую функцию, которая будет принимать
    for i in range(n_items):
        item = random.randint(1, 100) # случайные числа от 1 до 100
        queue.put(item) #отправляем в очередь в другую функцию (consumer)
        print(f'Производитель создал: {item}')
        time.sleep(random.uniform(.1, .5)) # .1 и .5 соответствует 0.1 и 0.5
    queue.put(None) # элементы закончены кладем None

def consumer(queue): # функция потребителя
    while True:
        item = queue.get() # методом get забираем элемент из очереди
        if item is None: # если пришел  элемент None то останавливается функция
            break
        result = item ** 2 #возмем элемент и возведем в квадрат
        print(f'Получен -> {item}, изготовлен -> {result}')
        time.sleep(random.uniform(.2,.6))
    print('Пользователь работу закончил!')

if __name__ == '__main__':
    queue = multiprocessing.Queue() #строим очередь мультипроцессинга
    p_producer = multiprocessing.Process(target = producer, args = (queue, 10))
    p_consumer = multiprocessing.Process(target = consumer, args = (queue,))
    p_producer.start()
    p_consumer.start()
    p_producer.join()
    p_consumer.join()
    print('Главный процесс завершен!')