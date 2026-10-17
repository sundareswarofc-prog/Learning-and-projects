def my_func():
    x=1
    def inner():
        print(x)
    inner()
my_func()

########### the above code is similar to closure ##################

############ Gobal Keyword ###############

def my_func():
    global x
    x=2
my_func()   
print(x)


############ nonlocal ##################

def my_func():
    x=2
    print(x) ### here this will print 2
    def inner():
        nonlocal x ## by using this nonlocal keyword we can change the outer function variable 
        x=5
    inner()
    print(x) ## this can print 5

my_func()


