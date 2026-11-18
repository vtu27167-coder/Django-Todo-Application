# Django Todo Application

A simple and user-friendly Todo Application developed using Python and Django.

## Features

- Add new tasks
- View pending tasks
- View completed tasks
- Mark tasks as completed
- Move completed tasks back to pending
- Edit existing tasks
- Delete tasks

## Technologies Used

- Python
- Django
- HTML
- CSS
- Bootstrap
- SQLite

## Project Structure

```text
project3/
├── app/
│   ├── migrations/
│   ├── templates/
│   │   └── app/
│   │       ├── home.html
│   │       └── edit.html
│   ├── models.py
│   └── views.py
├── project/
│   ├── settings.py
│   └── urls.py
├── manage.py
└── README.md
```

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/vtu27167-coder/Django-Todo-Application.git
```

2. Open the project folder:

```bash
cd Django-Todo-Application
```

3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the environment on Windows:

```bash
env\Scripts\activate
```

5. Install Django:

```bash
pip install django
```

6. Apply migrations:

```bash
python manage.py migrate
```

7. Start the server:

```bash
python manage.py runserver
```

8. Open in your browser:

```text
http://127.0.0.1:8000/
```

## Author

Uday Kumar

GitHub: https://github.com/vtu27167-coder