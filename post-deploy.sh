python -m pip install virtualenv
virtualenv env
python -m pip install -r requirements.txt
python manage.py migrate 
python manage.py runserver
