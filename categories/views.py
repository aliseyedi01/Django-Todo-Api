# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# apps
from accounts.permissions import IsAuthenticatedAndOwner
from tasks.serializers import CategorySerializer
from tasks.models import Category
# django
from django.urls import path
# swagger
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class CategoryListView(APIView):
    permission_classes = [IsAuthenticatedAndOwner]

    @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def get(self, request):
        categories = Category.objects.filter(user=request.user)
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    @swagger_auto_schema(
        responses={200: CategorySerializer(many=True)},
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'name': openapi.Schema(type=openapi.TYPE_STRING, description='Category title'),
            },
            required=['name']
        ),
    )
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


class CategoryDetailView(APIView):
    permission_classes = [IsAuthenticatedAndOwner]

    # @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def get(self, request, pk):
        try:
            category = Category.objects.get(uuid=pk)
            serializer = CategorySerializer(category)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Category.DoesNotExist:
            return Response({"error": f"Category with UUID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)

    # @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def put(self, request, pk):
        category = Category.objects.get(uuid=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "The category was successfully edited", "category": serializer.data})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # @swagger_auto_schema(responses={200: CategorySerializer(many=True)})
    def delete(self, request, pk):
        try:
            category = Category.objects.get(uuid=pk)
            category.delete()
            return Response({"Success": f"The category with name {category.name} was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": f"Category with ID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
