def outer(n):
    return lambda x: x*n
x=outer(3)
print(x(2))


################ built in funcion ################
numbers = [1, 2, 3, 4, 5]
#map
y=list(map(lambda x:x*2,numbers))
print(y)

#filter
z=list(map(lambda x:x%2==0,numbers))
print(z)

#sorted
students = [("Emil", 25), ("Tobias", 22), ("Linus", 28)]
sorted_students = sorted(students, key=lambda x: x[1])
print(sorted_students)