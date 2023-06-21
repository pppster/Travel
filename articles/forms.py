from typing import Any, Dict
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'title-input'}),
        #     'content': forms.TextInput(attrs={'class': 'content-input'}),
        # }

    def clean(self):
        data = self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains=title)
        if qs.exists():
            self.add_error('title', f'The title "{title}" is already taken')
        return data
