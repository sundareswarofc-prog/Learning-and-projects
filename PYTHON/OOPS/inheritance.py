# class Parent_Class:
#     def __init__(self,name):
#         self.name=name

# class Child_Class(Parent_Class):
#     pass

# p1=Child_Class("sarath")
# print(p1.name)

###################################

class Parent_Class:
    def __init__(self,nickname):
        self.nickname=nickname

class Child_Class(Parent_Class):
    def __init__(self,name,age,nickname):
        super().__init__(nickname)
        self.age=age
        self.name=name
        # Parent_Class.__init__(self,name)
    def greet(self):
        return "test"


p1=Child_Class("sarath",21,"Gokul")
print(p1.nickname)
print(p1.age)

print(p1.greet())


#################################

##############SUPER###################

# class Parent_Class:
#     def __init__(self,name):
#         self.name=name

# class Child_Class(Parent_Class):
#     def __init__(self,name):
#         super().__init__(name)
#     def greet():
#         print("test")


# p1=Child_Class("sarath")
# print(p1.name)
# print(p1.greet())

############ we can pass parent constructor nickname from the child class using super contructor ######################
class Parent:
    def __init__(self, nickname):
        self.nickname = nickname

class Child(Parent):
    def __init__(self, name, age, nickname):
        super().__init__(nickname)
        self.name = name
        self.age = age

p1 = Child("Sarath", 21, "Sam")

print(p1.name)      # Sarath
print(p1.age)       # 21
print(p1.nickname)  # Sam