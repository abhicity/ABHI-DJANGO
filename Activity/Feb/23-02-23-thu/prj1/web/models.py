from django.db import models

# Create your models here.
class ProjectsModel(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.title
