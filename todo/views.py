from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .models import Task, Category
from .serializers import TaskSerializer, CategorySerializer, UserSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class SignUpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Log in the new user
        login(request, user)

        return redirect('login')


class LoginView(APIView):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request):
        # Handle GET request for signup view (if needed)
        return HttpResponse("Signup view accessed with GET request")

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)


class TodoView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # Handle Get Single & All Tasks
    def get(self, request, pk=None):
        if pk:
            try:
                task = Task.objects.get(uuid=pk)
                serializer = TaskSerializer(task)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Task.DoesNotExist:
                return Response({"error": f"Task with UUID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            get_tasks = Task.objects.all()
            serializer = TaskSerializer(get_tasks, many=True)
            return Response(serializer.data)

    # Handle Create Task
    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        print('after serializer')
        if serializer.is_valid():
            print('valid data')
            serializer.save()
            print('valid save')
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print('not valid data')
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle Update Task
    def put(self, request, pk):
        task = Task.objects.get(uuid=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)

        # Check if the specified category exists
        category = request.data.get('category', None)
        if category is not None:
            category_exists = Category.objects.filter(name=category).exists()
            if not category_exists:
                return Response({"error": f"Category with name {category} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            task.category = Category.objects.get(name=category)

        # Check if the specified user exists
        user = request.data.get('user', None)
        if user is not None:
            user_exists = User.objects.filter(username=user).exists()
            if not user_exists:
                return Response({"error": f"User with username {user} does not exist"}, status=status.HTTP_400_BAD_REQUEST)
            task.user = User.objects.get(username=user)

        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle Remove Task
    def delete(self, request, pk):
        try:
            task = Task.objects.get(uuid=pk)
            task.delete()
            return Response({"Success": "The post was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({"error": f"Task with ID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
