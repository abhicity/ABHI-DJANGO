from django.db import models

class StudentModel(models.Model):
    name = models.CharField(max_length=250)
    phone = models.IntegerField()
    email = models.EmailField()
    active = models.BooleanField()

    def __str__(self):
        return self.name