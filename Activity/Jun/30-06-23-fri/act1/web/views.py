from django.shortcuts import render
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'web/index.html'

class AboutPage(TemplateView):
    template_name = 'web/about.html'

class ContactPage(TemplateView):
    template_name = 'web/contact.html'