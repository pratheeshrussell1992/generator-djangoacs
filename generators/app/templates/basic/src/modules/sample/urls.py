from django.urls import path
from .conf import *
from .controllers.indexController import index as indexHandler
from .controllers.contactController import ContactPage  as contactHandler

app_name = Config.app_name

urlpatterns = [
    path("", indexHandler, name="index"),
    path("contact/", contactHandler.as_view() , name="contact")
]