class Person:
    def __init__(self, name, age): #init конструктор, атрибуты класса Person

        self.name = name #self.name поле класса
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age} years old'


ps1 = Person('Mary', 18)
ps2 = Person('Pit', 19)
ps3 = Person('Dasha', 19)
print(ps1.name)
ps1.name = 'Sasha'
print(ps1.name)


#инкапсуляция - все поля должны быть доступны только через методы класса
# , то есть не должно быть доступа к полям напямую