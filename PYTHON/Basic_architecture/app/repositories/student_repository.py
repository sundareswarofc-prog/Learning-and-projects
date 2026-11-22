students = []

def save_student(student):

    student_data = student.model_dump()
    student_data["id"] = len(students) + 1
    students.append(student_data)
    return student_data

def get_all_students():

    return students

def get_student_by_id(id):

    for student in students:
        if student["id"] == id:
            return student

    return None


def update_student(id, name, age):

    student = get_student_by_id(id)

    if student is None:
        return None

    student["name"] = name
    student["age"] = age

    return student

def remove_student(id):
     student=get_student_by_id(id)

     if student is None:
            return None
     
     students.remove(student)
     return {"message":"Student removed successfully"}
