from django.db import models


# Create your models here.
class exchange_rate(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField()

    def str(self):
        return self.title