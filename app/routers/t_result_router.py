from typing import List

from ..controllers.t_result_controller import create_test_result_logic, get_student_results_logic, \
    get_test_results_logic, get_test_average_logic, get_test_highest_logic
from ..models import TestResult, Student, Test
from ..schemes import TestResultScheme, ResponseMessage
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db

test_result_router = APIRouter()

@test_result_router.post("/results",
                         response_model=ResponseMessage,
                         status_code=201,
                         summary="Create a test result",
                         description="Create a test result for a student")
def create_test_result(test_result: TestResultScheme, db: Session = Depends(get_db)):
    return create_test_result_logic(test_result, db)

@test_result_router.get("/results/student/{student_id}", response_model=List[TestResultScheme])
def get_student_results(student_id: int, db: Session = Depends(get_db)):
    return get_student_results_logic(student_id, db)

@test_result_router.get("/results/test/{test_id}", response_model=List[TestResultScheme])
def get_test_results(test_id: int, db: Session = Depends(get_db)):
    return get_test_results_logic(test_id, db)

@test_result_router.get("/results/test/{test_id}/average")
def get_test_average(test_id: int, db: Session = Depends(get_db)):
    return get_test_average_logic(test_id, db)

@test_result_router.get("/results/test/{test_id}/highest")
def get_test_highest(test_id: int, db: Session = Depends(get_db)):
    return get_test_highest_logic(test_id, db)


