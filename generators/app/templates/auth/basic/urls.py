from django.urls import path, re_path
from .conf import *
from .controllers.registerController import OauthRegister as registerHandler
from .controllers.basicLoginController import BasicLogin as basicHandler
from .controllers.basicLoginController import BasicLogout as basicLogoutHandler


app_name = Config.app_name

urlpatterns = [
    re_path(r'^register/?$', registerHandler.as_view(), name="register"),
	re_path(r'^login/basic/token/?$',  basicHandler.as_view()),
	re_path(r'^logout/?$',  basicLogoutHandler.as_view())
]