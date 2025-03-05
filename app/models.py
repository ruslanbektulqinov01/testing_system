from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    test_results = relationship("TestResult", back_populates="student")


class Test(Base):
    __tablename__ = "tests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    max_score = Column(Integer)
    test_results = relationship("TestResult", back_populates="test")


class TestResult(Base):
    __tablename__ = "test_results"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"), index=True)
    test_id = Column(Integer, ForeignKey("tests.id"), index=True)
    score = Column(Integer)

    student = relationship("Student", back_populates="test_results")
    test = relationship("Test", back_populates="test_results")

