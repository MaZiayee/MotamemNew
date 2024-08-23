from django.db import models

# Create your models here.

class Customer(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)

    
    def __str__(self):
        return "{} - {}".format(self.id,self.title)
    
    
class Service(models.Model):
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    list_detail = models.JSONField()

    
    def __str__(self):
        return "{} - {}".format(self.id,self.title)
    

class FAQ(models.Model):
    question = models.CharField(max_length=300)
    answer = models.TextField()

    
    def __str__(self):
        return "{} - {}".format(self.id,self.question)

class Message(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    title = models.CharField(max_length=250)
    message_field = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return "{} - {} - {}".format(self.id,self.name,self.phone)    