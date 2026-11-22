from app.services.student_service import (
    create_student_service,
    get_students_service
)

def get_student_service():

    return {
        "create": create_student_service,
        "get_all": get_students_service
    }