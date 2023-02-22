from django.shortcuts import render
from .models import EmployesModel, EmployesModel2

# Create your views here.
def home_page(request):
    data = {"page_name": "Welcome to Home Page"}
    return render(request, "index.html", data)

def employes_list(request):
    employes = EmployesModel.objects.all()
    data = {"employes": employes}
    return render(request, "employes.html", data)

def employes_list(request):
    employes = EmployesModel2.objects.all()
    data = {"employes": employes}
    return render(request, "employes.html", data)