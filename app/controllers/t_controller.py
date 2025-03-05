from app.models import Test
from app.schemes import ResponseMessage


def create_test_logic(test, db):
    test_name = db.query(Test).filter(Test.name == test.name).first()
    if test_name:
        return ResponseMessage(message="Test with this name already exists")
    new_test = Test(
        name=test.name,
        max_score=test.max_score
    )
    db.add(new_test)
    db.commit()
    return ResponseMessage(message="Test created successfully")