
class Human:
    def __init__(self, name, *entities, magic = 0):
        #* entities - записываем неопредленное количество объектов  в кортеж entities, то что не попало в другие переменные
        self.name = name
        self.magic = magic
        self.entities = list(entities) # преобразуем кортеж entities в список (list)

    def change_name(self, name):
        self.name += ' ' + name

    def __add__(self, other):
        self.magic += len(other)//4
        self.entities.append(other)
        return self

    def __call__(self, num):
        return self.entities[:num]

    def __eq__(self, other):
        return (self.magic ==  other.magic
                and len(self.entities) == len(other.entities)
                and self.name == other.name)

    def __gt__(selfself, othen): #метод больше чем
        if self.magic > other.magic:
            return True
        elif (self.magic == other.magic
            and len(self.entities)>len(other.entities)):
            return True
        elif (self.magic == other.magic
            and  len(self.entities) == len(other.entities)):
            return True
        return False

    def __le__ (self, other): #меньше или равно
        if self.magic < other.magic:
            return True
        elif (self.magic == other.magic
            and len(self.entities) < len(other.entities)):
            return True
        elif (self.magic == other.magic
            and  len(self.entities) == len(other.entities)
            and self.name < other.name):
            return True
        return self == other
    
    def __ne__(self, other):
        return (self.magic !=  other.magic
                and len(self.entities) != len(other.entities)
                and self.name != other.name)

    def __sub__(self, other): #метод вычитания
        name = self.name[:3].capitalize()+other.name[-3:].capitalize #срез первые три буквы заглавные и срез последние три буквы заглавные
        entities = list(set(self.entities) - set(other.entities))
        return Human(name, *entities, )


    def __str__(self):
        return f'Человек по имени {self.name} ({', '.join(self.entities)}, {self.magic})'

hm = Human('Illmarrannen', 'Forgiving', 'Forgivin',magic = 2)
hm1 = Human(, magic = 10)
hm.change_name('Rual')
id_hm = id(hm)
hm +='Skyman'
print(hm, hm(2), sep ='\n')
print(id_hm == id(hm))
hm2 = hm - hm1
print(hm2)
print(hm2 >hm1, hm2<= hm, hm2 != hm)
