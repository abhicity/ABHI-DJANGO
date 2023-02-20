from django.shortcuts import render

# Create your views here.
def student_list(request):
    students = PersonalModel.objects.all()
    data = {"students": students}
    return render(request, "s_list.html", data)