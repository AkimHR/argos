from django.urls import path
from . import views

urlpatterns = [
    
    path("", views.crew, name='index'),
]