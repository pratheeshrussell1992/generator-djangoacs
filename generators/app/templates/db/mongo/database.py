#Host should be of form 
#mongodb://USERNAME:PASSWORD@HOST:PORT/DATABASE

database_setting = {
    'default': {
        'ENGINE': 'djongo',
        "CLIENT": {
           "name": "admin",
           "host": "mongodb://admin:Acs2021@db:27017/admin",
           "username": "admin",
           "password": "Acs2021",
           "authMechanism": "SCRAM-SHA-1",
        }, 
    }
}


database_apps = []