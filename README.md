# FastAPI Student Management System with Local AI

I built this project during my AI/ML internship while learning backend development with Python.

At the beginning, I was mainly learning how APIs work, how FastAPI is structured, how a backend connects to a database, and how CRUD operations are implemented. Later, I also learned how a local LLM can be connected with a FastAPI backend using Ollama.

The final project is a student management API where student records can be created, viewed, updated, and deleted. I also added an AI endpoint that can answer simple questions based on the student records stored in the database.

## What I built

The project has two main parts.

The first part is a student management backend built using FastAPI, SQLite, SQLAlchemy, and Pydantic.

The second part is a local AI feature using Ollama, where the model can answer questions based on the data stored in the student database.

For example, after adding student records, I can ask:

```json
{
  "question": "How many students are there?"
}
```

and the API can return an answer such as:

```json
{
  "question": "How many students are there?",
  "answer": "There are 3 students in the database records."
}
```

I also tested questions like:

```text
What courses are the students enrolled in?
```

and the model answered using the student data stored in SQLite.

## Project features

The student API supports:

- Creating a student
- Getting all students
- Getting one student using student ID
- Updating selected student details
- Deleting a student
- Returning proper errors when a student is not found
- Asking AI-based questions about the student records

## Technologies used

I used the following technologies while building this project:

- Python
- FastAPI
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn
- Ollama
- LangChain
- Swagger UI
- Git and GitHub
- VS Code

## Project structure

The project is separated into different files so that each part of the backend has its own responsibility.

```text
fastapi-student-management-local-ai/
│
├── app/
│   ├── routes/
│   │   ├── ai_query.py
│   │   ├── base.py
│   │   ├── create_student.py
│   │   ├── delete_students.py
│   │   ├── get_students.py
│   │   └── update_student.py
│   │
│   ├── __init__.py
│   ├── config.py
│   ├── database.py
│   ├── model.py
│   └── schemas.py
│
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```

## What each main file does

`main.py` is the main starting point of the FastAPI application.

`config.py` reads configuration values from the environment.

`database.py` handles the database connection and database sessions.

`model.py` defines the structure of the student table in the database.

`schemas.py` defines the format of data that the API accepts and returns.

The `routes` folder contains the different API operations such as create, read, update, delete, and AI query.

I learned that separating the code like this makes the backend easier to understand and maintain compared to writing everything in one file.

## Database

For this project, I used SQLite.

The database URL is:

```env
DATABASE_URL=sqlite:///./students.db
```

The database file is created locally and is not uploaded to GitHub.

One important concept I learned was the use of SQLAlchemy sessions.

For every request, the application opens a database session, performs the required database operation, and then closes the session.

This helped me understand why database connections should not stay open unnecessarily.

## CRUD operations

A major part of this project was learning CRUD.

CRUD stands for:

```text
C - Create
R - Read
U - Update
D - Delete
```

### Create student

```text
POST /students/
```

This endpoint creates a new student record.

The flow is:

```text
Student data
↓
Pydantic validation
↓
Database session
↓
Create student object
↓
db.add()
↓
db.commit()
↓
db.refresh()
↓
Return created student
```

A successful create request returns:

```text
201 Created
```

### Get all students

```text
GET /students/
```

This endpoint returns all student records.

I also learned about the basic pagination idea using `skip` and `limit`.

### Get one student

```text
GET /students/{student_id}
```

This endpoint searches for one student using the student ID.

If the student exists, the record is returned.

If the student does not exist, the API returns:

```text
404 Not Found
```

### Update student

```text
PATCH /students/{student_id}
```

This endpoint updates an existing student.

I learned how partial updates work, where only the fields actually sent by the user are updated instead of replacing the complete record.

### Delete student

```text
DELETE /students/{student_id}
```

This endpoint deletes a student from the database.

A successful deletion returns:

```text
204 No Content
```

## Pydantic schemas

Another important concept I learned was the difference between database models and API schemas.

The database model defines how the data is stored in SQLite.

The Pydantic schemas define what data the API receives and returns.

In this project I used schemas for:

- common student fields
- creating a student
- updating a student
- returning student data

This helped me understand how validation is handled before data reaches the database.

## HTTP status codes

While testing the API, I also learned how HTTP status codes are used.

Some of the codes I worked with were:

```text
200 OK
201 Created
204 No Content
404 Not Found
422 Validation Error
500 Internal Server Error
```

Earlier these numbers were only theory for me, but after testing the APIs in Swagger I could clearly understand where and why they are used.

## FastAPI and Swagger

I used FastAPI's Swagger documentation to test all the endpoints.

After running the project, Swagger can be opened at:

```text
http://127.0.0.1:8000/docs
```

This made API testing much easier because I could send requests directly from the browser and check the request body, response body, and status code.

## Local AI using Ollama

The AI part of the project was added after the CRUD backend was working.

I used Ollama to run an LLM locally on my own system instead of calling a cloud API.

The model I used was:

```text
llama3.2:1b
```

I downloaded it using:

```bash
ollama pull llama3.2:1b
```

and tested it using:

```bash
ollama run llama3.2:1b
```

One important thing I learned here was the difference between an online hosted LLM and a local LLM.

With Ollama, the model runs on the local computer and does not need a per-request external API call.

## AI query endpoint

The AI endpoint in this project is:

```text
POST /ai/query-students
```

The basic flow is:

```text
User question
↓
FastAPI endpoint
↓
Student records are read from SQLite
↓
The records are converted into context
↓
The context and question are sent to the local Ollama model
↓
The model generates an answer
↓
FastAPI returns the response
```

This helped me understand how an LLM can be connected with normal backend and database logic.

For example, after adding three students, I asked:

```text
How many students are there?
```

and the model correctly answered that there were three students.

I also asked:

```text
What courses are the students enrolled in?
```

and the model answered using the student records available in the database.

## Virtual environment

I also learned why virtual environments are useful.

For this project, I created a separate Python virtual environment so that all project libraries remain isolated from other Python projects on my system.

Example:

```bash
python -m venv venv
```

In Git Bash:

```bash
source venv/Scripts/activate
```

Then I installed all dependencies using:

```bash
python -m pip install -r requirements.txt
```

## Running the project

Clone the repository:

```bash
git clone https://github.com/ishitashukla01/fastapi-student-management-local-ai.git
```

Move into the project folder:

```bash
cd fastapi-student-management-local-ai
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it and install the dependencies:

```bash
python -m pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
DATABASE_URL=sqlite:///./students.db
```

Make sure Ollama is installed and the model is available:

```bash
ollama list
```

Then run the FastAPI application:

```bash
python -m uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000/docs
```

to test all the APIs.

## What I learned during this project

This project helped me understand much more than just writing API code.

I learned how a backend project is actually structured and how different files work together.

I learned:

- how FastAPI routes work
- how REST APIs are created
- how request and response data is validated
- how SQLite stores data
- how SQLAlchemy connects Python code with the database
- how database sessions work
- how CRUD operations are implemented
- how HTTP status codes are used
- how Swagger is used for API testing
- how virtual environments keep dependencies separate
- how `.env` files are used for configuration
- how `.gitignore` protects local and sensitive files
- how a local LLM can run using Ollama
- how FastAPI can communicate with a local AI model
- how database records can be passed as context to an LLM
- how to debug issues related to Python packages, ports, models, and local servers
- how to prepare and push a working project to GitHub

While working on this project I also faced practical issues such as virtual environment activation, dependency installation, Ollama setup, local model downloading, disk space problems, and API errors. Solving those problems was also an important part of the learning process.

## Repository safety

The following local files are intentionally not uploaded to GitHub:

```text
.env
venv/
__pycache__/
students.db
```

The repository only contains `.env.example` as a reference.

## Current scope

This is currently a backend project.

The focus was on understanding FastAPI, database operations, API structure, and local AI integration.

A frontend interface is not included at this stage.

## Possible improvements

In the future, I can extend this project by adding:

- a frontend interface
- login and authentication
- PostgreSQL or MySQL
- better search and filtering
- automated API tests
- Docker support
- cloud deployment
- more advanced AI queries
- better handling of larger datasets

## Author

**Ishita Shukla**

B.Tech CSE - Artificial Intelligence & Machine Learning

Built during my AI/ML internship as a practical project to understand backend development, APIs, databases, and local LLM integration.
