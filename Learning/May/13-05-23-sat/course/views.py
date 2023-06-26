from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import CourseModel

class CourseList(ListView):
    model = CourseModel
    template_name = 'coursemodel_list.html'
    ordering = "-id"
    context_object_name = 'courses'

class CourseDetail(DetailView):
    model = CourseModel
    template_name = 'course/coursemodel_detail.html'
    context_object_name = 'course'


class CourseCreate(CreateView):
    model = CourseModel
    fields = "__all__"
    # template_name = "course/add.html"
    success_url = "/"

class CourseUpdate(UpdateView):
    model = CourseModel
    template_name = "course/coursemodel_update.html"
    fields = "__all__"
    success_url = reverse_lazy("course:list")

class CourseDelete(DeleteView):
    model = CourseModel
    template_name = "course/coursemodel_delete.html"
    success_url = reverse_lazy("course:list")
