from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def blog_page(request):
    blogs = BlogModel.objects.all()
    data = {"blogs": blogs}
    return render(request, "blog.html", data)   

def blog_list_page(request):
    return render(request, "blog_list.html") 

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")