from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import rest_framework.status as  HTTPStatus

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema


class BasicLogin(APIView):
    permission_classes = (AllowAny,)
    #AllowAny,  IsAuthenticated,

    renderer_classes = [JSONRenderer]

    @csrf_exempt
    @swagger_auto_schema(operation_description="Login REQUEST",responses={404: 'unauthorized',200:'success'},
    request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='enter username'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='enter password'),
    }))
    def post(self, request, format=None):
        if request.method == "POST":
            username = request.data.get("username")
            password = request.data.get("password")
            if username is None or password is None:
                return Response({'error': 'Please provide both username and password'},status=HTTPStatus.HTTP_400_BAD_REQUEST)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},status=HTTPStatus.HTTP_400_BAD_REQUEST)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.HTTP_405_METHOD_NOT_ALLOWED
            response = Response({'success': 'false'},status=status_code)
            return response;

class BasicLogout(APIView):
    permission_classes = (IsAuthenticated,)
    renderer_classes = [JSONRenderer]

    @csrf_exempt
    @swagger_auto_schema(operation_description="Logout User",responses={404: 'unauthorized',200:'success'},
    manual_parameters=[
    openapi.Parameter(name='Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING,description="token YOUR_TOKEN",required=True),])
    def post(self, request, format=None):
        if request.method == "POST":
            request.user.auth_token.delete()
            return Response({'success': 'true'},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.HTTP_405_METHOD_NOT_ALLOWED
            response = Response({'success': 'false'},status=status_code)
            return response