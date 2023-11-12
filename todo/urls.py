# from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, re_path
from .views import TodoView


urlpatterns = [
    path('', TodoView.as_view(), name='task-list'),
    path('<uuid:pk>/', TodoView.as_view(), name='task-detail'),
]
