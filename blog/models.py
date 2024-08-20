from django.db import models
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True) 
    # tag
    category= models.ForeignKey('Category',on_delete=models.SET_NULL,null=True)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return "{} - {}".format(self.id,self.title)
    

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return "{} - {}".format(self.id,self.name)