"""<%= project_name %> URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


urlpatterns = [
    path('user/', include("modules.user.urls")),
    path('sample/', include("modules.sample.urls"))
]



if settings.DEBUG:
    schema_view = get_schema_view(
    openapi.Info(
        title="Django ACS TEMPLATE Docs",
        default_version='v1',
        description="This is a documentation of ACS Django Template",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="pratheeshrussell@gmail.com"),
        license=openapi.License(name="BSD License"),
        ),
        public=True,
        permission_classes=(permissions.AllowAny,),)

    urlpatterns_DEV = [
        path('admin/', admin.site.urls),
        re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
        re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
        re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc')
		#re_path(r'^oauthapp/', include('oauth2_provider.urls', namespace='oauth2_provider')),
        ]
    urlpatterns.extend(urlpatterns_DEV)
    try:
        import oauthlib
        oautpatterns_DEV = [re_path(r'^oauthapp/', include('oauth2_provider.urls', namespace='oauth2_provider')),]
        urlpatterns.extend(oautpatterns_DEV)
    except ImportError:
        pass