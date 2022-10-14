from django.db import models

# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=64)
    department = models.CharField(max_length=64)
    cost = models.IntegerField()