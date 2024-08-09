from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
class Post(models.Model):
    STATUS = (
        ('0', 'Draft'),
        ('1', 'Publish'),
    )
    title = models.CharField(max_length=100)
    title_tag = models.CharField(max_length=100,default="My Blog")
    body = models.TextField()
    status = models.CharField(choices=STATUS,max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User,related_name='blog_posts')

    def total_likes(self):
        return self.likes.count()

    
    def __str__(self) -> str:return self.title +'|'+ str(self.author)

    def get_absolute_url(self):
        return reverse('home')
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Comment by {self.user.username} on {self.post.title}'

# Create your models here.
