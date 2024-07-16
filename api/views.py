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
#User list
class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

#User update password
class UserUpdatePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request):
        user = request.user
        current_password = request.data.get('current_password')
        new_password = request.data.get('new_password')
        if not check_password(current_password, user.password):
            return Response({'error': 'Invalid password'}, status=status.HTTP_400_BAD_REQUEST)
        if len(new_password) < 8:
            return Response({'error': 'New password must be at least 8 characters long'}, status=status.HTTP_400_BAD_REQUEST)
        user.set_password(new_password)
        user.save()
        
        return Response({'message': 'Password updated successfully'}, status=status.HTTP_200_OK)
#Admin change employee role
class ChangeUserRoleView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.user.role not in ['admin', 'superadmin']:
            return Response(
                {'error': 'You are not authorized to change user roles.'},
                status=status.HTTP_403_FORBIDDEN
            )

        email = request.data.get('email')
        new_role = request.data.get('new_role')

        if not email or not new_role:
            return Response(
                {'error': 'Email and new role are required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if new_role not in ['admin', 'employee', 'superadmin']:
            return Response(
                {'error': 'Invalid role specified.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        user.role = new_role
        user.save()

        return Response(
            {'success': f'User role updated to {new_role}.'},
            status=status.HTTP_200_OK
        )
#delete a user from the database
class DeleteUserView(APIView):
    # Only authenticated users can access this view
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        # Check if the current user has the admin or superadmin role
        if request.user.role not in ['admin', 'superadmin']:
            return Response(
                {'error': 'You are not authorized to delete users.'},
                status=status.HTTP_403_FORBIDDEN
            )

        # Get the email from the request data
        email = request.data.get('email')

        # Check if email is provided
        if not email:
            return Response(
                {'error': 'Email is required.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        # Try to find the user with the provided email
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response(
                {'error': 'User not found.'},
                status=status.HTTP_404_NOT_FOUND
            )

        # Delete the user
        user.delete()

        # Return a success response
        return Response(
            {'success': 'User deleted successfully.'},
            status=status.HTTP_200_OK
        )