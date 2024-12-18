from django.db import models

class BlogModel(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    publish = models.BooleanField(default=True)
    dop = models.DateField()

    def __str__(self):
        return self.title