from django.shortcuts import render, redirect, get_object_or_404
from .models import BlogModel
from .forms import BlogForm, ContactForm


def home_page(request):
    return render(request, "home.html")


def blog_list(request):
    blogs = BlogModel.objects.all()
    return render(request, "list.html", {"blogs": blogs})


def add_blog(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        # print(forms)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm()
    context = {"form": form}
    return render(request, "common_form.html", context)


def detail_blog(request, id):
    # blog = BlogModel.objects.get(id=id)
    blog = get_object_or_404(BlogModel, id=id)
    context = {"blog": blog}
    return render(request, "detail.html", context=context)


def edit_blog(request, id):
    blog = BlogModel.objects.get(id=id)
    if request.method == "POST":
        form = BlogForm(request.POST, instance=blog)
        if form.is_valid():
            form.save()
            return redirect("blog_list")
    else:
        form = BlogForm(instance=blog)
    context = {"form": form, "blog": blog}
    return render(request, "common_form.html", context=context)


def delete_blog(request, id):
    blog = BlogModel.objects.get(id=id)
    if request.method == "POST":
        blog.delete()
        return redirect("blog_list")
    else:
        context = {"blog": blog}
        return render(request, "delete_blog.html", context)


def contact_page(request):
    contact = ContactForm()
    return render(request, "contact.html", {"form": contact})




#########################################
def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")