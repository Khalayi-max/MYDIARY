'''Defines urls for my_diary1.'''
from django.urls import path

from . import views

#namespace below
app_name = 'my_diary1'

urlpatterns = [
    #homepage

    path('', views.homepage, name = 'homepage'),
    path('days/', views.days, name = 'days'),
    path('days/int<day_id>/', views.day, name = 'day'),
    path('new_day/', views.new_day, name= 'new_day'),
    path('new_thought/int<day_id>/', views.new_thought, name = 'new_thought'),
    path('edit_thought/int<thought_id>/', views.edit_thought, name ='edit_thought'),
    #path('thoughts/',views.thoughts , name = 'thoughts'),

]