# serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User  # Import your custom User model

from rest_framework import serializers
from .models import User

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'email', 'password', 'phone_number', 'notification_preference']
        extra_kwargs = {'password': {'write_only': True}}  # Hide password in responses

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data.get('phone_number', ''),
            notification_preference=validated_data.get('notification_preference', 'email'),
            password=validated_data['password']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
