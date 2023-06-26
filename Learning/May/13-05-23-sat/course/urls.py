from django.urls import path
from .views import CourseList, CourseDetail, CourseCreate, CourseUpdate, CourseDelete


urlpatterns = [
    path("", CourseList.as_view(), name="list"),
    path("<int:pk>/", CourseDetail.as_view(), name="course_detail"),
    path("new/", CourseCreate.as_view(), name="add"),
    
    
    
    path("update/<int:pk>/", CourseUpdate.as_view(), name="update"),
    path("delete/<int:pk>/", CourseDelete.as_view(), name="delete"),

]
