from django.shortcuts import render
from .models import BlogModel

# Create your views here.
def blog_list(request):
    blogs = BlogModel.objects.all()
    data = {"blogs": blogs}
    return render(request, "blog/list.html", data)


def blog_detail(request, id):
    blog = BlogModel.objects.get(id=id)
    data = {"blog": blog}
    return render(request, "blog/detail.html", data)