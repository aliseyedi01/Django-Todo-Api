from django.urls import path
from .views import CategoryView

urlpatterns = [
    path('', CategoryView.as_view(), name='category-list'),
    path('<uuid:pk>/', CategoryView.as_view(), name='category-detail'),
]
