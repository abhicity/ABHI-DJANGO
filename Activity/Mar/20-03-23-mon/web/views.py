from django.shortcuts import render

# Create your views here.
def home_page(request):
    data = {}
    return render(request, 'index.html', context=data)