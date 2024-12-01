from fastapi import APIRouter, HTTPException, Response, status
from models.student import Student, StudentUpdate
from utils.util import merge
from schemas.student import (
    studentEntity,
    StudentEntityOnlyID,
    studentsEntityWithOutAddress,
)
from config.db import students_db
from bson import ObjectId

student = APIRouter(prefix="/students", tags=["students"])


@student.post("/")
async def create_student(student: Student, response: Response):
    response.status_code = status.HTTP_201_CREATED
    student_dict = dict(student)
    student_dict["address"] = dict(student.address)
    inserted_student = await students_db.students.insert_one(student_dict)
    return StudentEntityOnlyID(inserted_student)


@student.get("/")
async def get_students(country: str = None, age: int = None):
    query = {}
    if country:
        query["address.country"] = country
        # Currently country is case sensitive
    if age:
        query["age"] = age
    # Limited Max Elements to 1000 for performance
    students = await students_db.students.find(query).to_list(1000)
    return {"data": studentsEntityWithOutAddress(students)}


@student.get("/{id}")
async def get_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    student = await students_db.students.find_one({"_id": ObjectId(id)})
    if student:
        return studentEntity(student)
    raise HTTPException(status_code=404, detail="Student not found")


@student.patch("/{id}")
async def update_student(id: str, obj: StudentUpdate, response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    student = await students_db.students.find_one({"_id": ObjectId(id)})
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")

    update_data = dict(obj)
    update_data["address"] = dict(update_data["address"])
    del student["_id"]
    update_data = merge(update_data, student)

    await students_db.students.update_many({"_id": ObjectId(id)}, {"$set": update_data})
    return {}


@student.delete("/{id}")
async def delete_student(id: str):
    if not ObjectId.is_valid(id):
        raise HTTPException(status_code=400, detail="Invalid ID format")

    result = await students_db.students.delete_one({"_id": ObjectId(id)})

    if result.deleted_count == 1:
        return {}

    raise HTTPException(status_code=404, detail="Student not found")
