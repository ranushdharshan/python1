from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
app = FastAPI(
    title="Student Directory API",
    description="A beginner project for managing student records",
    version="1.0.0",
)
# Temporary storage; data resets when the server restarts.
students = []
next_student_id = 1
class StudentCreate(BaseModel):
    name: str = Field(min_length=2, max_length=100)
    email: str = Field(min_length=5, max_length=150)
    department: str = Field(min_length=2, max_length=100)
@app.get("/")
def home():
    return {"message": "Welcome to the Student Directory API"}
@app.post("/students", status_code=201)
def create_student(student: StudentCreate):
    global next_student_id
    for existing in students:
        if existing["email"].lower() == student.email.lower():
            raise HTTPException(
                status_code=409,
                detail="A student with this email already exists",
            )
    new_student = {
        "id": next_student_id,
        "name": student.name.strip(),
        "email": student.email.strip().lower(),
        "department": student.department.strip(),
    }
    students.append(new_student)
    next_student_id += 1
    return new_student
@app.get("/students")
def list_students():
    return students
@app.get("/students/{student_id}")
def get_student(student_id: int):
    for student in students:
        if student["id"] == student_id:
            return student
    raise HTTPException(status_code=404, detail="Student not found")
@app.delete("/students/{student_id}")
def delete_student(student_id: int):
    for index, student in enumerate(students):
        if student["id"] == student_id:
            deleted_student = students.pop(index)
            return {
                "message": "Student deleted successfully",
                "student": deleted_student,
            }
    raise HTTPException(status_code=404, detail="Student not found")