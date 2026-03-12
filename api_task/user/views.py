from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password,check_password
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    data = request.data
    user = User.objects.create(
        name = data['name'],
        email = data['email'],
        password_hash=make_password(data['password']),
        role = data['role']
    )

    return Response({
        "userId": user.id,
        "message": "User Created"
    })


@api_view(['POST'])
def login(request):
    email = request.data['email']
    password = request.data['password']

    try:
        user = User.objects.get(email=email)
    except:
        return Response({"error": "User not Found "}, status=404)
    
    if not check_password(password, user.password_hash):
        return Response({"error": "Invalid Password"}, status=401)
    
    refresh = RefreshToken.for_user(user)

    return Response({
        "token": str(refresh.access_token),
        "user": {
            "id": user.id,
            "name": user.name,
            "role": user.role
        }
    })


# Create your views here.
