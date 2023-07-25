from django.db import models
from PIL import Image


class SocialMedia(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to="img/", blank=True)
    url = models.URLField(max_length=300)

    def __str__(self):
        return self.name