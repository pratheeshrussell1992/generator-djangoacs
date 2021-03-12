from django.apps import AppConfig
from .conf import Config as config

class UserConfig(AppConfig):
    name = config.app_name
