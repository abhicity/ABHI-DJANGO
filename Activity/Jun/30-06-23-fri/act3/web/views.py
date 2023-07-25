from django.shortcuts import render
from django.urls import reverse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin


class HomePage(TemplateView):
    template_name = "web/index.html"

class AboutPage(LoginRequiredMixin, TemplateView):
    template_name = "web/about.html"

class ContactPage(LoginRequiredMixin, TemplateView):
    template_name = "web/contact.html"



class BlogPage(LoginRequiredMixin, TemplateView):
    template_name = "web/blog.html"

class UserCreate(CreateView):
    form_class = UserCreationForm
    template_name = "web/register.html"

    def get_success_url(self):
        return reverse("web:login")