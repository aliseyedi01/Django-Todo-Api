
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from tasks.models import Category
from tasks.serializers import CategorySerializer
from rest_framework.permissions import IsAuthenticated


class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

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
            categories = Category.objects.all()
            serializer = CategorySerializer(categories, many=True)
            return Response(serializer.data)

    # Handle Create Category
    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle Update Category
    def put(self, request, pk):
        category = Category.objects.get(uuid=pk)
        serializer = CategorySerializer(category, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Handle Remove Category
    def delete(self, request, pk):
        try:
            category = Category.objects.get(uuid=pk)
            category.delete()
            return Response({"Success": "The category was successfully deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": f"Category with ID {pk} not found"}, status=status.HTTP_404_NOT_FOUND)
