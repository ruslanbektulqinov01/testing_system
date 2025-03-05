from app.models import Student


def test_create_student(client, db_session):
    """Test creating a new student via API endpoint"""
    # Test data
    student_data = {"name": "Test Student", "email": "test@example.com"}

    # Make the POST request to create a student
    response = client.post("/students", json=student_data)

    # Check response status code and message
    assert response.status_code == 201
    assert response.json() == {"message": "Student created successfully"}

    # Verify the student was actually created in the database
    student = db_session.query(Student).filter(Student.email == student_data["email"]).first()
    assert student is not None
    assert student.name == student_data["name"]
    assert student.email == student_data["email"]


def test_create_student_duplicate_email(client, db_session):
    """Test creating a student with a duplicate email"""
    # Test data
    student_data = {"name": "Test Student", "email": "test@example.com"}

    # Create the first student
    response = client.post("/students", json=student_data)
    assert response.status_code == 201

    # Try to create another student with the same email
    duplicate_data = {"name": "Another Student", "email": "test@example.com"}
    response = client.post("/students", json=duplicate_data)

    # Check that the request was rejected
    assert "Student with this email already exists" in response.json()["message"]

    # Verify only one student with this email exists in the database
    students = db_session.query(Student).filter(Student.email == student_data["email"]).all()
    assert len(students) == 1

