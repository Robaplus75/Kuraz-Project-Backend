# ✅ Task Management API

A simple CRUD API for managing tasks using Django REST Framework for Kuraz tech.

---

### 🔧 Setup Instructions

1. **Clone the Repository**

git clone git@github.com:Robaplus75/Kuraz-Project-Backend.git
cd Kuraz-Project-Backend.git

# Create virtual environment
python -m venv env

# Activate it
source env/bin/activate       # On Linux/macOS
# OR
env\Scripts\activate          # On Windows

pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver

📡 API Endpoints
All API endpoints are prefixed with: /api/

🔹 GET /api/tasks/
List all tasks.

🔹 POST /api/tasks/
Create a new task.

🔹 PUT /api/tasks/<id>/
Update a task to be completed by ID.

🔹 DELETE /api/tasks/<id>/
Delete a task by ID.

🔹 GET /api/tasks/filter/?completed=true|false
Filter tasks based on completion status.

Examples:

/api/tasks/filter/?completed=true
/api/tasks/filter/?completed=false
