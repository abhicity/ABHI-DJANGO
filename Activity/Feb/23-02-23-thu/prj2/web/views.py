from django.shortcuts import render
from .models import StudentModel

# Create your views here.
def home_page(request):
    return render(request, "index.html")

def student_list(request):
    students = StudentModel.objects.all()
    data = {"students": students}
    return render(request, "students.html", data)


def student_detail(request, id):
    student = StudentModel.objects.get(id=id)
    data = {"student": student}
    return render(request, "student.html", data)