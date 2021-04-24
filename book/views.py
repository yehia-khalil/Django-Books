from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm,IsbnForm
from django.shortcuts import redirect
from .models import Book
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required

# Create your views here.

def index(request):
    books = Book.objects.all()
    # books = User.Books.all()
    return render(request, 'book/index.html', {"books": books})


@login_required
@permission_required('book.view_book')
def create(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'book/create.html', {'form': form})

def create_uuid(request):
    
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = IsbnForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            form.save()
            # redirect to a new URL:
            return redirect("index")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = IsbnForm()

    return render(request, 'book/create-uuid.html', {'form': form})


@login_required
@permission_required('book.view_book')
def show(request, num):
    books = Book.objects.get(id=num)
    return render(request, 'book/book.html', {"books": books})


def destroy(request, num):
    books = Book.objects.get(id=num)
    books.delete()
    return redirect("index")


def edit(request, num):
    books = Book.objects.get(id=num)
    form = NameForm(request.POST or None, instance=books)
    if form.is_valid():
        form.save()
        return redirect("index")

    return render(request, 'book/edit.html', {'form': form,'book':books})
