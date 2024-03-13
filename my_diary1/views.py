from django.shortcuts import render
#from django.http import HttpResponse
from .models import Day


# Create your views here.
def homepage(request):
    '''this gives value of the homepage'''
    return render(request, 'my_diary1/homepage.html')


def days(request):
    days = Day.objects.order_by('date')
    context = {'day': days}
    return render(request, 'my_diary1/days.html', context)
