# In Python, dunder methods are special methods whose names begin and end with double underscores (__).

# __init__()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Arun", 25)

# print(p1.name)
# print(p1.age)







#__str__()

# class Person:
#     def __init__(self,name):
#         self.name=name
#     def __str__(self):
#         return f"{self.name}" #__str__ methods must return a string

# p=Person("Sarath")
# print(p)






# __repr__()

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def __repr__(self): 
#         return f"Person('{self.name}', {self.age})" #It shows the developer friendly representation (Person('arun',25))

# p1 = Person("Arun", 25)

# print(p1)




# __len__()

class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

team = Team(["Arun", "Bala", "Kumar"])

print(len(team))



#__add__()

class Add:
    def __init__(self,age):
        self.age=age
    def __add__(self,other):
        return self.age + other.age
    # def __str__(self):
    #     return str(self.age)

p1=Add(21)
p2=Add(21)
# p3=Add(2)


print(p1+p2)



#__eq__()

class Person:
    def __init__(self, age):
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

p1 = Person(25)
p2 = Person(25)
p3 = Person(30)

print(p1 == p2)
print(p1 == p3)



# __lt__()

class Person:
    def __init__(self, age):
        # self.name = name
        self.age = age

    def __lt__(self, other):
        return self.age < other.age

p1 = Person("Arun", 25)
p2 = Person("Bala", 20)

print(p1 < p2)