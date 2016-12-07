from django import forms
from django.db import models
from django.forms import ModelForm
from .models import Post
from django.core.exceptions import ObjectDoesNotExist
from django_summernote.widgets import SummernoteWidget


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'text_call', 'text_content', 'thumbnail']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control', 'widget': 'select'}),
            'text_call': forms.Textarea(attrs={'class': 'form-control', 'style': 'height: 100px;'}),
            'text_content': forms.TextInput(attrs={'class': 'form-control'}),
            'text_content': SummernoteWidget(),
        }
