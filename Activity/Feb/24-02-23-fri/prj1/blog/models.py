from django.db import models

# Create your models here.
class BlogModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title