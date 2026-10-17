class My_Class:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=My_Class("Arun", 27)
print(p1.name)

class My_Class2:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def my_greet(self):
        return "sarath"
    def print_greet(self):
        print(f"{self.my_greet()},Welcome")

p2=My_Class2("sarath",21)
p2.print_greet()


######################### class properties and object properties #################

class Test_Class:
    species="human"
    def __init__(self,name):
        self.name=name
print(Test_Class.species) ### we can access it directly (or)

p3=Test_Class("test")
print(p3.name,p3.species)