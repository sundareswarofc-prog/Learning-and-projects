# def change_case(fn):
#        def inner():
#          return fn().upper()
#        return inner()

# @change_case
# def my_func():
#      return "sarath"
# print(my_func)

# ###### this is called decorators


# def changecase(func):
#   def myinner():
#     return func().upper()
#   return myinner

# @changecase
# def myfunction():
#   return "Hello Sally"

# @changecase
# def otherfunction():
#   return "I am speed!"

# print(myfunction())
# print(otherfunction())

#### we can use single decorators for multiple function

### Multiple decorators ####

# def changecase(func):
#     print("decorating with changecase")
#     def myinner():
#         print("-> enter changecase wrapper")
#         result = func().upper()
#         print("<- leave changecase wrapper")
#         return result
#     return myinner

# def addgreeting(func):
#     print("decorating with addgreeting")
#     def myinner():
#         print("-> enter addgreeting wrapper")
#         result = "Hello " + func() + " Have a good day!"
#         print("<- leave addgreeting wrapper")
#         return result
#     return myinner

    
# @changecase
# @addgreeting
# def myfunction():
#     print("   original function runs")
#     return "Tobias"
    
# print("--- calling ---")
# print(myfunction())

# myfunction = changecase(addgreeting(myfunction))#
