print("1. Add Student \n2. View Students\n3. Find Student \n4. Find Highest Mark \n5. Exit")
choice=int(input("Enter the choice: "))
student=dict({})

if choice==1 :
    name=input("Enter the Name: ")
    age=int(input("Enter the Marks: "))

    if not name or not age:
        print("Enter the naem and age properly")
    else:
       student["name"]=name
       student["age"]=age
 
elif choice==2:
    if not student:
        print('no students are added')
    else:
      for x in student:
        pass