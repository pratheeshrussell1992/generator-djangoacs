from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.conf import settings as mainSettings
from datetime import timedelta


from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import rest_framework.status as  HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework_simplejwt.settings import api_settings
from rest_framework_simplejwt.exceptions import TokenError
#from rest_framework_simplejwt.serializers import TokenRefreshSerializer


from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema


class JwtLogin(APIView):
    permission_classes = (AllowAny,)
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
                return Response({'error': 'Please provide both username and password'},status=400)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},status=404)
            refresh = RefreshToken.for_user(user)
            return Response({'token': str(refresh.access_token),
            'refresh_token':str(refresh),
            "token_type":"Bearer"},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = JsonResponse({'success': 'false'},status=status_code)
            return response



class JwtRenewLogin(APIView):
    permission_classes = (AllowAny,)
    #AllowAny,  IsAuthenticated,

    renderer_classes = [JSONRenderer]

    @csrf_exempt
    @swagger_auto_schema(operation_description="Renew Token REQUEST",responses={404: 'unauthorized',200:'success'},
    request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'refresh token': openapi.Schema(type=openapi.TYPE_STRING, description='enter refresh token'),
    }))
    def post(self, request, format=None):
        if request.method == "POST":
            ref_token = request.data.get("refresh_token")  
            try:
                reftokenModel =RefreshToken(ref_token) # RefreshToken(token=ref_token)
            except TokenError:
                return Response({'success': False,"message":"Token is invalid or expired. Do a full login" },status=HTTPStatus.HTTP_400_BAD_REQUEST)
            data = {'access': str(reftokenModel.access_token),'refresh' : ref_token}

            if api_settings.ROTATE_REFRESH_TOKENS:
                if api_settings.BLACKLIST_AFTER_ROTATION:
                    try:
                        reftokenModel.blacklist()
                    except AttributeError:
                        pass
                reftokenModel.set_jti()
                reftokenModel.set_exp()
                data['refresh'] = str(reftokenModel)
            
            return Response({'token': data['access'],
            'refresh_token':data['refresh'],
            "token_type":"Bearer"},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = JsonResponse({'success': 'false'},status=status_code)
            return response
