from pydantic import BaseModel, Field

class StudentScheme(BaseModel):
    id: int = Field(..., description="Unique identifier for the student")
    name: str = Field(..., min_length=2, max_length=50, description="Student's full name")
    email: str = Field(..., description="Student's email address")

    class Config:
        from_attributes = True

class StudentCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=50, description="Student's full name")
    email: str = Field(..., description="Student's email address")

    class Config:
        from_attributes = True

class TestScheme(BaseModel):
    id: int = Field(..., description="Unique identifier for the test")
    name: str = Field(..., min_length=2, max_length=100, description="Name of the test")
    max_score: int = Field(..., description="Maximum possible score")

    class Config:
        from_attributes = True


class TestCreate(BaseModel):
    name: str = Field(..., min_length=2, max_length=100, description="Name of the test")
    max_score: int = Field(..., description="Maximum possible score")

    class Config:
        from_attributes = True

class TestResultScheme(BaseModel):
    student_id: int = Field(..., description="ID of the student taking the test")
    test_id: int = Field(..., description="ID of the test taken")
    score: int = Field(..., description="Score obtained in the test")

    class Config:
        from_attributes = True


class ResponseMessage(BaseModel):
    message: str

