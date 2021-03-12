from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.permissions import IsAuthenticated, AllowAny

from drf_yasg import openapi
from drf_yasg.app_settings import swagger_settings
from drf_yasg.inspectors import CoreAPICompatInspector, FieldInspector, NotHandled, SwaggerAutoSchema
from drf_yasg.utils import no_body, swagger_auto_schema

class ContactPage(APIView):
    permission_classes = (IsAuthenticated,)
    #AllowAny,  IsAuthenticated,

    renderer_classes = [JSONRenderer]
    @swagger_auto_schema(operation_description="Sample GET REQUEST",responses={404: 'unauthorized',200:'message'},
    manual_parameters=[
    openapi.Parameter(name='Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING,description="Bearer YOUR_TOKEN",required=True),])
    def get(self, request, format=None):
        # request.user.groups.filter(name='user_permission')
        #x = request.user.permission
        if request.user.has_perm('sample.access_sample'):
             content = {'message': 'You have special permission'}
        else:
             content = {'message': 'sample module contact page'}       
        return Response(content)