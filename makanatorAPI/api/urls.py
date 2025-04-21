from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('play/', views.play, name='play'),
    path('howtoplay/', views.howtoplay, name='howtoplay'),
    path('trueorfalse/', views.trueorfalse, name='trueorfalse'),
    path('result_true/', views.result_true, name='result_true'),
]
