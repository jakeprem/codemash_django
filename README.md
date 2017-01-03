Follow these commands to setup and run the server (these are written for Linux)
```
git clone https://gitlab.com/jakeprem/codemash_django
cd codemash_django

pip install virtualenv
virtualenv -p python3 .env

source .env/bin/active
pip install -r requirements.txt

python manage.py migrate
python manage.py populate_data
```

Now create a user for the admin page
```
python manage.py createsuperuser
```

Run the server. Navigate to localhost:8000/admin
```
python manage.py runserver
```


This will remove all data from the database. Alternatively, delete the db.sqlite3 file.
```
python manage.py flush
```