from django.contrib import admin
from django.urls import path, include
from web.views import (
    home_page,
    about_page,
    contact_page,
    blog_list,
    add_blog,
    contact_page,
    edit_blog,
    delete_blog,
    detail_blog,
)
from students.views import (
    search_students,
    students_list,
    add_student,
    save_student,
    post_save_student,
    post_add_student,
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home_page, name="home"),
    path("search/", search_students, name="search"),
    path("students/", students_list, name="list"),
    path("students/add/", add_student, name="add"),
    path("students/post_add/", post_add_student, name="post_add"),
    path("students/add/save/", save_student, name="save"),
    path("students/post_add/save/", post_save_student, name="post_save"),
    # BLogs
    path("blogs/", blog_list, name="blog_list"),
    path("blogs/add/", add_blog, name="blog_add"),
    path("blogs/edit/<int:id>/", edit_blog, name="edit_blog"),
    path("blogs/<int:id>/", detail_blog, name="detail_blog"),
    path("blogs/delete/<int:id>/", delete_blog, name="delete_blog"),
    #path("", include(("course.urls", "course"), namespace="course")),
    path("about/", about_page, name="about"),
    path("contact/", contact_page, name="contact"),
]