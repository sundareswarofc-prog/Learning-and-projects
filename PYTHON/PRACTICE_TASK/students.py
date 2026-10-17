students = [
    {"name": "Arun", "age": 21, "marks": 85},
    {"name": "Bala", "age": 22, "marks": 72},
    {"name": "Kumar", "age": 20, "marks": 91},
    {"name": "Ravi", "age": 23, "marks": 64},
    {"name": "Siva", "age": 21, "marks": 78}
]

avg=0
highest=students[0]["marks"]
passed_students=0
failed=0

for x in students:
    print(f"{x["name"]}    | Age:{x["age"]} | marks:{x["marks"]} | {"passed" if x["marks"]>=40 else "filed" }")

    if(x["marks"]>highest):
        highest=x["marks"]
    if(x["marks"]>=40):
        passed_students+=1
    else:
        failed=failed+1
    
    
    avg+=x["marks"]
print("Average--------------",avg/len(students))
print("highest marks...",highest)
print("Passed students--------------",passed_students)
print("failed students--------------",failed)

