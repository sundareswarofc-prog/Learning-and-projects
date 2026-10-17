import psycopg2

try:
    conn=psycopg2.connect(
        user="postgres",
        password="12345",
        host="localhost",
        database="python_learning"
    )
    print("database connected succefuly")
except:
    print(f"failed ")

def add_user():
    name=str(input("Enter the student name : "))
    age=int(input("Enter the age : "))
    course=input("Enter the course : ")

    with conn.cursor() as cur:
        cur.execute(
               """
            INSERT INTO students (name, age, course)
            VALUES (%s, %s, %s)
            """,
            (name, age, course)
        )
    conn.commit()
    print("created succesfully")

def fetch_all():
    with conn.cursor() as cur:
        cur.execute(
            "SELECT id, name, age, course FROM students ORDER BY id"
        )
        student=cur.fetchall()
        print(student)



while True:
    choose=input("Enter the choice:")

    if choose == "1":
      add_user()
    elif choose == "2":
        fetch_all()
    else:
        print ("Invalid choice")