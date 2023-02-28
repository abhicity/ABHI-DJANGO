from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateField(auto_now_add=True)
    edited = models.DateField(auto_now=True)
    published = models.DateField()
    draft = models.BooleanField()

    def __str__(self):
        return self.title