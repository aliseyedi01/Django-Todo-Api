from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Task, Category
from django.contrib.auth.models import User
from .serializers import TaskSerializer
from django.core.exceptions import ObjectDoesNotExist


class TodoView(APIView):
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
