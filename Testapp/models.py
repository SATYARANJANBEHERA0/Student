from django.db import models

# Create your models here.
class Student(models.Model):
    Firstname = models.CharField(max_length=100)
    Lasttname = models.CharField(max_length=100)
    Email = models.EmailField()
    Password = models.CharField(max_length=100)
    Occupation = models.CharField(max_length=100)
    Gender = models.CharField(max_length=100)
    DOB = models.DateField()
    Education = models.CharField(max_length=100)
    State = models.CharField(max_length=100)
    Country = models.CharField(max_length=100)
