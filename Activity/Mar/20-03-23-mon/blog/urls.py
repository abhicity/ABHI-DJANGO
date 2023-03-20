from django.urls import path
from .views import blog_list, blog_detail

urlpatterns = [
    path("", blog_list, name='list'),
    path("<int:id>", blog_detail, name='detail'),
]
