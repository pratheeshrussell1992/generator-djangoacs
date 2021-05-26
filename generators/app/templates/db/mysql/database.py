database_setting = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
		'STORAGE_ENGINE': 'InnoDB',
        'NAME': 'djangodb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET storage_engine=InnoDB;SET sql_mode='STRICT_TRANS_TABLES'",
        }
    }
}


database_apps = []