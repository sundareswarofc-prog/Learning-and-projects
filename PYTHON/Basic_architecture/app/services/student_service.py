from app.repositories.student_repository import (get_all_students,save_student,update_student,remove_student)


def create_student_service(student):

    if student.age < 18:
        return {"error": "Student must be 18 or older"}


    return save_student(student)

def get_students_service():

    return get_all_students()

def update_student_service(id, name, age):

    if age < 18:
        return {"error": "Student must be 18 or older"}

    student = update_student(id, name, age)

    if student is None:
        return {"error": "Student not found"}

    return student

def delete_student(id):

      student = remove_student(id)
     
      if student is None:
         return {"error":"Student not found"}
      return student


    