from turtle import *
#Нарисуйте три разных круга, используя разные цвета и радиусы, используя модуль turtle.
# Для каждого круга используйте begin_fill(), color(), circle() и end_fill().
# Сохраните файл с проектом на компьютер.

for i in range(3):
    begin_fill()
    color('70,181,75')
    circle (50)
    end_fill()
    penup()
    forward(50)
    pendown()


