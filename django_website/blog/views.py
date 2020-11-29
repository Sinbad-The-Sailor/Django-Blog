from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Category, Post
from .forms import PostForm, UpdateForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'

class PostUpdateView(UpdateView):
    model = Post
    form_class = UpdateForm
    template_name = 'blog/post_update.html'
           
class PostDeleteView(DeleteView):
    model = Post
    template_name = 'blog/post_delete.html' 
    success_url = reverse_lazy('blog-home')       

class CategoryCreateView(CreateView):
    model = Category
    template_name = 'blog/category_form.html' 
    fields = '__all__'  
    success_url = reverse_lazy('blog-home')

def CategoryView(request, cat):
    posts = Post.objects.filter(category = cat.replace('-', ' '))
    return render(request, 'blog/category.html', {'cat' : cat, 'posts' : posts, })

def about(request):
    return render(request, 'blog/about.html')

def contact(request):
    return render(request, 'blog/contact.html')