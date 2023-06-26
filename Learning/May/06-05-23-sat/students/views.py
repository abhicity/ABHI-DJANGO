from django.shortcuts import render, redirect
from .models import StudentModel


def search_students(request):
    # name = request.GET.get("name", "Skill")
    data = request.GET
    # data = name.upper()
    context = {"data": data}
    return render(request, "students/search.html", context=context)


def students_list(request):
    students = StudentModel.objects.all()
    context = {"students": students}
    return render(request, "students/list.html", context=context)


def add_student(request):
    return render(request, "students/add.html")


def post_add_student(request):
    return render(request, "students/post_add.html")


def save_student(request):
    name = request.GET.get("name", "")
    phone = request.GET.get("number", "")
    email = request.GET.get("email", "")

    obj = StudentModel.objects.create(name=name, phone=phone, email=email, active=True)
    obj.save()
    students = StudentModel.objects.all()
    context = {"students": students}
    # return render(request, 'students/list.html', context=context)
    return redirect("list")


def post_save_student(request):
    if request.method == "POST" and request.user.is_authenticated:
        name = request.POST.get("name")
        phone = request.POST.get("number")
        email = request.POST.get("email")

        obj = StudentModel.objects.create(
            name=name, phone=phone, email=email, active=True
        )
        obj.save()
        students = StudentModel.objects.all()
        context = {"students": students}
        # return render(request, 'students/list.html', context=context)
        return redirect("list")
    else:
        return redirect("home")
