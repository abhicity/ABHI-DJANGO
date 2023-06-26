# from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View



# def home_page(request):
#     data = {}
#     return render(request, 'home.html', context=data)


class HomePage(TemplateView):
    template_name = "web/home.html"
    extra_context = {"name": "ASDF"}
