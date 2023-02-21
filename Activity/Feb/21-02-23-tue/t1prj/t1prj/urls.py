"""t1prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web.views import home_page, blog_page, blog_list_page, about_page, contact_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home_page, name="home"),
    path("blog/", blog_page, name="blog"),
    path("blog_list/", blog_list_page, name="blog_list"),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
]
