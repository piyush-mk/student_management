from fastapi import FastAPI
from app.routers.students import router as students_router

app = FastAPI(title="Student Management System")

app.include_router(students_router, prefix="/students", tags=["Students"])
