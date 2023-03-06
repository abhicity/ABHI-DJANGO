from django.urls import path
from .views import blog_list, blog_detail, dict_list, dict_detail, tuple_list, tuple_detail

app_name = "blog"

urlpatterns = [
    path("", blog_list, name="list"),
    path("<int:id>/", blog_detail, name="detail"),
    path("dict/", dict_list, name="dict_list"),
    path("<int:id>/", dict_detail, name="dict_detail"),
    path("tuple/", tuple_list, name="tuple_list"),
    path("<int:id>/", tuple_detail, name="tuple_detail"),
]