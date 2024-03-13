from django.contrib import admin

# Register your models here.
#Import module models fromm app to access 
#class Day from the model.py dir
from my_diary1.models import Day

from my_diary1.models import Thought


admin.site.register(Day)
admin.site.register(Thought)