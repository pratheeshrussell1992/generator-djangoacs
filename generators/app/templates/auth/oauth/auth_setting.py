from datetime import timedelta


# FRAMEWORK SETTINGS
REST_FRAMEWORK_PERMISSIONS = { 
  'DEFAULT_PERMISSION_CLASSES': ( 
      'rest_framework.permissions.IsAuthenticated', 
  ), 
  'DEFAULT_AUTHENTICATION_CLASSES': ( 
      'oauth2_provider.contrib.rest_framework.OAuth2Authentication',
  ), 
} 

# FRAMEWORK APPS
AUTH_APPS = [
    'oauth2_provider', 
]

# SETTINGS FOR OAUTH
OAUTH_CLIENTID_SETTING = 'YOUR CLIENT ID HERE'
OAUTH_CLIENT_SETTING  = 'CLIENT SECRET HERE'

# SETTINGS FOR JWT
# https://django-rest-framework-simplejwt.readthedocs.io/en/latest/settings.html
JWT_SETTING = {}