from rest_framework import serializers
from ..user import User


class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name','email','phone_no','gender','password']

