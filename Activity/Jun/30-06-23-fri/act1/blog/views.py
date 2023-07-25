from django.shortcuts import render
from .models import SocialMedia
from django.views.generic.list import ListView

class SocialMediaList(ListView):
    model = SocialMedia
    template_name = "blog/list.html"
    context_object_name = "links"
