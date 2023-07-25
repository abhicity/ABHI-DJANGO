from django.urls import path
from .views import SocialMediaList

urlpatterns = [
    path("", SocialMediaList.as_view(), name="list"),
]