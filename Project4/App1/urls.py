from django.urls import path
from . import views

urlpatterns = [
    path('reg', views.register, name='reg'),
    path('save',views.save,name='save'),
    path('det ',views.det,name='det'),
]