# FastAPI Student Management & Local AI Query Project

A Python backend project developed during the **EWB Edu Tech AI/ML Internship**. It provides CRUD APIs for managing student records with **FastAPI**, **SQLAlchemy**, and **SQLite**, plus an optional local AI extension using **Ollama + LangChain**.

## Features

- Create student records
- List students with basic pagination
- Retrieve a student by ID
- Partially update student details
- Delete student records
- SQLite persistence with SQLAlchemy ORM
- Pydantic request/response validation
- Automatic Swagger/OpenAPI documentation
- Local AI query endpoint using Ollama
- Grounded AI answers based on stored student records

## Tech Stack

- Python 3.11+
- FastAPI
- Uvicorn
- SQLAlchemy
- SQLite
- Pydantic / pydantic-settings
- Ollama
- LangChain Ollama integration

## Project Structure

```text
.
├── app/
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   ├── schemas.py
│   └── routes/
│       ├── __init__.py
│       ├── base.py
│       ├── create_student.py
│       ├── get_students.py
│       ├── update_student.py
│       ├── delete_students.py
│       └── ai_query.py
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.11 or later
- pip
- Ollama (only required for the optional AI endpoint)

## Setup

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_REPOSITORY_FOLDER>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

Activate it on Git Bash:

```bash
source venv/Scripts/activate
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Configure the environment

Copy `.env.example` to `.env`. The default SQLite configuration is:

```env
DATABASE_URL=sqlite:///./students.db
```

### 5. Run the FastAPI application

```bash
python -m uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

## CRUD Endpoints

| Method | Endpoint | Purpose |
| --- | --- | --- |
| POST | `/students/` | Create a student |
| GET | `/students/` | List students |
| GET | `/students/{student_id}` | Retrieve one student |
| PATCH | `/students/{student_id}` | Update provided fields |
| DELETE | `/students/{student_id}` | Delete a student |

### Example student request

```json
{
  "student_name": "Aarav Sharma",
  "student_class": "12",
  "student_section": "A",
  "student_dob": "2008-05-18",
  "student_email": "aarav@example.com",
  "student_phone": "9999999999",
  "student_course": "Computer Science"
}
```

## Optional Local AI Extension

Install Ollama separately and pull the local model:

```bash
ollama pull llama3.2:1b
```

Ensure Ollama is running, then start the FastAPI application.

AI endpoint:

```text
POST /ai/query-students
```

Example request:

```json
{
  "question": "How many students are there?"
}
```

The backend retrieves student records itself and provides them as context to the local model. The model is **not allowed to execute SQL directly**.

## API Testing

Use Swagger UI at `http://127.0.0.1:8000/docs` to test all endpoints.

Recommended checks:

1. Create a student and verify `201 Created`.
2. Retrieve all students and confirm the new record appears.
3. Retrieve the student by ID.
4. Update selected fields and confirm the changes.
5. Delete the student and verify `204 No Content`.
6. Request the deleted ID again and verify `404 Not Found`.
7. If Ollama is installed, test `/ai/query-students` with a question grounded in the stored records.

## Security / Data Notes

- Do not commit `.env`, passwords, API keys, or secrets.
- Use only dummy student data in this project.
- The SQLite database file is excluded from Git so personal data is not published.
- The local AI model receives only records retrieved by backend code; it does not receive unrestricted SQL access.

## Learning Outcomes

This project provided hands-on practice with:

- FastAPI backend development
- RESTful CRUD API design
- SQLAlchemy ORM and SQLite persistence
- Pydantic validation and response schemas
- Modular Python project structure
- Virtual environments and dependency management
- Swagger/OpenAPI testing
- Local LLM inference with Ollama
- LangChain integration
- Grounding AI responses in application data

## Author

**Ishita Shukla**

Developed as part of the EWB Edu Tech AI/ML Internship.
