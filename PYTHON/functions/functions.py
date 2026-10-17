def my_function():
    print("my_func")
my_function()

############ positional arguments ###########

def add(a,b):
    print(a+b)
add(1,2)

############ keyword arguments ###########

def get_names(name,age):
    print(name,age)

get_names(age=21,name="sarath")

###########  positional only arguments (arg,/)##########

def get_age(age,/):
    print(age,"--------postional only arguments-------")

get_age(21)


###########  keyword only arguments (arg,/)##########

def get_keyword(*,name):
    print(name,"-----keyword only argument--------")

get_keyword(name="sarath")


############### combinig both ##########

# def f(a, b, /, c, d, *, e, f):
#     pass

# f(1, 2, 3, d=4, e=5, f=6)   # OK
# f(a=1, b=2, c=3, d=4, e=5, f=6)  # TypeError: a, b are positional-only
# f(1, 2, 3, 4, 5, 6)         # TypeError: e, f must be keywords


##################### *args and **kargs ################

def args(*args):
    print(args)
args(1,3,45)

def kwargs(**args):
    for x in args:
      print(args[x])

kwargs(name="sarath",age=21)

#unpacking arguments

numbers=[1,2,3,4]

def args(a,*b):
    print(a,b)
args(*numbers)