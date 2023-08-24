from django.urls import path
from .views import student_list, student_detail
from .views_generic import *

urlpattern = [
    path('students', student_list),
    path('students/<int:pk>', student_detail),
    path('students', StudentList.as_view()),

]