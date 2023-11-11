# from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from django.urls import path, re_path
from .views import TodoView, SignUpView, LoginView, LogoutView

urlpatterns = [
    path('task/', TodoView.as_view(), name='task-list'),
    path('task/<uuid:pk>/', TodoView.as_view(), name='task-detail'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]
