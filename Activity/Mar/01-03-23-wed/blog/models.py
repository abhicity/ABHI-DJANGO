from django.db import models

# Create your models here.
class PystringModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    post_date = models.DateField()
    publish = models.BooleanField()



class PydictModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    post_date = models.DateField()
    publish = models.BooleanField()



class PytupleModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    edited = models.DateTimeField(auto_now=True)
    post_date = models.DateField()
    publish = models.BooleanField()

    def __str__(self):
        return self.title