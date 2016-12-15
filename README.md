Follow these commands to setup and run the server
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

This will remove all data from the database. Alternatively, delete the db.sqlite3 file.
```
python manage.py flush
```