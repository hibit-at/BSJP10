from django.db import models

# Create your models here.

class Ranking(models.Model):
    date = models.DateTimeField()
    n0 = models.CharField(default='', max_length=50)
    n1 = models.CharField(default='', max_length=50)
    n2 = models.CharField(default='', max_length=50)
    n3 = models.CharField(default='', max_length=50)
    n4 = models.CharField(default='', max_length=50)
    n5 = models.CharField(default='', max_length=50)
    n6 = models.CharField(default='', max_length=50)
    n7 = models.CharField(default='', max_length=50)
    n8 = models.CharField(default='', max_length=50)
    n9 = models.CharField(default='', max_length=50)
