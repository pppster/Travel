from typing import Any, Dict
from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', 'summary', 'content')
        labels = {
            'title': '',
            'summary': '',
            'content': '',
        }
        
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Add a Title'}),
            'summary': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a short description'}),
            'content': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter your content'}),
        }
