from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import check_password
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404

User = get_user_model()
# Create your views here.
"""                                     USER VIEWS                                                                      """
#user registration
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#User log in view
class UserLoginView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(request, email=email, password=password)
        
        if user is not None:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if not created:
                token.delete()
                token = Token.objects.create(user=user)
                
            response_data = {
                'message': 'User logged in successfully',
                'email': user.email,
                'token': token.key
            }
            return Response(response_data, status=status.HTTP_200_OK)
        else:
            return Response(
                {'error': 'Invalid email and/or password'},
                status=status.HTTP_401_UNAUTHORIZED
            )