from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib.auth.decorators import login_required

from .models import Day,Thought
from .forms import DayForm,ThoughtForm


# Create your views here.
def homepage(request):
    '''this gives value of the homepage'''
    return render(request, 'my_diary1/homepage.html')

@login_required
def days(request):
    days = Day.objects.filter(owner=request.user).order_by('date')
    context = {'days': days}
    return render(request, 'my_diary1/days.html', context)

@login_required
def day(request,day_id):
    day = Day.objects.get(id=day_id)
    if day.owner != request.user:
        raise Http404
    thoughts = day.thought_set.order_by('date')
    context = {'day': day, 'thoughts': thoughts}
    return render(request, 'my_diary1/day.html', context)

#adding new day
@login_required
def new_day(request):
    if request.method != 'POST':
        form = DayForm()
    else:
        form = DayForm(request.POST)
        if form.is_valid():
            new_day = form.save(commit=False)
            new_day.owner = request.user
            new_day.save()
            
            return HttpResponseRedirect(reverse('my_diary1:days'))
        
    context = {'form': form}
    return render (request, 'my_diary1/new_day.html', context )

@login_required
def new_thought(request,day_id):
    day = Day.objects.get(id=day_id)

    if request.method != 'POST':
        form = ThoughtForm()
    else:
        form = ThoughtForm(data=request.POST)
        if form.is_valid():
            new_thought = form.save(commit=False)
            new_thought.day = day
            new_thought.save()
            return HttpResponseRedirect(reverse('my_diary1:day', args=[day_id]))
        
    context = {'day': day, 'form': form}
    return render(request, 'my_diary1/new_thought.html', context)

@login_required
def edit_thought(request,thought_id):
    thought = Thought.objects.get(id=thought_id)
    day = thought.day
    if day.owner != request.user:
        raise Http404

    if request.method != 'POST':
        form = ThoughtForm(instance=thought)
    else:
        form = ThoughtForm(instance=thought,data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('my_diary1:day', args=[day.id]))
        
    context ={'thought': thought, 'day': day, 'form': form}
    return render(request, 'my_diary1/edit_thought.html', context)