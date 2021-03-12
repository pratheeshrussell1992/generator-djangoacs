from django.urls import path, re_path
from .conf import *
from .controllers.registerController import OauthRegister as registerHandler
from .controllers.oauthLoginController import OauthLogin as oauthHandler
from .controllers.oauthLoginController import OauthRenewLogin as oauthRefreshHandler
from .controllers.oauthLoginController import OauthLogout as oauthLogoutHandler
app_name = Config.app_name

urlpatterns = [
    re_path(r'^register/?$', registerHandler.as_view(), name="register"),
    re_path(r'^login/oauth/?$',  oauthHandler.as_view()),
    re_path(r'^login/renew/?$',  oauthRefreshHandler.as_view()),
    re_path(r'^logout/?$',  oauthLogoutHandler.as_view())
]