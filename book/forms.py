from django.forms import ModelForm
from.models import Book, Isbn
from django.core.exceptions import ValidationError


class NameForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


        
class IsbnForm(ModelForm):
    class Meta:
        model = Isbn
        fields = '__all__'

    def clean_book_title(self):
        title = self.cleaned_data.get("book_title")
        if len(title) < 10 or len(title) > 50 : 
            raise ValidationError("title must be between 10 and 50 chars")
        print(title)
        return title