from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Isbn(models.Model):
    book_title = models.CharField(max_length=50,default="batates")
    isbn_number = models.UUIDField(default = uuid.uuid4)
    author = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Books", default=1)

    def __str__(self):
        return f"{self.isbn_number}"


class Book(models.Model):
    description = models.TextField(max_length=1024)
    price = models.IntegerField()
    categories = models.ManyToManyField(Category)
    isbn = models.OneToOneField(Isbn, on_delete=models.CASCADE)
    # author_id = models.ForeignKey(User,on_delete=models.CASCADE, related_name="Books", default=1)

    def __str__(self):
        return self.isbn.book_title

