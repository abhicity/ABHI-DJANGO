from django.db import models

# Create your models here.
class StudentsModel(models.Model):
    name = models.CharField(max_length=50)
    reg_no = models.CharField(max_length=20)
    education = models.CharField(max_length=30)


    def __str__(self):
        return self.name