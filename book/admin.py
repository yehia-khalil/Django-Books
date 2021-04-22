from django.contrib import admin
from .models import *
from .forms import NameForm,IsbnForm

# Register your models here.
class BookInline(admin.TabularInline):
    model = Book

class BookAdmin(admin.ModelAdmin):
    form = NameForm
    list_display = ("description","price","isbn")
    list_filter  = ("categories",)
    search_fields = ("description", )


class IsbnAdmin(admin.ModelAdmin):
    inlines = [
        BookInline,
    ]
    form = IsbnForm
    list_display = ("book_title","isbn_number","author")
    search_fields = ("book_title", )
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Isbn,IsbnAdmin)