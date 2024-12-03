from fastapi import FastAPI
from app.routers.students import router as students_router

app = FastAPI(title="Student Management System")

app.include_router(students_router, prefix="/students", tags=["Students"])
@app.get("/")
def read_root():
    return {"message": "Welcome to the Student Management System API"}
