import os as dbos
BASE_DIR_db = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

database_setting = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dbos.path.join(BASE_DIR_db, 'db.sqlite3'),
    }
}


database_apps = []