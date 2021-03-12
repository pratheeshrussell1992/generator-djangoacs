from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
import rest_framework.status
from rest_framework.response import Response


from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema
from drf_yasg.utils import swagger_auto_schema


@csrf_exempt
@permission_classes((AllowAny,))
    @swagger_auto_schema(operation_description="Login REQUEST",responses={404: 'unauthorized',200:'message'},
    request_body=openapi.Schema(
    type=openapi.TYPE_OBJECT, 
    properties={
        'username': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
        'password': openapi.Schema(type=openapi.TYPE_STRING, description='string'),
    }))
@api_view(["POST"])
def oauthLogin(request):
    if request.method == "POST":
        username = request.data.get("username")
        password = request.data.get("password")
        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'},status=HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if not user:
            return Response({'error': 'Invalid Credentials'},status=HTTP_404_NOT_FOUND)
        token, _ = Token.objects.get_or_create(user=user)
        return Response({'token': token.key},status=HTTP_200_OK)
    else:
        status_code = HTTPStatus.METHOD_NOT_ALLOWED
        response = JsonResponse({'success': 'false'},status=status_code)
        return response;