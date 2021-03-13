from django.urls import path, re_path
from .conf import *
from .controllers.registerController import OauthRegister as registerHandler
from .controllers.jwtLoginController import JwtLogin as jwtHandler
from .controllers.jwtLoginController import JwtRenewLogin as jwtRefreshHandler

app_name = Config.app_name

urlpatterns = [
    re_path(r'^register/?$', registerHandler.as_view(), name="register"),
    path('login/jwt/token/', jwtHandler.as_view(), name='token_obtain_pair'),
    path('login/jwt/renew/', jwtRefreshHandler.as_view(), name='token_refresh')
]