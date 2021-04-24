from django.urls import path, include
from django.contrib.auth.models import User
from book.models import Book, Isbn
from rest_framework import routers, serializers, viewsets, generics

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def delete(self):
        id = self.data.get('id')
        book = Book.objects.get(pk=id)
        book.delete()


class IsbnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Isbn
        fields = ['description', 'price', 'isbn_id', ]


class UserSerializer(serializers.ModelSerializer):
    # password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User;
        fields = ['username', 'email','password']

        
    def save(self):
        user = User(
            email=self.validated_data.get('email'),
            username=self.validated_data.get('username')
        )
    
        user.set_password(self.validated_data.get('password'))
        user.save()
