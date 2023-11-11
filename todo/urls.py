from django.urls import path
from .views import TodoView

urlpatterns = [
    path('task/', TodoView.as_view()),
    path('task/<uuid:pk>/', TodoView.as_view()),
]
