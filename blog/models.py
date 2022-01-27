from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=150) #How many characters we want
    description = models.TextField()
    date = models.DateField()
    
    #return the name in more scripting way
    def __str__(self):
        return self.title