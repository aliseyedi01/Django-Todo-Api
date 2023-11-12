# django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
# drf
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken


class SignUpView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']

        if not username or not password or not email:
            return Response({'error': 'All fields must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        # Create a new user
        user = User.objects.create_user(username=username, email=email, password=password)

        # Log in the new user
        login(request, user)

        return redirect('login')


class LoginView(APIView):
    @method_decorator(csrf_exempt)
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']

        if not username or not password:
            return Response({'error': 'Username and password must be provided'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(request, username=username, password=password)
        if user is not None:
            # refresh = RefreshToken.for_user(user)
            # access_token = str(refresh.access_token)
            access_token = str(AccessToken.for_user(user))
            refresh_token = str(RefreshToken.for_user(user))

            return Response({'message': 'Login Successful', 'access_token': access_token, 'refresh_token': refresh_token}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful'}, status=status.HTTP_200_OK)
