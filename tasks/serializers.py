from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Task
from .models import Category
from rest_framework import serializers


# Category
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'uuid', 'user')

    def to_representation(self, instance):
        return {'uuid': instance.uuid, 'name': instance.name, 'user': instance.user.username}


# User
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def validate(self, data):
        # Validate email
        email = data.get('email')
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'email': 'Email already exists'})

        return data

    def to_representation(self, instance):
        return {'id': instance.id, 'username': instance.username}


# Task
class TaskSerializer(ModelSerializer):
    category = CategorySerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Task
        fields = '__all__'
