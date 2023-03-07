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
    return render(request, "blog/dict_list.html", data)

def dict_detail(request, id):
    pydictmethods_content = PydictModel.objects.get(id=id)
    data = {"pydictmethods_content": pydictmethods_content}
    return render(request, "blog/dict_detail.html", data)

def tuple_list(request):
    pytuplemethods_title = PytupleModel.objects.all()
    data = {"pytuplemethods_title": pytuplemethods_title}
    return render(request, "blog/tuple_list.html", data)

def tuple_detail(request, id):
    pytuplemethods_content = PytupleModel.objects.get(id=id)
    data = {"pytuplemethods_content": pytuplemethods_content}
    return render(request, "blog/tuple_detail.html", data)

def search(request):
    query = request.GET['query']
    #abhi = PystringModel.objects.all()
    abhi = PystringModel.objects.filter(title__icontains=query)
    #.values()
    data = {"abhi": abhi}
    return render(request, "blog/list.html", data)

    #def search_blogs(request):
#    return render(request, "blog/list.html" )



    #abhi = PystringModel.objects.all()