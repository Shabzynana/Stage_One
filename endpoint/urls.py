from django.urls import path
from . import views

urlpatterns = [
    path('mee/', views.index, name='index'),
]
