from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('students',views.students,name='students'),
    path('save',views.save,name='save'),
    path('details',views.det,name='det')
]