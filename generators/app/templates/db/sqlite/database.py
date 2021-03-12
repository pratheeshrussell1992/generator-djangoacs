import os as dbos
BASE_DIR_db = dbos.path.dirname(dbos.path.dirname(dbos.path.abspath(__file__)))

database_setting = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': dbos.path.join(BASE_DIR_db, 'db.sqlite3'),
    }
}


database_apps = []