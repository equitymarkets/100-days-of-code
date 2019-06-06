#Day 50: Working to install Django today

#The following are the command shell commands that worked for me when installing Django, setting up a virtual environment, and starting 
#an app running.

virtualenv .

./Scripts/activate

pip install django

django-admin.py startproject python riceforest

cd riceforest

.\manage.py startapp riceforest





