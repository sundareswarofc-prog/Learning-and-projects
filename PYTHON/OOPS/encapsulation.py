# class Encap():
#     def __init__(self,name):
#         self.name=name
  

#     def get_Name(self):
#         return self.name

#     def set_Name(self,name):
#         if(name==" "):
#             print('Not a Name')
#         else:
#             self.name=name

# res=Encap("Sarath")
# print(res.get_Name())
# res.set_Name("ganesh")
# print(res.get_Name())


class Person:
    def __init__(self,age):
        self.__age=age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self,age):
        self.__age=age

p1=Person(21)
print(p1.age)

p1.age=31
print(p1.age)