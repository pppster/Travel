from typing import Any, Dict
from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'summary', 'content', ) # 'image'
        labels = {
            'title': '',
            'summary': '',
            'content': '',
            # 'image': '',
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add a Title'}),
            'summary': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter a short description'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter your content'}),
            # 'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': '',
        }
        
        widgets = {
            'text': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Leave your comment', 'width': '50%'}),
        }
