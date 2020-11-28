from django import forms
from django.forms import widgets
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control',}),
            'content' : forms.Textarea(attrs={'class': 'form-control',}),
            'author' : forms.Select(attrs={'class': 'form-control',}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control',}),
            'content' : forms.Textarea(attrs={'class': 'form-control',}),
        }