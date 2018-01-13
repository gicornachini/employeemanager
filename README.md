# Employee-Manager
Resolução do desafio técnico proposto pelo Luizalabs

## Requirements
- Python 2.7.11
- Django 1.11.9
- Django REST framework 3.7.7+
- model-mommy 1.5.0 # Help setup tests
- django-fixture-magic 0.1.3 # Create complex fixtures

## How to run
After clone/download, do:

1. Install requirements ``` pip install -r requirements.txt ```

2. Migrate ``` python manage.py migrate ```

3. Load data from fixture ``` python manage.py loaddata employees/fixtures/employees.json```

3. Run ``` python manage.py runserver ```

4. Open <a href='http://localhost:8000/employee/'>http://localhost:8000/employee/</a> or run in the terminal ```curl -H "Content-Type: application/javascript" http://localhost:8000/employee/list/ ```