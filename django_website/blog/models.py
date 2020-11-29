from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default='sinbad-the-sailor')
    category = models.CharField(max_length=100, default='uncategorized')
    preview = models.CharField(max_length=100, default=' ')

    def get_absolute_url(self):
        return reverse('post-detail', args=str(self.id))