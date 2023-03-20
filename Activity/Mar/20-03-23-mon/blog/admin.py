from django.contrib import admin
from .models import BlogModel, CategoryModel

# Register your models here.



admin.site.register(BlogModel)
admin.site.register(CategoryModel)