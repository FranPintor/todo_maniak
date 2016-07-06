ToDo Maniaks

Deploy Develop Environment (Linux  or Mac)

** DataBase
Mysql Server Runing In Port 3306
Database Name: todo_maniak
Database User: root
Database Pass: root

** PIP & Virtualenvironment
1.- Install PIP : easy_install pip
2.- Install VIRTUALENV: pip virtualenv
3.- Create Environment: virtualenv your_env_name
4.- Activate Environment: source bin/activate
5.- Clone Repository: git clone git@github.com:coffe67/todo_maniak.git
6.- Go To Project Folder: cd todo_maniak
10.- Install requirements: pip install -r requirements.txt
11.- Migrate DB: python manage.py migrate
12.- Create superuser (django admin): python manage.py createsuperuser
12.- Runserver: python manage.py runserver


