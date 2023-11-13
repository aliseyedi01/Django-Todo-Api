# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from accounts.permissions import IsAuthenticatedAndOwner
# django
from django.contrib.auth.models import User
from tasks.models import Category
from tasks.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class CategoryView(APIView):
    permission_classes = [IsAuthenticatedAndOwner]

    # Handle Get Single & All Categories
    def get(self, request, pk=None):
        if pk:
            try:
                category = Category.objects.get(uuid=pk)
                serializer = CategorySerializer(category)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Category.DoesNotExist:
                return Response({"error": f"Category with UUID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            categories = Category.objects.filter(user=request.user)
            serializer = CategorySerializer(categories, many=True)
            # user_tasks = Task.objects.filter(user=request.user)
            # serializer = TaskSerializer(user_tasks, many=True)
            return Response(serializer.data)

    # Handle Update Category
    def post(self, request):
        name = request.data.get('name')
        user = request.user
        if name is not None:
            # Check for existing category with the same name for the same user
            if Category.objects.filter(name=name, user=user).exists():
                return Response({"error": "A category with this name already exists for the user"}, status=status.HTTP_400_BAD_REQUEST)
            category = Category.objects.create(name=name, user=user)
            serializer = CategorySerializer(category)
            return Response({"message": "Category created successfully", "category": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "name is a required field"}, status=status.HTTP_400_BAD_REQUEST)

    # Handle Update Category
    def put(self, request, pk):
        category = Category.objects.get(uuid=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The category was successfully edited", "category": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle Remove Category
    def delete(self, request, pk):
        try:
            category = Category.objects.get(uuid=pk)
            category.delete()
            return Response({"Success": f"The category with name {category.name} was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": f"Category with ID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
