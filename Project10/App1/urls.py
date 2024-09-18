from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.employee),
    path('emp/<int:id>', views.employee_id, name='employee-detail'),  #
    
]