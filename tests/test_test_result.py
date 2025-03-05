from app.models import Test, TestResult, Student

def test_create_t_result(client, db_session):
    test_data = {"name": "Test Test", "max_score": 100}
    student_data = {"name": "Test Student", "email": "test@gmail.com"}
    test_result_data = {"student_id": 1, "test_id": 1, "score": 90}

    response = client.post("/tests", json=test_data)
    assert response.status_code == 201
    response = client.post("/students", json=student_data)
    assert response.status_code == 201
    response = client.post("/results", json=test_result_data)
    assert response.status_code == 201
    assert response.json() == {"message": "Test result created successfully"}
    test_result = db_session.query(TestResult).filter(TestResult.student_id == test_result_data["student_id"]).first()
    assert test_result is not None
    assert test_result.student_id == test_result_data["student_id"]
    assert test_result.test_id == test_result_data["test_id"]



