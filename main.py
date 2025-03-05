from fastapi import FastAPI
from app.routers import t_result_router, student_router, t_router
from app.database import Base, engine
app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(student_router.student_router)
app.include_router(t_router.test_router)
app.include_router(t_result_router.test_result_router)

