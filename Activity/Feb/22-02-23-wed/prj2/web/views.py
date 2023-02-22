from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def home_page(request):
    data = {"page_name": "Welcome to Abhi iBlog"}
    return render(request, "index.html", data)

def blog_list(request):
    blog = BlogModel.objects.all()
    data = {"blog": blog}
    return render(request, "blog.html", data)