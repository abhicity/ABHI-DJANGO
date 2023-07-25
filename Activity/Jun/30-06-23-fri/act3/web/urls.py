from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import HomePage, AboutPage, ContactPage, UserCreate, BlogPage

urlpatterns = [
    path("", HomePage.as_view(), name="home"),
    path("about", AboutPage.as_view(), name="about"),
    path("contact", ContactPage.as_view(), name="contact"),
    path("accounts/login/", LoginView.as_view(template_name="web/login.html"), name="login"),
    path("login/", LogoutView.as_view(template_name="web/logout.html"), name="logout"),
    path("register/", UserCreate.as_view(), name="register"),
    path("blog/", BlogPage.as_view(), name="blog"),
]
