from django.shortcuts import render
from django.views.generic import TemplateView



# FUNCTION BASED VIEWS
# def home_page(request):
#     context = {}
#     return render(request, 'web/index.html', context)

# def about_page(request):
#     context = {}
#     return render(request, 'web/about.html', context)

# def contact_page(request):
#     context = {}
#     return render(request, 'web/contact.html', context)




# CLASS BASED VIEWS
class HomePage(TemplateView):
    template_name = "web/index.html"
    extra_context = {}

class AboutPage(TemplateView):
    template_name = "web/about.html"
    extra_context = {}

class ContactPage(TemplateView):
    template_name = "web/contact.html"
    extra_context = {}