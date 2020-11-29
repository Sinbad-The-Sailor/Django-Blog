from django.urls import path
from .views import PostDeleteView, PostListView, PostDetailView, PostCreateView, PostUpdateView, CategoryCreateView, CategoryView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/edit/<int:pk>/', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:pk>/', PostDeleteView.as_view(), name='post-delete'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('category/new/', CategoryCreateView.as_view(), name='category-create'),
    path('about/', views.about, name='blog-about'),
    path('contact/', views.contact, name='blog-contact'),
    path('category/<str:cat>/', CategoryView, name = 'category-home'),
]
