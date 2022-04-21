from django.contrib import admin
from testApp.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['name','rollno','class_std','telugu','english','social','maths','science','total']
    list_filter = ('name','rollno','class_std')
admin.site.register(Student,StudentAdmin)