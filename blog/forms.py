from django.contrib.auth.models import User

from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment

        fields = ['body']
        snippets = {
            'body':forms.Textarea(attrs={'class': 'form-control'}),
        }