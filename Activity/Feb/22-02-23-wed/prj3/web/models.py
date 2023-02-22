from django.db import models

# Create your models here.
class EmployesModel(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=20)

class EmployesModel2(models.Model):
    name = models.CharField(max_length=50)
    emp_id = models.CharField(max_length=20)


    def __str__(self):
        return self.name