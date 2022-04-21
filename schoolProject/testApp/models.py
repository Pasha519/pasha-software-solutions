from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=40)
    rollno = models.IntegerField()
    class_std = models.IntegerField()
    telugu = models.IntegerField()
    english = models.IntegerField()
    social = models.IntegerField()
    maths = models.IntegerField()
    science = models.IntegerField()
    total = models.IntegerField()
