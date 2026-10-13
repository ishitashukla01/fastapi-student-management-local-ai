from sqlalchemy import Column, Date, Integer, String

from app.database import Base


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    student_name = Column(String, index=True, nullable=False)
    student_class = Column(String, nullable=False)
    student_section = Column(String, nullable=False)
    student_dob = Column(Date, nullable=False)
    student_email = Column(String, nullable=False)
    student_phone = Column(String, nullable=True)
    student_course = Column(String, nullable=True)
