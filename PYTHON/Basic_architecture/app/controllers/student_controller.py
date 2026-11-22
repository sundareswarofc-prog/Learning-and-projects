from app.services.student_service import (create_student_service,get_students_service,update_student_service,delete_student)

def create_student(student):
    return create_student_service(student)

def get_students_controller():
    return get_students_service()
    

def update_student_controller(id, name, age):

    return update_student_service(id, name, age)

def remove_student(id):

    return delete_student(id)