###### Hide the unnecessary details and show only the essential features of an object.##########

# class Animal:
#     def make_sound(self):
#         self.dog()
#         self.cat()

#     def cat(self):
#         print("Meow")

#     def dog(self):
#         print("Barks")

# animal=Animal()
# animal.make_sound()

############# Python having some abstraction base classes #################

from abc import ABC,abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print("drive")
    def color(self,color):
        print(color)

class Ship(Vehicle):
    def move(self):
        print("sail!")

car=Car()
car.move()
car.color("Red")
ship=Ship()
ship.move()
