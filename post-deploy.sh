python -m pip uninstall -y -r requirements.txt
python -m pip install -r requirements.txt
python manage.py migrate 
python manage.py runserver
