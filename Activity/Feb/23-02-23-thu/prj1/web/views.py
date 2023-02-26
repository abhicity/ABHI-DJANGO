from django.shortcuts import render
from .models import ProjectsModel

# Create your views here.
def home_page(request):
    data = {"page_name": "Home Page"}
    return render(request, "index.html", data)


def project_list(request):
    projects = ProjectsModel.objects.all().order_by("-id")
    data = {"projects": projects}
    return render(request, "projects.html", data)


def project_detail(request, id):
    project = ProjectsModel.objects.get(id=id)
    data = {"project": project}
    return render(request, "project_detail.html", data)
