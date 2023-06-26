from django.shortcuts import render
from django.views.generic import CreateView
from django.views.generic.list import ListView
from .models import DishesModel, CategoryModel



class DishesList(ListView):
    model = DishesModel
    fields = "__all__"
    template_name = "dishes/list.html"
    context_object_name = "dishes"

class DishesCreate(CreateView):
    model = DishesModel
    fields = "__all__"
    template_name = "dishes/add.html"
    context_object_name = "dishes"
    #success_url = "/"














