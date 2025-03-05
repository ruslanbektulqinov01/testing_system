from app.models import Student, Test, TestResult
from app.schemes import ResponseMessage


def create_test_result_logic(test_result, db):
    student_id = db.query(Student).filter(Student.id == test_result.student_id).first()
    if not student_id:
        return ResponseMessage(message="Student does not exist")
    test_id = db.query(Test).filter(Test.id == test_result.test_id).first()
    if not test_id:
        return ResponseMessage(message="Test does not exist")
    if test_result.score > test_id.max_score:
        return ResponseMessage(message="Score is greater than the maximum score")
    new_test_result = TestResult(
        student_id=test_result.student_id,
        test_id=test_result.test_id,
        score=test_result.score
    )
    db.add(new_test_result)
    db.commit()
    return ResponseMessage(message="Test result created successfully")

def get_student_results_logic(student_id, db):
    results = db.query(TestResult).filter(TestResult.student_id == student_id).all()
    return results

def get_test_results_logic(test_id, db):
    results = db.query(TestResult).filter(TestResult.test_id == test_id).all()
    return results

def get_test_average_logic(test_id, db):
    results = db.query(TestResult).filter(TestResult.test_id == test_id).all()
    total_score = 0
    for result in results:
        total_score += result.score
    average_score = total_score / len(results)
    return {"test_id": test_id, "average_score": average_score}

def get_test_highest_logic(test_id, db):
    results = db.query(TestResult).filter(TestResult.test_id == test_id).all()
    highest_score = 0
    for result in results:
        if result.score > highest_score:
            highest_score = result.score
    return {"test_id": test_id, "highest_score": highest_score}

