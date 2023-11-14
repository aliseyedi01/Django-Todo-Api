# from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, re_path
from .views import TodoListView, TodoDetailView


urlpatterns = [
    path('', TodoListView.as_view(), name='task-list'),
    path('<uuid:pk>/', TodoDetailView.as_view(), name='task-detail'),
]
