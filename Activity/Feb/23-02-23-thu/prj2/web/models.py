from django.db import models

# Create your models here.
class StudentModel(models.Model):
    name = models.CharField(max_length=150)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.name