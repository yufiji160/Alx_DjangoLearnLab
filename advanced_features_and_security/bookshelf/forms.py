from django import forms
from .models import Book

class SafeSearchForm(forms.Form):
    q = forms.CharField(
        required=False,
        max_length=200,
        strip=True,
        widget=forms.TextInput(attrs={"placeholder": "Search books..."}),
    )

    def clean_q(self):
        data = self.cleaned_data.get("q", "")
        return data

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["title", "author", "description"]

