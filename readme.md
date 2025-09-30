Task Manager Application
📌 Overview

The Task Manager Application is a Django-based project that allows users, admins, and superadmins to manage tasks, track completion reports, and monitor worked hours.
It provides:

JWT-secured REST APIs (via Django REST Framework).

A custom Admin Panel (HTML templates) for superadmins and admins.

Role-based permissions (SuperAdmin, Admin, User).

🗂️ Project Structure

```
TASK_MANAGER/
│
├── accounts/               # Handles user models, permissions, roles
│   ├── migrations/
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── tests.py
│
├── admin_panel/            # Custom admin panel (HTML templates + views)
│   ├── migrations/
│   ├── templates/
│   │   └── admin_panel/
│   │       ├── login.html
│   │       ├── superadmin_dashboard.html
│   │       └── base.html
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── apps.py
│
├── tasks/                  # Task management (models, APIs, serializers)
│   ├── migrations/
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│   ├── models.py
│   └── apps.py
│
├── task_manager/           # Project settings and root URLs
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── requirements.txt


```


🚀 Features
🔑 Authentication

JWT authentication (via rest_framework_simplejwt).

Login with username & password → receive JWT token.

Token refresh supported.

📋 Tasks API

GET /api/tasks/ → List tasks assigned to logged-in user.

PUT /api/tasks/{id}/ → Update task (mark as completed, submit report + worked hours).

GET /api/tasks/{id}/report/ → View completion report (Admins & SuperAdmins only).

🖥️ Admin Panel

Custom-built HTML templates.

SuperAdmin Dashboard

Manage admins (create, delete, promote/demote).

Manage users (create, delete, assign roles).

View all tasks and completion reports.

Admin Dashboard

Assign tasks to users.

Manage tasks for their users.

View completion reports (cannot manage roles).

User Access

View assigned tasks.

Submit completion reports + worked hours.

| Method | Endpoint                  | Description                                       |
| ------ | ------------------------- | ------------------------------------------------- |
| POST   | `/api/token/`             | Obtain JWT token                                  |
| POST   | `/api/token/refresh/`     | Refresh JWT token                                 |
| GET    | `/api/tasks/`             | Fetch logged-in user’s tasks                      |
| PUT    | `/api/tasks/{id}/`        | Update task status, add completion report & hours |
| GET    | `/api/tasks/{id}/report/` | View task report (Admins & SuperAdmins only)      |


✅ Requirements

Python 3.10+

Django 5.x

Django REST Framework

djangorestframework-simplejwt


👨‍💻 Author

Developed as part of the Task Manager Project for learning and demonstrating:

Django REST API design

Role-based permissions

JWT authentication

Custom admin panels
