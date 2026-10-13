from fastapi import APIRouter, Depends, HTTPException
from langchain_ollama import ChatOllama
from pydantic import BaseModel
from sqlalchemy.orm import Session

from app.database import get_db
from app.model import Student


router = APIRouter(prefix="/ai", tags=["AI Query"])

llm = ChatOllama(model="llama3.2:1b", temperature=0)


class QueryRequest(BaseModel):
    question: str


@router.post("/query-students")
def ask_student_database(payload: QueryRequest, db: Session = Depends(get_db)):
    try:
        students = db.query(Student).all()
        context_data = "\n".join(
            [
                (
                    f"ID={s.id}, Name={s.student_name}, Class={s.student_class}, "
                    f"Section={s.student_section}, DOB={s.student_dob}, "
                    f"Email={s.student_email}, Phone={s.student_phone}, "
                    f"Course={s.student_course}"
                )
                for s in students
            ]
        )

        if not context_data:
            context_data = "No student records are currently stored."

        prompt = f"""
You are a helpful assistant for a student database application.
Answer only from the database records below.
If the answer cannot be determined from these records, say so clearly.

Database records:
{context_data}

User question: {payload.question}

Answer:
"""

        response = llm.invoke(prompt)
        answer_text = response.content if hasattr(response, "content") else str(response)

        return {"question": payload.question, "answer": answer_text}

    except Exception as exc:
        raise HTTPException(
            status_code=500,
            detail=f"AI query failed: {exc}",
        ) from exc
