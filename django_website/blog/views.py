from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post



# Create your views here.
def home(request):
    context = {
        'posts' : Post.objects.all() 
    }
    return render(request, 'blog/home.html', context)

def contact(request):
    return render(request, 'blog/contact.html')


# TODO: Change with new templates!
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

# TODO: Change with new templates!
class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content'] 
    
def about(request):
    return render(request, 'blog/about.html')