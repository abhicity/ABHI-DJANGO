from django.shortcuts import render
from .models import PystringModel, PydictModel, PytupleModel

# Create your views here.
def blog_list(request):
    pystringmethodstitle = PystringModel.objects.all()
    data = {"pystringmethodstitle": pystringmethodstitle}
    return render(request, "blog/list.html", data)

def blog_detail(request, id):
    pystringmethodscontent = PystringModel.objects.get(id=id)
    data = {"pystringmethodscontent": pystringmethodscontent}
    return render(request, "blog/detail.html", data)

def dict_list(request):
    pydictmethods_title = PydictModel.objects.all()
    data = {"pydictmethods_title": pydictmethods_title}
    return render(request, data)

def dict_detail(request, id):
    pydictmethods_content = PydictModel.objects.get(id=id)
    data = {"pydictmethods_content": pydictmethods_content}
    return render(request, data)

def tuple_list(request):
    pytuplemethods_title = PytupleModel.objects.all()
    data = {"pytuplemethods_title": pytuplemethods_title}
    return render(request, data)

def tuple_detail(request, id):
    pytuplemethods_content = PytupleModel.objects.get(id=id)
    data = {"pytuplemethods_content": pytuplemethods_content}
    return render(request, data)