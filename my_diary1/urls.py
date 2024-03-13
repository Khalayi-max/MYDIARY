'''Defines urls for my_diary1.'''
from django.urls import path

from . import views

#namespace below
app_name = 'my_diary1'

urlpatterns = [
    #homepage

    path('', views.homepage, name = 'homepage'),
    path('days/', views.days, name = 'days'),
    #path('thoughts/',views.thoughts , name = 'thoughts'),

]