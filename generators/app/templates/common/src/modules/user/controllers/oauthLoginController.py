from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from django.utils import timezone
from django.conf import settings as mainSettings
from datetime import timedelta

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
import rest_framework.status as  HTTPStatus
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.renderers import JSONRenderer

from oauthlib import common, oauth2
from oauthlib.oauth2 import BearerToken
from oauth2_provider.views.base import TokenView
from oauth2_provider.models import Application,AccessToken,RefreshToken

from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema


class OauthLogin(APIView,TokenView):
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
                return Response({'error': 'Please provide both username and password'},status=400)
            user = authenticate(username=username, password=password)
            if not user:
                return Response({'error': 'Invalid Credentials'},status=404)

            expires = timezone.now() + timedelta(seconds=3600000)
            application = Application.objects.get(client_id=mainSettings.OAUTH_CLIENTID)
            access_token = AccessToken(
                user=user,scope='',
                expires=expires,
                token=common.generate_token(),
                
                application=application)
            access_token.save()
            refresh_token = RefreshToken(
                user=user,
                token=common.generate_token(),
                application=application,
                access_token=access_token
                )
            refresh_token.save()
            
            return Response({'token': access_token.token,
            'refresh_token':refresh_token.token,
            "token_type":"Bearer"},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = JsonResponse({'success': 'false'},status=status_code)
            return response



class OauthRenewLogin(APIView,TokenView):
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
            expires = timezone.now() + timedelta(seconds=3600000)
            application = Application.objects.get(client_id= mainSettings.OAUTH_CLIENTID)       
            try:
                refTokenModel = RefreshToken.objects.get(token=ref_token)
            except RefreshToken.DoesNotExist:
                return Response({'error': 'Refresh token invalid'},status=400)
            access_token = AccessToken(
                user = refTokenModel.user,
                scope='',
                expires=expires,
                token=common.generate_token(),             
                application=application)
            access_token.save()
            
            #refresh_token = RefreshToken(token=ref_token,
             #   application=application,access_token=access_token )

            refTokenModel.access_token = access_token
            refTokenModel.save()
            
            return Response({'token': access_token.token,
            'refresh_token':ref_token,
            "token_type":"Bearer"},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = JsonResponse({'success': 'false'},status=status_code)
            return response

class OauthLogout(APIView,TokenView):
    permission_classes = (IsAuthenticated,)
    #AllowAny,  IsAuthenticated,

    renderer_classes = [JSONRenderer]

    @csrf_exempt
    @swagger_auto_schema(operation_description="Logout User",responses={404: 'unauthorized',200:'success'},
    manual_parameters=[
    openapi.Parameter(name='Authorization', in_=openapi.IN_HEADER,
    type=openapi.TYPE_STRING,description="Bearer YOUR_TOKEN",required=True),])
    def post(self, request, format=None):
        if request.method == "POST":
            current_token = request.META.get('HTTP_AUTHORIZATION').replace("bearer ", "")
            accToken = AccessToken.objects.get(token=current_token)
            refTokensModel = RefreshToken.objects.filter(access_token=accToken.id)
            for refToken in refTokensModel.iterator():
                refToken.delete()
            accToken.revoke()
            return Response({'done':'no'},status=HTTPStatus.HTTP_200_OK)
        else:
            status_code = HTTPStatus.METHOD_NOT_ALLOWED
            response = JsonResponse({'success': 'false'},status=status_code)
            return response;