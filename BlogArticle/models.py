from django.db import models
from django.contrib.auth.models import User

from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.

class category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) -> str:
        return self.name
    
    def get_absolute_url(self):
        
        return reverse('homePage')
     
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    bio = models.TextField()
    profile_pic = models.ImageField(null=True, blank=True, upload_to='photos/profile/')
    
    def __str__(self):
        return str(self.user)
           

class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='article tag')
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    #body = models.TextField()
    post_date = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default='category of article')
    likes = models.ManyToManyField(User, related_name='other_like')
    
    def total_likes(self):
        return self.likes.count()
    
    def __str__(self) -> str:
        return self.title +' | '+ str(self.author)
    
    def get_absolute_url(self):
        return reverse('detile-post', kwargs={'pk': self.pk})
    
class comment(models.Model):
    post = models.ForeignKey(Post,related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    email = models.EmailField(null=True)
    date_add = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s-%s' % (self.post.title, self.name)