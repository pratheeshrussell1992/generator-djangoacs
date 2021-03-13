from datetime import timedelta


# FRAMEWORK SETTINGS
REST_FRAMEWORK_PERMISSIONS = { 
  'DEFAULT_PERMISSION_CLASSES': ( 
      'rest_framework.permissions.IsAuthenticated', 
  ), 
  'DEFAULT_AUTHENTICATION_CLASSES': ( 
      'rest_framework_simplejwt.authentication.JWTAuthentication',
  ), 
} 

# FRAMEWORK APPS
AUTH_APPS = [
    'rest_framework_simplejwt.token_blacklist',
]

# SETTINGS FOR OAUTH
OAUTH_CLIENTID_SETTING = ''
OAUTH_CLIENT_SETTING  = ''

# SETTINGS FOR JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
JWT_SETTING = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1)
}