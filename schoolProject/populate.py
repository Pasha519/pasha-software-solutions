import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','schoolProject.settings')
import django
django.setup()

from testApp.models import Student
from faker import Faker
from random import *
import random


faker = Faker()
def populate(n):
    for i in range(n):
        fname = faker.name()
        frollno = randint(1,30)
        fclass = randint(1,5)
        ftelugu = randint(1,100)
        fsocial = randint(1,100)
        fscience = randint(1,100)
        fenglish = randint(1,100)
        fmaths = randint(1,100)
        ftotal = ftelugu+fsocial+fscience+fenglish+fmaths

        std_records = Student.objects.get_or_create(name=fname,rollno=frollno,class_std=fclass,telugu=ftelugu,social=fsocial,
                                                    science=fscience,english=fenglish,maths=fmaths,total=ftotal)

populate(30)

