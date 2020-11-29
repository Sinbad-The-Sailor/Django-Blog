from django import forms
from django.forms import widgets
from .models import Post, Category

choices = Category.objects.all().values_list('name', 'name')

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'preview', 'content',]
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control',}),
            'author' : forms.Select(attrs={'class': 'form-control',}),
            'category' : forms.Select(choices = choices, attrs={'class': 'form-control',}),
            'preview' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control',}),
        }

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'preview', 'content',]
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control',}),
            'category' : forms.Select(choices = choices, attrs={'class': 'form-control',}),
            'preview' : forms.TextInput(attrs={'class': 'form-control'}),
            'content' : forms.Textarea(attrs={'class': 'form-control',}),
        }