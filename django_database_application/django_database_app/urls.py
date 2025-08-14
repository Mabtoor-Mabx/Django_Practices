from django.urls import path
from . import views

urlpatterns = [
    path('', views.Student_list, name = 'student_list')
]
