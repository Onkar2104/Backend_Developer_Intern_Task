# Backend_Developer_Intern_Task

A RESTful backend API for managing **Users, Projects, and Daily Progress Reports (DPR)**.
This project was developed as part of a **Backend Developer Intern Selection Task**.

The system allows administrators, managers, and workers to manage construction projects and track daily progress reports.

---

# Tech Stack

Backend Framework

* Python
* Django
* Django REST Framework

Database

* PostgreSQL

Authentication

* JWT (JSON Web Token)

Tools

* Postman (API Testing)
* Git & GitHub

---

# Project Features

* User Registration and Login
* JWT Authentication
* Role-based access control (admin, manager, worker)
* Project Management APIs
* Daily Progress Report (DPR) APIs
* PostgreSQL relational database
* RESTful API design
* Proper HTTP status codes and error handling

---

# Database Setup (PostgreSQL)

Install PostgreSQL on your system.

Create a database:

```sql
CREATE DATABASE api_task;
```

Update database configuration in `settings.py`:

```python
DATABASES = {
 'default': {
   'ENGINE': 'django.db.backends.postgresql',
   'NAME': 'api_task',
   'USER': 'postgres',
   'PASSWORD': 'your_password',
   'HOST': 'localhost',
   'PORT': '5432',
 }
}
```

---

# Install Dependencies

Create a virtual environment (recommended):

```
python -m venv venv
```

Activate the environment:

Windows:

```
venv\Scripts\activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Run Database Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

# Run the Server

Start the development server:

```
python manage.py runserver
```

Server will run at:

```
http://127.0.0.1:8000/
```

---

# API Testing

APIs can be tested using **Postman**.

Import the provided collection file:

```
API Testing.postman_collection.json
```

Example base URL:

```
http://127.0.0.1:8000
```

---

# Example API Requests

### Register User

POST `/auth/register`

Request body:

```
{
"name": "Onkar",
"email": "onkar@test.com",
"password": "123456",
"role": "admin"
}
```

Response:

```
{
"userId": 1,
"message": "User created"
}
```

---

### Login User

POST `/auth/login`

Request:

```
{
"email": "onkar@test.com",
"password": "123456"
}
```

Response:

```
{
"token": "JWT_TOKEN",
"user": {
"id": 1,
"name": "Onkar",
"role": "admin"
}
}
```

---

### Create Project

POST `/projects/create`

```
{
"name": "Bridge Construction",
"description": "City bridge project",
"start_date": "2026-03-10",
"end_date": "2026-09-10",
"status": "active",
"created_by": 1
}
```

---

### Create Daily Progress Report

POST `/reports/create`

```
{
"project": 1,
"user": 1,
"date": "2026-03-11",
"work_description": "Concrete work completed",
"weather": "Sunny",
"worker_count": 15
}
```

---

# Implemented API Endpoints

## Authentication

POST `/auth/register`
Create new user account

POST `/auth/login`
Authenticate user and generate JWT token

---

## Projects

POST `/projects/create`
Create a new project

GET `/projects`
List all projects

GET `/projects/{id}`
Get project details

PUT `/projects/{id}/update`
Update project information

DELETE `/projects/{id}/delete`
Delete project (admin only)

---

## Daily Progress Reports

POST `/reports/create`
Create daily progress report

GET `/reports/{project_id}`
List all DPRs for a project

---

# Project Structure

```
api_task/
│
├── user/
├── project/
├── report/
│
├── postman/
│   construction_api.postman_collection.json
│
├── requirements.txt
└── README.md
```

---

# Testing Workflow

Recommended testing order:

1. Register user
2. Login user
3. Create project
4. List projects
5. Create DPR
6. List DPR for project

---

# Author

Onkar Ijare
Backend Developer (Python / Django)
