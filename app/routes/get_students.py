from typing import List

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student
from app.schemas import StudentResponse


router = APIRouter(prefix="/students", tags=["Students"])


@router.get("/", response_model=List[StudentResponse])
def get_all_students(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=500),
    db: Session = Depends(get_db),
):
    return db.query(Student).offset(skip).limit(limit).all()


@router.get("/{student_id}", response_model=StudentResponse)
def get_student_by_id(student_id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == student_id).first()
    if not student:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Student not found",
        )
    return student
