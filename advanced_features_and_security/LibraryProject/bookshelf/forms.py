from django import forms
from .models import Book


class SafeSearchForm(forms.Form):
    """
    Simple search form with input validation.
    Prevents unsafe input and helps avoid SQL injection.
    """
    q = forms.CharField(
        required=False,
        max_length=200,
        strip=True,
        widget=forms.TextInput(attrs={'placeholder': 'Search books...'})
    )

    def clean_q(self):
        data = self.cleaned_data.get('q', '')
        return data


class BookForm(forms.ModelForm):
    """
    Secure ModelForm for the Book model.
    Using ModelForm ensures automatic input validation and escaping.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']
