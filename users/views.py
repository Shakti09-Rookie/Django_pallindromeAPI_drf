from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializer import UserSerializer, LoginSerializer
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from rest_framework import generics

# Create your views here.
class RegisterAPI(generics.CreateAPIView):
    serializer_class = UserSerializer

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username=serializer.data['username'])
            refresh = RefreshToken.for_user(user)
            return Response({
                'status' : 200,
                'data' : serializer.data,
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
                'message' : "Registration Successfull",
            })
        return Response({
            'status' : 400,
            'message' : 'Something went wrong',
            'data' : serializer.errors,
        })

class LoginAPI(generics.CreateAPIView):

    serializer_class = LoginSerializer

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            username = serializer.data['username']
            password = serializer.data['password']

            user = authenticate(username=username, password=password)
            if user is None:
                return Response({
                    'status' : 400,
                    'message' : 'Credentials Invalid',
                })

            refresh = RefreshToken.for_user(user)    
            return Response({
                'refresh' : str(refresh),
                'access' : str(refresh.access_token),
            })

        return Response({
            'status' : 400,
            'message' : 'Something went wrong',
            'data' : serializer.errors
        })

class UseropAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self,request):
        data= request.data
        user_id=request.user.id
        user = User.objects.get(id=user_id)
        user.password = make_password(data['password'])
        user.first_name = data['first_name']
        user.last_name = data['last_name']
        user.save()
        return Response({
            'message': 'Details Updated'
        })

    def delete(self,request):
        user_id=request.user.id
        user = User.objects.get(id=user_id)
        user.delete()
        return Response({
                    'message' : "User Removed"
                })