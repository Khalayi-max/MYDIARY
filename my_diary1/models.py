from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Day(models.Model):
    '''The day when a user is writing their thoughts'''
    day_name = models.CharField(max_length = 10)
    date = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return self.day_name
    
#define the thoughts model
class Thought(models.Model):
    '''Thoughts you want to let out about that particular day'''
    day = models.ForeignKey(Day, on_delete=models.CASCADE)
    # ForeignKey should specify the on_delete behavior, here set to CASCADE
    #foreignkey is used to refer to another record in the database
    #connects the thoughs oa a user to the specific day
    text = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    #more information on managing the model you can adda meta class

    def __str__(self):#the __str__ method tells django what to show when a thought is called
        #return the first 30 words
        if len(self.text) > 30:
            return self.text[:30] + '...'
        else:
            return self.text
        