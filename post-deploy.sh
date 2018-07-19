python -m pip uninstall -y -r <(python -m pip freeze)
python -m pip install -r requirements.txt
python manage.py migrate 
python manage.py runserver
