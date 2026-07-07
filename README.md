# employee-shift-attendance-management-system
FastAPI Employee Shift &amp; Attendance Management System with JWT Authentication, Employee Management, Shift Management, Attendance Tracking, Reports, SQLAlchemy ORM, Pagination, Logging, Docker Support, and Unit Tests.
# Employee Shift & Attendance Management System

## Features

- JWT Authentication
- Employee Management (CRUD)
- Shift Management
- Attendance Management
- Monthly Attendance Report
- Search, Filter & Pagination
- SQLAlchemy ORM
- SQLite Database
- Docker Support
- Logging
- Basic Unit Tests

---

## Setup Instructions

### Install Dependencies


pip install -r requirements.txt


### Run Project


py -m uvicorn main:app --reload


Swagger URL
```
http://127.0.0.1:8000/docs


## Environment Variables


SECRET_KEY=attendance_secret_key
ALGORITHM=HS256


## API Examples

- POST `/auth/register`
- POST `/auth/login`
- POST `/employees`
- POST `/shifts`
- POST `/attendance`



## Docker Deployment


docker build -t attendance-system .
docker run -p 8000:8000 attendance-system


## Assumptions

- Employee email must be unique.
- One attendance record per employee per day.
- Check-out must be after check-in.
- Employee records use soft delete.
