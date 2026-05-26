# BodhiTree Django Clone

A Django-based student performance dashboard inspired by the BodhiTree LMS platform.

## Features

- Student Login System
- Dynamic Dashboard
- Fetch Logged-in User Data
- Leaderboard Ranking
- Highest Marks Calculation
- Time Taken Display
- Responsive Frontend using HTML & CSS
- Django Backend with SQLite Database

---

## Tech Stack

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Django
- SQLite3

---

## Project Structure

```bash
Bodhitree_Demo/
│
├── student/
│   ├── migrations/
│   ├── static/
│   │   ├── style2.css
│   │   └── bodhitree icon.png
│   │
│   ├── templates/
│   │   └── index.html
│   │
│   ├── admin.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── Bodhitree_Demo/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── manage.py
└── README.md
```

---

## Database Model

```python
class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    roll_no = models.IntegerField(unique=True)

    name = models.CharField(max_length=100)

    marks = models.IntegerField()

    time_taken = models.FloatField(default=0)
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/BodhiTree-Django.git
```

### Enter Project Folder

```bash
cd BodhiTree-Django
```

### Install Django

```bash
pip install django
```

### Run Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

### Run Server

```bash
python manage.py runserver
```

---

## Access Project

### Homepage

```txt
http://127.0.0.1:8000/
```

### Admin Panel

```txt
http://127.0.0.1:8000/admin
```

### Login Page

```txt
http://127.0.0.1:8000/accounts/login/
```

---

## Functionalities

- Displays logged-in student's:
  - Marks
  - Highest Marks
  - Time Taken
  - Leaderboard Rank

- Uses Django Authentication System

- Data fetched dynamically using Fetch API and JSON

---

## Future Improvements

- JWT Authentication
- REST API using Django REST Framework
- Charts and Analytics
- Real-time Leaderboard
- Dark Mode
- Deployment on Render/Heroku/AWS

---

## Author

Aniket Chakraborty

---

## License

This project is for educational and learning purposes.
