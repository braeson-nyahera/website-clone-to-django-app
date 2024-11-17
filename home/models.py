from django.db import models

# Create your models here.
class Team(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    image = models.ImageField(upload_to='team/')

    def __str__(self):
        return self.name
    
class Testimonial(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    details = models.TextField()
    image = models.ImageField(upload_to='testimonials/')

    def __str__(self):
        return self.name
    
class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to= 'blog/')
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    comments = models.IntegerField()
    descripion = models.TextField()

    def __str__(self):
        return self.title