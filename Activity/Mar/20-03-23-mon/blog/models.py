from django.db import models
from PIL import image

# Create your models here.
class CategoryModel(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class BlogModel(models.Model):
    title = models.CharField(max_length=300)
    image = models.ImageField(default="blog/default.jpg", upload_to="blog/")
    content = models.TextField()
    doc = models.DateTimeField(auto_now_add=True)
    doe = models.DateField(auto_now=True)
    dop = models.DateField(verbose_name="Publish Date")
    published = models.BooleanField(default=False)
    category = models.ManyToManyField(CategoryModel)

    def __str__(self):
        return self.title


    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        print("im running the save method inside model")
        img = Image.open(self.image)
        print("width:", img.width)
        print("height:",img.height)