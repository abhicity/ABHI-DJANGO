from django.db import models

class CategoryModel(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name



class DishesModel(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(CategoryModel)

    def __str__(self):
        return self.name