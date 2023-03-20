from django.shortcuts import render
from .models import BlogModel, CategoryModel

# Create your views here.
def blog_list(request):
    blogs = BlogModel.objects.filter(published=True)
    data = {"blogs":blogs}
    return render(request, 'blog/list.html', context=data)

def blog_detail(request, id):
    blog = BlogModel.objects.get(id=id)
    data = {"blog":blog}
    return render(request, 'blog/detail.html', context=data)