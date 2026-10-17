class Vehicle:
    def __init__(self,name,brand):
        self.name=name
        self.brand=brand
    def move(self):
        print("drive")

class Car(Vehicle):
    pass

class Ship(Vehicle):
    def __init__(self,name,brand):
        Vehicle.__init__(self,name,brand)
    def move(self):
        print("sail!")

class Plane(Vehicle):
    def move(self):
        print("Air!")

v1=Car("Thar","rocks")
v2=Ship("titanic","V2")
v3=Plane("Kingfisher", "V2")

print(v1.name)
v1.move()
v2.move()
