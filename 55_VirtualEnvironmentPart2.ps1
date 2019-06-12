#Powershell commands to correctly setup virtual environment with all dependencies

mkdir rice_forest
cd rice_forest
virtualenv project
project/Scripts/activate
pip install Django
django-admin startproject rice_forest .
cd rice_forest
python manage.py migrate
