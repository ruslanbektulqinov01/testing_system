from app.models import Test


def test_create_test(client, db_session):
    test_data = {"name": "Test Test", "max_score": 100}

    response = client.post("/tests", json=test_data)

    assert response.status_code == 201
    assert response.json() == {"message": "Test created successfully"}

    test = db_session.query(Test).filter(Test.name == test_data["name"]).first()
    assert test is not None
    assert test.name == test_data["name"]
    assert test.max_score == test_data["max_score"]

def test_create_test_duplicate_name(client, db_session):
    test_data = {"name": "Test Test", "max_score": 100}

    response = client.post("/tests", json=test_data)
    assert response.status_code == 201

    duplicate_data = {"name": "Test Test", "max_score": 100}
    response = client.post("/tests", json=duplicate_data)

    assert "Test with this name already exists" in response.json()["message"]

    tests = db_session.query(Test).filter(Test.name == test_data["name"]).all()
    assert len(tests) == 1
