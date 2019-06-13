mkdir rice_forest
cd rice_forest
virtualenv project
project/Scripts/activate
pip install Django
django-admin startproject rice_forest .
python manage.py migrate
python manage.py startapp forest
python manage.py createsuperuser

http://127.0.0.1:8000/
