from django.db import models

# Create your models here.
class project(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=30)

    def __str__(self):
        return self.name
    
class Brand(models.Model):
    name = models.CharField(max_length=15)
    description = models.TextField()
    logo = models.ImageField(upload_to='logos/')
    website = models.URLField(max_length=200)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=15)
    def __str__(self):
        return self.name
    
class designvisual(models.Model):
    name = models.CharField(max_length=15)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name