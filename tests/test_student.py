from app.models import Student


def test_create_student(client, db_session):
    student_data = {"name": "Test Student", "email": "test@example.com"}

    response = client.post("/students", json=student_data)

    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully"}

    student = db_session.query(Student).filter(Student.email == student_data["email"]).first()
    assert student is not None
    assert student.name == student_data["name"]
    assert student.email == student_data["email"]


def test_create_student_duplicate_email(client, db_session):
    student_data = {"name": "Test Student", "email": "test@example.com"}

    response = client.post("/students", json=student_data)
    assert response.status_code == 201

    duplicate_data = {"name": "Another Student", "email": "test@example.com"}
    response = client.post("/students", json=duplicate_data)

    assert "Student with this email already exists" in response.json()["message"]

    students = db_session.query(Student).filter(Student.email == student_data["email"]).all()
    assert len(students) == 1

