from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import Task
from .models import Category


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'uuid')

    def to_representation(self, instance):
        return {'uuid': instance.uuid, 'name': instance.name}


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('username', 'id')
        fields = ['id', 'username', 'password', 'email']

    def to_representation(self, instance):
        return {'id': instance.id, 'username': instance.username}


class TaskSerializer(ModelSerializer):
    category = CategorySerializer(required=False)
    user = UserSerializer(required=False)

    class Meta:
        model = Task
        fields = '__all__'
