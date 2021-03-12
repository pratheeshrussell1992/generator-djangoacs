from django.apps import AppConfig
from .conf import *

class SampleConfig(AppConfig):
    name = Config.app_name
