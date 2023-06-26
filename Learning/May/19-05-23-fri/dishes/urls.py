from django.urls import path
from .views import DishesCreate, DishesList

urlpatterns = [
    path("", DishesList.as_view(), name='list'),
    path("add/", DishesCreate.as_view(), name='add'),


]
