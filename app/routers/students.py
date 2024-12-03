from fastapi import APIRouter, HTTPException, Query
from app.database import students_collection
from app.schemas import StudentCreate, StudentUpdate, StudentResponse
from bson import ObjectId
from typing import List

router = APIRouter()

# Helper function to convert MongoDB document to Python dict
def serialize_student(student):
    student["id"] = str(student["_id"])
    del student["_id"]
    return student

@router.post("/", response_model=dict, status_code=201)
async def create_student(student: StudentCreate):
    student_dict = student.dict()
    result = await students_collection.insert_one(student_dict)
    return {"id": str(result.inserted_id)}

@router.get("/", response_model=List[StudentResponse])
async def list_students(country: str = Query(None), age: int = Query(None)):
    query = {}
    if country:
        query["address.country"] = country
    if age:
        query["age"] = {"$gte": age}
    students = await students_collection.find(query).to_list(100)
    return [serialize_student(student) for student in students]

@router.get("/{id}", response_model=StudentResponse)
async def get_student(id: str):
    student = await students_collection.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return serialize_student(student)

@router.patch("/{id}", status_code=204)
async def update_student(id: str, updates: StudentUpdate):
    updates_dict = updates.dict(exclude_unset=True)
    result = await students_collection.update_one({"_id": ObjectId(id)}, {"$set": updates_dict})
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")

@router.delete("/{id}", status_code=200)
async def delete_student(id: str):
    result = await students_collection.delete_one({"_id": ObjectId(id)})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Student not found")
    return {"message": "Student deleted successfully"}
