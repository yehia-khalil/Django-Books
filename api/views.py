from django.shortcuts import render
from book.models import Book
from .serializers import BookSerializer, UserSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

# Create your views here.


@api_view(['GET'])
# @permission_classes([IsAuthenticated])
def index(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def add(request):
    print("inside add inside api views")
    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "Data added successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "Data not added", "errors": serializer.errors}, status=400)

@api_view(['POST'])
def signup(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        username = form.validated_data.get('username')
        raw_password = form.validated_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(request, user)
        return Response({"message": "signed up successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
    return Response({"message": "signing up failed", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
