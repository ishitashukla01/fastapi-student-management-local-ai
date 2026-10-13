from datetime import date
from typing import Optional

from pydantic import BaseModel, ConfigDict


class StudentBase(BaseModel):
    student_name: str
    student_class: str
    student_section: str
    student_dob: date
    student_email: str
    student_phone: Optional[str] = None
    student_course: Optional[str] = None


class StudentCreate(StudentBase):
    pass


class StudentUpdate(BaseModel):
    student_name: Optional[str] = None
    student_class: Optional[str] = None
    student_section: Optional[str] = None
    student_dob: Optional[date] = None
    student_email: Optional[str] = None
    student_phone: Optional[str] = None
    student_course: Optional[str] = None


class StudentResponse(StudentBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
