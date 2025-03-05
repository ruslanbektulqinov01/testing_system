from typing import List

from ..controllers.t_controller import create_test_logic
from ..models import Test
from ..schemes import TestScheme, ResponseMessage, TestCreate
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db

test_router = APIRouter()

@test_router.post("/tests", response_model=ResponseMessage,
                  status_code=201,
                  summary="Create a test",
                  description="Create a test with a unique name")
def create_test(test: TestCreate, db: Session = Depends(get_db)):
    return create_test_logic(test, db)

@test_router.get("/tests/{test_id}", response_model=TestScheme)
def get_test(test_id: int, db: Session = Depends(get_db)):
    test = db.query(Test).filter(Test.id == test_id).first()
    return test

@test_router.get("/tests", response_model=List[TestScheme])
def get_tests(db: Session = Depends(get_db)):
    tests = db.query(Test).all()
    return tests

