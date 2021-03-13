# FRAMEWORK SETTINGS
REST_FRAMEWORK_PERMISSIONS = { 
  'DEFAULT_PERMISSION_CLASSES': ( 
      'rest_framework.permissions.IsAuthenticated', 
  ), 
  'DEFAULT_AUTHENTICATION_CLASSES': ( 
     'rest_framework.authentication.TokenAuthentication',,
  ), 
} 

# FRAMEWORK APPS
AUTH_APPS = [
    'rest_framework.authtoken', 
]

# SETTINGS FOR OAUTH
OAUTH_CLIENTID_SETTING = ''
OAUTH_CLIENT_SETTING  = ''

# SETTINGS FOR JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
JWT_SETTING = {}