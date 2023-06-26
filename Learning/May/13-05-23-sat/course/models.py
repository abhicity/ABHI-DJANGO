from django.db import models

class CourseModel(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    branch = models.CharField(max_length=50)
    hrs = models.IntegerField(verbose_name="Duration")

    def __str__(self):
        return str(self.name)