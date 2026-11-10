from abc import ABC, abstractmethod

class Gadget(ABC):
    @abstractmethod
    def talk(selfself):
        pass

    @abstractmethod
    def inet(self):
        pass

    @abstractmethod
    classVideo(selfself):
        pass

classes = (Talk, Inet, Video)

class Smartphone(Talk, Inet, Video): #множественное  наследование
#class Smartphone (*classes):  если необходимо несколько классов использовать, то можно через кортеж обозначив его ранее
    def talk(self):
        pass

    def inet(self):
        print('inet')

    def video(self):
        print('video')
class Telephone(Talk):
    def talk(selfself):
        print('talk')

sm = Smartphone()
