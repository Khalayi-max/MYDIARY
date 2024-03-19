from django import forms

from .models import Day

from .models import Thought

class DayForm(forms.ModelForm):
    class Meta:
        model = Day
        fields = ['day_name']
        labels = {'day_name': ''}

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = Thought
        fields = ['text']
        labels = {'text': ''}
    