from django.shortcuts import render
from .models import StudentsModel

# Create your views here.
def home_page(request):
    data = {"page_name": "Home Page"}
    return render(request, "index.html", data)

def students_list(request):
    students = StudentsModel.objects.all()
    data = {"students": students}
    return render(request, "students.html", data)