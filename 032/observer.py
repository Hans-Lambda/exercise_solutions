from abc import ABC, abstractmethod


class Observable(ABC):

    @abstractmethod
    def attach(self, observer):
        pass

    @abstractmethod
    def detach(self, observer):
        pass


class Observer(ABC):

    @abstractmethod
    def notify(self):
        pass


class SmokeSensor(Observable):

    def __init__(self):
        self.list_of_observers = []

    def attach(self, observer):
        self.list_of_observers.append(observer)

    def detach(self, observer):
        self.list_of_observers.remove(observer)

    def smoke_detected(self):
        for observer in self.list_of_observers:
            observer.notify()


class Firefighter(Observer):

    def notify(self):
        print("This is the firefighters: Prepare yourself! Something is burning!")


class Police(Observer):

    def notify(self):
        print("This is the police: Check for who started the fire!")


class Victims(Observer):

    def notify(self):
        print("This is the victim: PANIC!!")


if __name__ == '__main__':

    smoke_sensor = SmokeSensor()
    police_dep = Police()
    smoke_sensor.attach(police_dep)

    firefighters = Firefighter()
    smoke_sensor.attach(firefighters)

    victims = list()
    for i in range(3):
        victim = Victims()
        smoke_sensor.attach(victim)

    smoke_sensor.smoke_detected()
    smoke_sensor.smoke_detected()
