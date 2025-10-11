from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
      model = Comment
      fields = ['content']
      widgets = {
      'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Write your comment...'}),
}


    def clean_content(self):
         data = self.cleaned_data.get('content', '').strip()
         if not data:
            raise forms.ValidationError('Comment cannot be empty.')
         if len(data) > 2000:
             raise forms.ValidationError('Comment is too long (max 2000 characters).')
         return data