from django import forms
from .models import Book


class ExampleForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your name'})
    )
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'placeholder': 'Enter your message'}),
        required=True
    )


class SafeSearchForm(forms.Form):
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
    class Meta:
        model = Book
        fields = ['title', 'author', 'description']  # adjust if your model differs
